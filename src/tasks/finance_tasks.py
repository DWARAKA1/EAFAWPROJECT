from src.core.base_task import BaseFinanceTask
from crewai import Task, Agent
from typing import Any

class FinancialAnalysisTask(BaseFinanceTask):
    def get_description(self, data: Any) -> str:
        return f"""
        Analyze financial data: {data}
        
        Include:
        1. Revenue trends and growth patterns
        2. Profitability analysis
        3. Liquidity ratios and cash flow
        4. Key performance indicators
        5. Industry benchmarks comparison
        6. Actionable recommendations
        """
    
    def get_expected_output(self) -> str:
        return "Comprehensive financial analysis report with insights and recommendations"

class RiskAssessmentTask(BaseFinanceTask):
    def get_description(self, data: Any) -> str:
        return f"""
        Conduct risk assessment on: {data}
        
        Cover:
        1. Market risk analysis
        2. Credit risk evaluation
        3. Operational risk identification
        4. Liquidity risk assessment
        5. Regulatory compliance risks
        6. Risk mitigation strategies
        """
    
    def get_expected_output(self) -> str:
        return "Detailed risk assessment report with mitigation strategies"

class BudgetMonitoringTask(BaseFinanceTask):
    def get_description(self, data: Any) -> str:
        return f"""
        Monitor budget performance: {data}
        
        Include:
        1. Budget vs actual variance analysis
        2. Expense category breakdown
        3. Budget overrun identification
        4. Forecast accuracy assessment
        5. Cost optimization opportunities
        6. Budget reallocation recommendations
        """
    
    def get_expected_output(self) -> str:
        return "Budget monitoring report with variance analysis and recommendations"

class InvestmentAnalysisTask(BaseFinanceTask):
    def get_description(self, data: Any) -> str:
        return f"""
        Analyze investment opportunities: {data}
        
        Include:
        1. Investment performance evaluation
        2. Risk-return analysis
        3. Portfolio diversification assessment
        4. Market timing considerations
        5. Asset allocation recommendations
        6. Expected returns and risk metrics
        """
    
    def get_expected_output(self) -> str:
        return "Investment analysis report with recommendations and risk metrics"

class ComplianceCheckTask(BaseFinanceTask):
    def get_description(self, data: Any) -> str:
        return f"""
        Review processes for compliance: {data}
        
        Cover:
        1. Regulatory compliance verification
        2. Internal policy adherence
        3. Audit trail completeness
        4. Documentation requirements
        5. Approval workflow validation
        6. Risk control effectiveness
        """
    
    def get_expected_output(self) -> str:
        return "Compliance review report with gap analysis and remediation plan"

class FinanceTasks:
    """Factory for creating finance tasks"""
    
    def __init__(self):
        self._tasks = {
            'financial_analysis': FinancialAnalysisTask(),
            'risk_assessment': RiskAssessmentTask(),
            'budget_monitoring': BudgetMonitoringTask(),
            'investment_analysis': InvestmentAnalysisTask(),
            'compliance_check': ComplianceCheckTask()
        }
    
    def financial_analysis_task(self, agent: Agent, data: Any) -> Task:
        return self._tasks['financial_analysis'].create_task(agent, data)
    
    def risk_assessment_task(self, agent: Agent, data: Any) -> Task:
        return self._tasks['risk_assessment'].create_task(agent, data)
    
    def budget_monitoring_task(self, agent: Agent, data: Any) -> Task:
        return self._tasks['budget_monitoring'].create_task(agent, data)
    
    def investment_analysis_task(self, agent: Agent, data: Any) -> Task:
        return self._tasks['investment_analysis'].create_task(agent, data)
    
    def compliance_check_task(self, agent: Agent, data: Any) -> Task:
        return self._tasks['compliance_check'].create_task(agent, data)