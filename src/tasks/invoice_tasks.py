from crewai import Task
from typing import Any, Dict
from src.common.logger import get_logger

logger = get_logger(__name__)

class InvoiceTasks:
    @staticmethod
    def invoice_extraction_task(agent, invoice_data: Dict[str, Any]) -> Task:
        """Create task for invoice data extraction"""
        return Task(
            description=f"""
            Extract and structure data from the invoice document:
            1. Use OCR to process the document
            2. Extract key fields (invoice number, date, amount, vendor, line items)
            3. Validate extracted data format
            4. Return structured data
            
            Invoice data: {invoice_data}
            """,
            agent=agent
        )

    @staticmethod
    def invoice_validation_task(agent, invoice_data: Dict[str, Any]) -> Task:
        """Create task for invoice validation"""
        return Task(
            description=f"""
            Validate the extracted invoice data:
            1. Check vendor details in ERP
            2. Verify purchase order match
            3. Validate line items and amounts
            4. Check for duplicates
            5. Verify budget availability
            
            Invoice data: {invoice_data}
            """,
            agent=agent
        )

    @staticmethod
    def approval_routing_task(agent, invoice_data: Dict[str, Any]) -> Task:
        """Create task for approval routing"""
        return Task(
            description=f"""
            Route invoice for appropriate approvals:
            1. Determine approval chain based on amount and department
            2. Send notifications to approvers
            3. Track approval status
            4. Handle approval/rejection actions
            
            Invoice data: {invoice_data}
            """,
            agent=agent,
            requires_human_input=True  # Enable human approver interaction
        )

    @staticmethod
    def payment_execution_task(agent, invoice_data: Dict[str, Any]) -> Task:
        """Create task for payment execution"""
        return Task(
            description=f"""
            Execute payment for approved invoice:
            1. Prepare payment data
            2. Submit to payment gateway
            3. Record transaction details
            4. Update payment status
            
            Invoice data: {invoice_data}
            """,
            agent=agent
        )

    @staticmethod
    def compliance_check_task(agent, invoice_data: Dict[str, Any]) -> Task:
        """Create task for compliance verification"""
        return Task(
            description=f"""
            Ensure compliance throughout the process:
            1. Verify policy adherence
            2. Maintain audit trail
            3. Check regulatory requirements
            4. Generate compliance report
            
            Invoice data: {invoice_data}
            """,
            agent=agent
        )