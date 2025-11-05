from dataclasses import dataclass
from src.config.workflow_config import WorkflowConfig
from src.services.finance_service import FinanceService

@dataclass
class ServiceContainer:
    """Container for service dependencies"""
    config: WorkflowConfig
    finance_service: FinanceService

class DependencyProvider:
    """Dependency injection container"""
    
    _instance = None
    _container = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DependencyProvider, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance
    
    def _initialize(self):
        """Initialize service container"""
        # Create configuration
        config = WorkflowConfig()
        
        # Create services
        finance_service = FinanceService()
        
        # Create container
        self._container = ServiceContainer(
            config=config,
            finance_service=finance_service
        )
    
    @property
    def container(self) -> ServiceContainer:
        """Get service container"""
        return self._container
    
    def get_finance_service(self) -> FinanceService:
        """Get finance service instance"""
        return self._container.finance_service
    
    def get_config(self) -> WorkflowConfig:
        """Get configuration instance"""
        return self._container.config