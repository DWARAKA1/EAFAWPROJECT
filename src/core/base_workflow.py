from abc import ABC, abstractmethod
from typing import Dict, Any
from src.common.logger import get_logger

logger = get_logger(__name__)

class BaseWorkflow(ABC):
    """
    Abstract base class for all workflows in the system.
    Provides common functionality and enforces consistent interface.
    """
    
    def __init__(self):
        """Initialize base workflow components"""
        pass
    
    @abstractmethod
    def process_invoice(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Abstract method that must be implemented by all workflow classes
        
        Args:
            data: Dictionary containing workflow input data
            
        Returns:
            Dict containing workflow results
        """
        pass
    
    def validate_input(self, data: Dict[str, Any]) -> bool:
        """
        Validate workflow input data
        
        Args:
            data: Dictionary containing workflow input data
            
        Returns:
            bool indicating if input is valid
        """
        try:
            # Implement common validation logic here
            return True
        except Exception as e:
            logger.error(f"Input validation error: {str(e)}")
            return False
    
    def log_workflow_step(self, step_name: str, step_data: Dict[str, Any]) -> None:
        """
        Log workflow step execution
        
        Args:
            step_name: Name of the workflow step
            step_data: Data associated with the step
        """
        try:
            logger.info(f"Executing workflow step: {step_name}")
            logger.debug(f"Step data: {step_data}")
        except Exception as e:
            logger.error(f"Error logging workflow step: {str(e)}")
    
    def handle_error(self, error: Exception, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Handle workflow errors consistently
        
        Args:
            error: Exception that occurred
            context: Context information about where the error occurred
            
        Returns:
            Dict containing error information
        """
        error_info = {
            "error_type": type(error).__name__,
            "error_message": str(error),
            "context": context
        }
        logger.error(f"Workflow error: {error_info}")
        return error_info