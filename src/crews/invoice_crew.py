from crewai import Crew, Process
from src.agents.invoice_agents import InvoiceAgents
from src.tasks.invoice_tasks import InvoiceTasks
from src.tools.invoice_tools import invoice_processing_tools
from typing import Dict, Any
from src.common.logger import get_logger

logger = get_logger(__name__)

class InvoiceCrew:
    """Crew for Invoice-to-Pay workflow automation"""
    
    def __init__(self):
        self.agents = InvoiceAgents()
        self.tasks = InvoiceTasks()
        self.tools = invoice_processing_tools

    def invoice_processing_crew(self, invoice_data: Dict[str, Any]) -> Crew:
        """Create crew for invoice processing workflow"""
        
        # Create specialized agents
        ingestion_agent = self.agents.invoice_ingestion_agent()
        validation_agent = self.agents.validation_agent()
        approval_agent = self.agents.approval_routing_agent()
        payment_agent = self.agents.payment_agent()
        compliance_agent = self.agents.compliance_agent()
        
        # Assign tools to agents
        for agent in [ingestion_agent, validation_agent, approval_agent, 
                     payment_agent, compliance_agent]:
            agent.tools = self.tools
        
        # Create sequential tasks
        extraction_task = self.tasks.invoice_extraction_task(
            ingestion_agent, invoice_data)
        validation_task = self.tasks.invoice_validation_task(
            validation_agent, invoice_data)
        approval_task = self.tasks.approval_routing_task(
            approval_agent, invoice_data)
        payment_task = self.tasks.payment_execution_task(
            payment_agent, invoice_data)
        compliance_task = self.tasks.compliance_check_task(
            compliance_agent, invoice_data)
        
        # Create crew with sequential process
        crew = Crew(
            agents=[
                ingestion_agent,
                validation_agent,
                approval_agent,
                payment_agent,
                compliance_agent
            ],
            tasks=[
                extraction_task,
                validation_task,
                approval_task,
                payment_task,
                compliance_task
            ],
            process=Process.sequential,
            verbose=True
        )
        
        return crew