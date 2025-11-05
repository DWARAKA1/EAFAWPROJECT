from src.core.base_workflow import BaseWorkflow
from src.crews.invoice_crew import InvoiceCrew
from typing import Dict, Any
from src.common.logger import get_logger

logger = get_logger(__name__)

class InvoiceWorkflow(BaseWorkflow):
    """Workflow for Invoice-to-Pay process"""
    
    def __init__(self):
        super().__init__()
        self.invoice_crew = InvoiceCrew()
    
    def process_invoice(self, invoice_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the full Invoice-to-Pay workflow
        
        Args:
            invoice_data: Dictionary containing invoice information and document path
            
        Returns:
            Dict containing workflow results and status
        """
        try:
            logger.info(f"Starting invoice processing workflow for invoice: {invoice_data.get('invoice_id', 'Unknown')}")
            
            # Create and execute the invoice processing crew
            crew = self.invoice_crew.invoice_processing_crew(invoice_data)
            result = crew.kickoff()
            
            # Process and structure the results
            workflow_result = {
                "status": "SUCCESS",
                "invoice_id": invoice_data.get("invoice_id"),
                "workflow_results": result,
                "payment_status": "Completed",
                "audit_trail": {
                    "extraction_status": "Completed",
                    "validation_status": "Completed",
                    "approval_status": "Approved",
                    "payment_status": "Processed"
                }
            }
            
            logger.info(f"Successfully completed invoice processing workflow for invoice: {invoice_data.get('invoice_id', 'Unknown')}")
            return workflow_result
            
        except Exception as e:
            error_msg = f"Error in invoice processing workflow: {str(e)}"
            logger.error(error_msg)
            return {
                "status": "FAILED",
                "invoice_id": invoice_data.get("invoice_id"),
                "error": error_msg
            }