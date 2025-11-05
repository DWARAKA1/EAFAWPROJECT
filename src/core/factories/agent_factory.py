from typing import Dict, Type
from src.core.interfaces.agent_interface import BaseAgent
from src.agents.finance_agents import FinanceAgents
from src.agents.invoice_agents import InvoiceAgents

class AgentFactory:
    """Factory for creating agent providers"""
    
    _agent_types: Dict[str, Type[BaseAgent]] = {
        'finance': FinanceAgents,
        'invoice': InvoiceAgents
    }
    
    @classmethod
    def get_agent_provider(cls, agent_type: str) -> BaseAgent:
        """
        Get agent provider by type
        
        Args:
            agent_type: Type of agent provider to create
            
        Returns:
            Instance of agent provider
            
        Raises:
            ValueError: If agent type is not supported
        """
        if agent_type not in cls._agent_types:
            raise ValueError(f"Unsupported agent type: {agent_type}")
            
        return cls._agent_types[agent_type]()