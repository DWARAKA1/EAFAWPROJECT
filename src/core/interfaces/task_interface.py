from abc import ABC, abstractmethod
from typing import Dict, Any
from crewai import Task

class BaseTask(ABC):
    """Abstract base class for all task providers"""
    
    @abstractmethod
    def create_task(self, description: str, agent: Any, context: Dict[str, Any] = None) -> Task:
        """Create a task with specified parameters"""
        pass
    
    @abstractmethod
    def get_task_context(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Get context for task execution"""
        pass