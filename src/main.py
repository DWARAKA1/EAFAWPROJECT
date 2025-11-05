"""
Enterprise Agentic Finance Automation Workflow
Main application entry point
"""

import sys
from pathlib import Path
from dotenv import load_dotenv
from src.workflows.finance_workflow import FinanceWorkflow
from src.models.finance_models import FinanceWorkflowInput, WorkflowType
from src.common.logger import get_logger

# Add src to Python path
src_path = Path(__file__).parent
sys.path.insert(0, str(src_path))

# Load environment variables
load_dotenv()

logger = get_logger(__name__)
logger.info("TEST LOG ENTRY: Logger setup is working and writing to file.")

def main():
    """Main application entry point"""
    logger.info("Enterprise Agentic Finance Automation Workflow")
    logger.info("=" * 50)
    
    # Initialize workflow engine
    finance_workflow = FinanceWorkflow()
    
    # Example usage
    logger.info("Running sample financial analysis workflow...")
    
    # Sample input data
    sample_input = FinanceWorkflowInput(
        workflow_type=WorkflowType.FINANCIAL_ANALYSIS,
        financial_data={
            "company": "Sample Corp",
            "revenue": 1000000,
            "expenses": 800000,
            "assets": 2000000,
            "liabilities": 500000
        },
        user_id="demo_user",
        organization_id="demo_org"
    )
    
    try:
        # Execute workflow
        result = finance_workflow.execute_financial_analysis_workflow(sample_input)
        logger.info(f"Workflow Status: {result.status}")
        logger.info(f"Workflow Type: {result.workflow_type}")
        if result.status == "SUCCESS":
            logger.info(f"Results: {result.results}")
            if result.recommendations:
                for category, items in result.recommendations.items():
                    if items:
                        logger.info(f"{category.replace('_', ' ').title()}: {items}")
        else:
            logger.error(f"Error: {result.error_message}")
    except Exception as e:
        logger.error(f"Failed to execute workflow: {str(e)}")
    logger.info("=" * 50)
    logger.info("To start the API server, run: python -m src.api.finance_api")
    logger.info("To start the Streamlit app, run: streamlit run src/frontend/streamlit_app.py")

if __name__ == "__main__":
    main()