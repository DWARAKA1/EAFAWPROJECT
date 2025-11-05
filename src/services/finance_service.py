from typing import Dict, Any
from src.core.factories.agent_factory import AgentFactory
from src.core.factories.tool_factory import ToolFactory
from src.config.workflow_config import WorkflowConfig
from src.common.logger import get_logger
from src.models.finance_models import FinanceWorkflowInput, FinanceWorkflowOutput

logger = get_logger(__name__)

class FinanceService:
    """Service layer for finance operations"""
    
    def __init__(self):
        self.config = WorkflowConfig()
        self.logger = logger
    
    def process_invoice(self, input_data: FinanceWorkflowInput) -> FinanceWorkflowOutput:
        """
        Process invoice through workflow
        
        Args:
            input_data: Finance workflow input data
            
        Returns:
            Workflow execution results
        """
        try:
            # Get required tools
            tools = ToolFactory.get_tools_by_types(['invoice', 'finance'])
            
            # Get invoice agents
            agent_provider = AgentFactory.get_agent_provider('invoice')
            
            # Create and execute workflow
            workflow_config = self.config.get_workflow_config()
            
            # TODO: Implement workflow execution logic
            result = self._execute_workflow(input_data, tools, agent_provider, workflow_config)
            
            return FinanceWorkflowOutput(
                status="SUCCESS",
                workflow_type=input_data.workflow_type,
                results=result
            )
            
        except Exception as e:
            self.logger.error(f"Error processing invoice: {str(e)}")
            return FinanceWorkflowOutput(
                status="FAILED",
                workflow_type=input_data.workflow_type,
                error_message=str(e)
            )
    
    def _execute_workflow(
        self, 
        input_data: FinanceWorkflowInput,
        tools: list,
        agent_provider: Any,
        workflow_config: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Execute workflow with given configuration
        
        Args:
            input_data: Workflow input data
            tools: List of tools to use
            agent_provider: Provider for creating agents
            workflow_config: Workflow configuration
            
        Returns:
            Workflow execution results
        """
        # TODO: Implement workflow execution
        pass