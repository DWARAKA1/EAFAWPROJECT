from fastapi import FastAPI, HTTPException, BackgroundTasks
from starlette.middleware.cors import CORSMiddleware
from src.workflows.finance_workflow import FinanceWorkflow
from src.models.finance_models import FinanceWorkflowInput, FinanceWorkflowOutput, WorkflowType
import uuid
from typing import Dict
import logging

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

# Initialize workflow engine
finance_workflow = FinanceWorkflow()
workflow_store: Dict[str, FinanceWorkflowOutput] = {}

@app.post("/api/v1/workflows/financial-analysis", response_model=FinanceWorkflowOutput)
async def execute_financial_analysis(
    input_data: FinanceWorkflowInput,
    background_tasks: BackgroundTasks
):
    """Execute financial analysis workflow"""
    try:
        workflow_id = str(uuid.uuid4())
        input_data.workflow_type = WorkflowType.FINANCIAL_ANALYSIS
        
        # Execute workflow in background
        background_tasks.add_task(
            run_workflow_background,
            workflow_id,
            "financial_analysis",
            input_data
        )
        
        return FinanceWorkflowOutput(
            workflow_id=workflow_id,
            status="RUNNING",
            workflow_type=WorkflowType.FINANCIAL_ANALYSIS
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/workflows/budget-management", response_model=FinanceWorkflowOutput)
async def execute_budget_management(
    input_data: FinanceWorkflowInput,
    background_tasks: BackgroundTasks
):
    """Execute budget management workflow"""
    try:
        workflow_id = str(uuid.uuid4())
        input_data.workflow_type = WorkflowType.BUDGET_MANAGEMENT
        
        background_tasks.add_task(
            run_workflow_background,
            workflow_id,
            "budget_management",
            input_data
        )
        
        return FinanceWorkflowOutput(
            workflow_id=workflow_id,
            status="RUNNING",
            workflow_type=WorkflowType.BUDGET_MANAGEMENT
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/workflows/investment-advisory", response_model=FinanceWorkflowOutput)
async def execute_investment_advisory(
    input_data: FinanceWorkflowInput,
    background_tasks: BackgroundTasks
):
    """Execute investment advisory workflow"""
    try:
        workflow_id = str(uuid.uuid4())
        input_data.workflow_type = WorkflowType.INVESTMENT_ADVISORY
        
        background_tasks.add_task(
            run_workflow_background,
            workflow_id,
            "investment_advisory",
            input_data
        )
        
        return FinanceWorkflowOutput(
            workflow_id=workflow_id,
            status="RUNNING",
            workflow_type=WorkflowType.INVESTMENT_ADVISORY
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/workflows/comprehensive", response_model=FinanceWorkflowOutput)
async def execute_comprehensive_workflow(
    input_data: FinanceWorkflowInput,
    background_tasks: BackgroundTasks
):
    """Execute comprehensive finance workflow"""
    try:
        workflow_id = str(uuid.uuid4())
        input_data.workflow_type = WorkflowType.COMPREHENSIVE
        
        background_tasks.add_task(
            run_workflow_background,
            workflow_id,
            "comprehensive",
            input_data
        )
        
        return FinanceWorkflowOutput(
            workflow_id=workflow_id,
            status="RUNNING",
            workflow_type=WorkflowType.COMPREHENSIVE
        )
    except Exception as e:
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

async def run_workflow_background(workflow_id: str, workflow_type: str, input_data: FinanceWorkflowInput):
    """Run workflow in background task"""
    try:
        if workflow_type == "financial_analysis":
            result = finance_workflow.execute_financial_analysis_workflow(input_data)
        elif workflow_type == "budget_management":
            result = finance_workflow.execute_budget_management_workflow(input_data)
        elif workflow_type == "investment_advisory":
            result = finance_workflow.execute_investment_advisory_workflow(input_data)
        elif workflow_type == "comprehensive":
            result = finance_workflow.execute_comprehensive_workflow(input_data)
        else:
            raise ValueError(f"Unknown workflow type: {workflow_type}")
        
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
        logging.error(f"Workflow {workflow_id} failed: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)