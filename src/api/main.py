"""
Enterprise Agentic Finance Automation API
Main FastAPI application
"""

from fastapi import FastAPI, HTTPException, BackgroundTasks, Depends
from starlette.middleware.cors import CORSMiddleware
from src.models.finance_models import FinanceWorkflowInput, FinanceWorkflowOutput, WorkflowType
from src.core.dependencies import DependencyProvider
from src.services.finance_service import FinanceService
import uuid
from typing import Dict
from src.common.logger import get_logger

logger = get_logger(__name__)

app = FastAPI(
    title="Enterprise Agentic Finance Automation API",
    description="AI-powered finance automation workflow using CrewAI",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency injection
def get_finance_service() -> FinanceService:
    """Get finance service instance"""
    return DependencyProvider().get_finance_service()

# Workflow store for background tasks
workflow_store: Dict[str, FinanceWorkflowOutput] = {}

@app.post("/api/v1/workflows/invoice", response_model=FinanceWorkflowOutput)
async def process_invoice(
    input_data: FinanceWorkflowInput,
    background_tasks: BackgroundTasks,
    finance_service: FinanceService = Depends(get_finance_service)
):
    """Process invoice through workflow"""
    try:
        workflow_id = str(uuid.uuid4())
        
        # Execute workflow in background
        background_tasks.add_task(
            run_workflow_background,
            workflow_id,
            input_data,
            finance_service
        )
        
        return FinanceWorkflowOutput(
            workflow_id=workflow_id,
            status="RUNNING",
            workflow_type=WorkflowType.INVOICE_PROCESSING
        )
    except Exception as e:
        logger.error(f"Error starting invoice workflow: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/workflows/{workflow_id}/status", response_model=FinanceWorkflowOutput)
async def get_workflow_status(workflow_id: str):
    """Get workflow execution status"""
    if workflow_id not in workflow_store:
        raise HTTPException(status_code=404, detail="Workflow not found")
    
    return workflow_store[workflow_id]

@app.get("/api/v1/workflows/{workflow_id}/results")
async def get_workflow_results(workflow_id: str):
    """Get workflow execution results"""
    if workflow_id not in workflow_store:
        raise HTTPException(status_code=404, detail="Workflow not found")
    
    workflow_output = workflow_store[workflow_id]
    if workflow_output.status != "SUCCESS":
        raise HTTPException(status_code=400, detail="Workflow not completed successfully")
    
    return {
        "workflow_id": workflow_id,
        "results": workflow_output.results,
        "recommendations": workflow_output.recommendations
    }

@app.get("/api/v1/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "Enterprise Finance Automation API"}

async def run_workflow_background(
    workflow_id: str,
    input_data: FinanceWorkflowInput,
    finance_service: FinanceService
):
    """Run workflow in background task"""
    try:
        result = finance_service.process_invoice(input_data)
        result.workflow_id = workflow_id
        workflow_store[workflow_id] = result
        
    except Exception as e:
        error_result = FinanceWorkflowOutput(
            workflow_id=workflow_id,
            status="FAILED",
            workflow_type=input_data.workflow_type,
            error_message=str(e)
        )
        workflow_store[workflow_id] = error_result
        logger.error(f"Workflow {workflow_id} failed: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)