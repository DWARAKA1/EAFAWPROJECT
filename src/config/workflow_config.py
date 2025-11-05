from typing import Dict, Any
from pydantic import BaseSettings
from functools import lru_cache

class FinanceSettings(BaseSettings):
    """Settings for finance workflows"""
    
    # API Keys
    GROQ_API_KEY: str
    CREW_API_KEY: str
    
    # LLM Configuration
    LLM_MODEL: str = "mixtral-8x7b-32768"
    LLM_TEMPERATURE: float = 0.0
    
    # Workflow Configuration
    MAX_RETRIES: int = 3
    TIMEOUT_SECONDS: int = 300
    ENABLE_HUMAN_APPROVAL: bool = True
    
    # Logging Configuration
    LOG_LEVEL: str = "INFO"
    ENABLE_AUDIT_LOG: bool = True
    
    # Integration Settings
    ERP_API_URL: str = ""
    PAYMENT_GATEWAY_URL: str = ""
    OCR_SERVICE_URL: str = ""
    
    class Config:
        env_file = ".env"
        case_sensitive = True

@lru_cache()
def get_settings() -> FinanceSettings:
    """
    Get cached settings instance
    
    Returns:
        Singleton instance of FinanceSettings
    """
    return FinanceSettings()

class WorkflowConfig:
    """Configuration manager for workflows"""
    
    def __init__(self):
        self.settings = get_settings()
        
    def get_llm_config(self) -> Dict[str, Any]:
        """Get LLM configuration"""
        return {
            "model": self.settings.LLM_MODEL,
            "temperature": self.settings.LLM_TEMPERATURE,
            "api_key": self.settings.GROQ_API_KEY
        }
    
    def get_workflow_config(self) -> Dict[str, Any]:
        """Get workflow configuration"""
        return {
            "max_retries": self.settings.MAX_RETRIES,
            "timeout": self.settings.TIMEOUT_SECONDS,
            "enable_human_approval": self.settings.ENABLE_HUMAN_APPROVAL
        }
    
    def get_integration_config(self) -> Dict[str, Any]:
        """Get integration configuration"""
        return {
            "erp_api_url": self.settings.ERP_API_URL,
            "payment_gateway_url": self.settings.PAYMENT_GATEWAY_URL,
            "ocr_service_url": self.settings.OCR_SERVICE_URL
        }