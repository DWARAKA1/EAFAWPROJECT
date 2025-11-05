from abc import ABC, abstractmethod
from crewai import Agent
from langchain_groq import ChatGroq
import os
from typing import Optional

class BaseFinanceAgent(ABC):
    """Base class for all finance agents"""
    
    def __init__(self, llm: Optional[ChatGroq] = None):
        self.llm = llm or self._create_default_llm()
    
    def _create_default_llm(self) -> ChatGroq:
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY environment variable not set")
        return ChatGroq(
            temperature=0,
            groq_api_key=api_key,
            model_name="mixtral-8x7b-32768"
        )
    
    @abstractmethod
    def get_role(self) -> str:
        pass
    
    @abstractmethod
    def get_goal(self) -> str:
        pass
    
    @abstractmethod
    def get_backstory(self) -> str:
        pass
    
    def create_agent(self) -> Agent:
        return Agent(
            role=self.get_role(),
            goal=self.get_goal(),
            backstory=self.get_backstory(),
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )