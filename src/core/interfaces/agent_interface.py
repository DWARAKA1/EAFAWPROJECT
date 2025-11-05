from abc import ABC, abstractmethod
from typing import List
from crewai import Agent, Tool

class BaseAgent(ABC):
    """Abstract base class for all agent providers"""
    
    @abstractmethod
    def get_llm(self):
        """Get the language model for the agent"""
        pass
    
    @abstractmethod
    def create_agent(self, role: str, goal: str, backstory: str, tools: List[Tool] = None) -> Agent:
        """Create an agent with specified parameters"""
        pass
    
    @property
    @abstractmethod
    def tools(self) -> List[Tool]:
        """Get tools available to the agent"""
        pass