from abc import ABC, abstractmethod
from crewai import Crew, Process
from src.agents.finance_agents import FinanceAgents
from src.tasks.finance_tasks import FinanceTasks
from src.tools.finance_tools import financial_data_tool, risk_calculator_tool, budget_analyzer_tool, compliance_checker_tool
from typing import Any

class BaseWorkflow(ABC):
    """Base workflow class"""
    
    def __init__(self):
        self.agents = FinanceAgents()
        self.tasks = FinanceTasks()
        self.tools = [financial_data_tool, risk_calculator_tool, budget_analyzer_tool, compliance_checker_tool]
    
    @abstractmethod
    def create_crew(self, data: Any) -> Crew:
        pass
    
    def execute(self, data: Any) -> Any:
        crew = self.create_crew(data)
        return crew.kickoff()

class FinancialAnalysisWorkflow(BaseWorkflow):
    def create_crew(self, data: Any) -> Crew:
        analyst = self.agents.financial_analyst_agent()
        risk_manager = self.agents.risk_manager_agent()
        
        analyst.tools = self.tools
        risk_manager.tools = self.tools
        
        analysis_task = self.tasks.financial_analysis_task(analyst, data)
        risk_task = self.tasks.risk_assessment_task(risk_manager, data)
        
        return Crew(
            agents=[analyst, risk_manager],
            tasks=[analysis_task, risk_task],
            process=Process.sequential,
            verbose=True
        )

class BudgetManagementWorkflow(BaseWorkflow):
    def create_crew(self, data: Any) -> Crew:
        controller = self.agents.budget_controller_agent()
        compliance = self.agents.compliance_officer_agent()
        
        controller.tools = self.tools
        compliance.tools = self.tools
        
        budget_task = self.tasks.budget_monitoring_task(controller, data)
        compliance_task = self.tasks.compliance_check_task(compliance, data)
        
        return Crew(
            agents=[controller, compliance],
            tasks=[budget_task, compliance_task],
            process=Process.sequential,
            verbose=True
        )

class InvestmentAdvisoryWorkflow(BaseWorkflow):
    def create_crew(self, data: Any) -> Crew:
        advisor = self.agents.investment_advisor_agent()
        risk_manager = self.agents.risk_manager_agent()
        
        advisor.tools = self.tools
        risk_manager.tools = self.tools
        
        investment_task = self.tasks.investment_analysis_task(advisor, data)
        risk_task = self.tasks.risk_assessment_task(risk_manager, data)
        
        return Crew(
            agents=[advisor, risk_manager],
            tasks=[investment_task, risk_task],
            process=Process.sequential,
            verbose=True
        )