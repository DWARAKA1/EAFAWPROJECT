from crewai import Crew, Process
from src.agents.finance_agents import FinanceAgents
from src.tasks.finance_tasks import FinanceTasks
from src.tools.finance_tools import financial_data_tool, risk_calculator_tool, budget_analyzer_tool, compliance_checker_tool

class FinanceCrew:
    def __init__(self):
        self.agents = FinanceAgents()
        self.tasks = FinanceTasks()
        self.tools = [
            financial_data_tool,
            risk_calculator_tool,
            budget_analyzer_tool,
            compliance_checker_tool
        ]

    def financial_analysis_crew(self, financial_data):
        # Create agents
        financial_analyst = self.agents.financial_analyst_agent()
        risk_manager = self.agents.risk_manager_agent()
        
        # Assign tools to agents
        financial_analyst.tools = self.tools
        risk_manager.tools = self.tools
        
        # Create tasks
        analysis_task = self.tasks.financial_analysis_task(financial_analyst, financial_data)
        risk_task = self.tasks.risk_assessment_task(risk_manager, financial_data)
        
        # Create crew
        crew = Crew(
            agents=[financial_analyst, risk_manager],
            tasks=[analysis_task, risk_task],
            process=Process.sequential,
            verbose=True
        )
        
        return crew

    def budget_management_crew(self, budget_data):
        # Create agents
        budget_controller = self.agents.budget_controller_agent()
        compliance_officer = self.agents.compliance_officer_agent()
        
        # Assign tools
        budget_controller.tools = self.tools
        compliance_officer.tools = self.tools
        
        # Create tasks
        budget_task = self.tasks.budget_monitoring_task(budget_controller, budget_data)
        compliance_task = self.tasks.compliance_check_task(compliance_officer, budget_data)
        
        # Create crew
        crew = Crew(
            agents=[budget_controller, compliance_officer],
            tasks=[budget_task, compliance_task],
            process=Process.sequential,
            verbose=True
        )
        
        return crew

    def investment_advisory_crew(self, investment_data):
        # Create agents
        investment_advisor = self.agents.investment_advisor_agent()
        risk_manager = self.agents.risk_manager_agent()
        compliance_officer = self.agents.compliance_officer_agent()
        
        # Assign tools
        investment_advisor.tools = self.tools
        risk_manager.tools = self.tools
        compliance_officer.tools = self.tools
        
        # Create tasks
        investment_task = self.tasks.investment_analysis_task(investment_advisor, investment_data)
        risk_task = self.tasks.risk_assessment_task(risk_manager, investment_data)
        compliance_task = self.tasks.compliance_check_task(compliance_officer, investment_data)
        
        # Create crew
        crew = Crew(
            agents=[investment_advisor, risk_manager, compliance_officer],
            tasks=[investment_task, risk_task, compliance_task],
            process=Process.sequential,
            verbose=True
        )
        
        return crew

    def comprehensive_finance_crew(self, financial_data, budget_data, investment_data):
        # Create all agents
        financial_analyst = self.agents.financial_analyst_agent()
        risk_manager = self.agents.risk_manager_agent()
        budget_controller = self.agents.budget_controller_agent()
        investment_advisor = self.agents.investment_advisor_agent()
        compliance_officer = self.agents.compliance_officer_agent()
        
        # Assign tools to all agents
        for agent in [financial_analyst, risk_manager, budget_controller, investment_advisor, compliance_officer]:
            agent.tools = self.tools
        
        # Create all tasks
        analysis_task = self.tasks.financial_analysis_task(financial_analyst, financial_data)
        risk_task = self.tasks.risk_assessment_task(risk_manager, financial_data)
        budget_task = self.tasks.budget_monitoring_task(budget_controller, budget_data)
        investment_task = self.tasks.investment_analysis_task(investment_advisor, investment_data)
        compliance_task = self.tasks.compliance_check_task(compliance_officer, 
                                                         f"{financial_data}, {budget_data}, {investment_data}")
        
        # Create comprehensive crew
        crew = Crew(
            agents=[financial_analyst, risk_manager, budget_controller, investment_advisor, compliance_officer],
            tasks=[analysis_task, risk_task, budget_task, investment_task, compliance_task],
            process=Process.sequential,
            verbose=True
        )
        
        return crew