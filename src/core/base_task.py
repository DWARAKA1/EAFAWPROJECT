from abc import ABC, abstractmethod
from crewai import Task, Agent
from typing import Any

class BaseFinanceTask(ABC):
    """Base class for all finance tasks"""
    
    @abstractmethod
    def get_description(self, data: Any) -> str:
        pass
    
    @abstractmethod
    def get_expected_output(self) -> str:
        pass
    
    def create_task(self, agent: Agent, data: Any) -> Task:
        return Task(
            description=self.get_description(data),
            agent=agent,
            expected_output=self.get_expected_output()
        )