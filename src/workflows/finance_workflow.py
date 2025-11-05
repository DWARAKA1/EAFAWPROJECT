from src.models.finance_models import FinanceWorkflowInput, FinanceWorkflowOutput, WorkflowStatus
from langchain_groq import ChatGroq
import os
from src.common.logger import get_logger

class FinanceWorkflow:
    """Direct Groq-based workflow without CrewAI"""
    
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY environment variable not set")
        self.llm = ChatGroq(
            temperature=0,
            groq_api_key=api_key,
            model_name="llama-3.1-8b-instant"
        )
        self.logger = get_logger(__name__)
    
    def execute_financial_analysis_workflow(self, input_data: FinanceWorkflowInput) -> FinanceWorkflowOutput:
        try:
            self.logger.info(f"[START] financial_analysis workflow for user: {input_data.user_id}, org: {input_data.organization_id}")
            
            prompt = f"""
            You are a Senior Financial Analyst. Analyze this financial data:
            {input_data.financial_data}
            
            Provide:
            1. Key financial insights
            2. Risk assessment
            3. Actionable recommendations
            4. Performance metrics
            
            Format as a professional financial analysis report.
            """
            
            result = self.llm.invoke(prompt)
            
            return FinanceWorkflowOutput(
                status=WorkflowStatus.SUCCESS,
                results=result.content,
                workflow_type=input_data.workflow_type,
                recommendations=self._extract_recommendations(result.content)
            )
        except Exception as e:
            self.logger.error(f"[ERROR] Financial analysis workflow failed: {str(e)}")
            return FinanceWorkflowOutput(
                status=WorkflowStatus.FAILED,
                error_message=str(e),
                workflow_type=input_data.workflow_type
            )
    
    def execute_budget_management_workflow(self, input_data: FinanceWorkflowInput) -> FinanceWorkflowOutput:
        try:
            self.logger.info(f"[START] budget_management workflow for user: {input_data.user_id}, org: {input_data.organization_id}")
            
            prompt = f"""
            You are a Budget Controller. Analyze this budget data:
            {input_data.budget_data}
            
            Provide:
            1. Budget variance analysis
            2. Expense optimization opportunities
            3. Cost control recommendations
            4. Budget reallocation suggestions
            """
            
            result = self.llm.invoke(prompt)
            
            return FinanceWorkflowOutput(
                status=WorkflowStatus.SUCCESS,
                results=result.content,
                workflow_type=input_data.workflow_type,
                recommendations={"budget_optimization": [result.content]}
            )
        except Exception as e:
            self.logger.error(f"[ERROR] Budget management workflow failed: {str(e)}")
            return FinanceWorkflowOutput(
                status=WorkflowStatus.FAILED,
                error_message=str(e),
                workflow_type=input_data.workflow_type
            )
    
    def execute_investment_advisory_workflow(self, input_data: FinanceWorkflowInput) -> FinanceWorkflowOutput:
        try:
            self.logger.info(f"[START] investment_advisory workflow for user: {input_data.user_id}, org: {input_data.organization_id}")
            
            prompt = f"""
            You are an Investment Advisor. Analyze this investment data:
            {input_data.investment_data}
            
            Provide:
            1. Portfolio performance analysis
            2. Risk-return assessment
            3. Asset allocation recommendations
            4. Investment opportunities
            """
            
            result = self.llm.invoke(prompt)
            
            return FinanceWorkflowOutput(
                status=WorkflowStatus.SUCCESS,
                results=result.content,
                workflow_type=input_data.workflow_type,
                recommendations={"investment_opportunities": [result.content]}
            )
        except Exception as e:
            self.logger.error(f"[ERROR] Investment advisory workflow failed: {str(e)}")
            return FinanceWorkflowOutput(
                status=WorkflowStatus.FAILED,
                error_message=str(e),
                workflow_type=input_data.workflow_type
            )
    
    def _extract_recommendations(self, content: str) -> dict:
        return {
            "financial_insights": [content],
            "risk_mitigation": [],
            "budget_optimization": [],
            "investment_opportunities": [],
            "compliance_actions": []
        }