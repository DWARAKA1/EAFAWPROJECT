from abc import ABC, abstractmethod
from typing import List
from crewai import Tool

class BaseToolProvider(ABC):
    """Abstract base class for all tool providers"""
    
    @abstractmethod
    def get_tools(self) -> List[Tool]:
        """Get all available tools"""
        pass
    
    @abstractmethod
    def get_tool_by_name(self, name: str) -> Tool:
        """Get a specific tool by name"""
        pass
    
    @abstractmethod
    def register_tool(self, tool: Tool) -> None:
        """Register a new tool"""
        pass