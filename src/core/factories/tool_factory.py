from typing import Dict, Type, List
from src.core.interfaces.tool_interface import BaseToolProvider
from src.tools.finance_tools import FinanceTools
from src.tools.invoice_tools import InvoiceTools
from crewai import Tool

class ToolFactory:
    """Factory for creating tool providers"""
    
    _tool_types: Dict[str, Type[BaseToolProvider]] = {
        'finance': FinanceTools,
        'invoice': InvoiceTools
    }
    
    @classmethod
    def get_tool_provider(cls, tool_type: str) -> BaseToolProvider:
        """
        Get tool provider by type
        
        Args:
            tool_type: Type of tool provider to create
            
        Returns:
            Instance of tool provider
            
        Raises:
            ValueError: If tool type is not supported
        """
        if tool_type not in cls._tool_types:
            raise ValueError(f"Unsupported tool type: {tool_type}")
            
        return cls._tool_types[tool_type]()
    
    @classmethod
    def get_tools_by_types(cls, tool_types: List[str]) -> List[Tool]:
        """
        Get tools for multiple types
        
        Args:
            tool_types: List of tool types to get tools for
            
        Returns:
            Combined list of tools from all providers
        """
        tools = []
        for tool_type in tool_types:
            provider = cls.get_tool_provider(tool_type)
            tools.extend(provider.get_tools())
        return tools