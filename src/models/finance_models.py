from pydantic import BaseModel, Field
from typing import Dict, List, Any, Optional
from datetime import datetime
from enum import Enum

class WorkflowType(str, Enum):
    FINANCIAL_ANALYSIS = "FINANCIAL_ANALYSIS"
    BUDGET_MANAGEMENT = "BUDGET_MANAGEMENT"
    INVESTMENT_ADVISORY = "INVESTMENT_ADVISORY"
    COMPREHENSIVE = "COMPREHENSIVE"

class WorkflowStatus(str, Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"

class FinanceWorkflowInput(BaseModel):
    """Input model for finance workflow requests"""
    workflow_type: WorkflowType
    financial_data: Optional[Dict[str, Any]] = None
    budget_data: Optional[Dict[str, Any]] = None
    investment_data: Optional[Dict[str, Any]] = None
    user_id: str
    organization_id: str
    priority: int = Field(default=1, ge=1, le=5)
    metadata: Optional[Dict[str, Any]] = None

class FinanceWorkflowOutput(BaseModel):
    """Output model for finance workflow results"""
    workflow_id: Optional[str] = None
    status: WorkflowStatus
    workflow_type: WorkflowType
    results: Optional[Any] = None
    recommendations: Optional[Dict[str, Any]] = None
    error_message: Optional[str] = None
    execution_time: Optional[float] = None
    created_at: datetime = Field(default_factory=datetime.now)
    completed_at: Optional[datetime] = None

class FinancialMetrics(BaseModel):
    """Model for financial metrics and KPIs"""
    revenue: Optional[float] = None
    profit_margin: Optional[float] = None
    roi: Optional[float] = None
    debt_to_equity: Optional[float] = None
    current_ratio: Optional[float] = None
    quick_ratio: Optional[float] = None
    cash_flow: Optional[float] = None
    ebitda: Optional[float] = None

class RiskMetrics(BaseModel):
    """Model for risk assessment metrics"""
    value_at_risk: Optional[float] = None
    volatility: Optional[float] = None
    sharpe_ratio: Optional[float] = None
    max_drawdown: Optional[float] = None
    beta: Optional[float] = None
    correlation_matrix: Optional[Dict[str, Dict[str, float]]] = None

class BudgetData(BaseModel):
    """Model for budget information"""
    department: str
    category: str
    budgeted_amount: float
    actual_amount: float
    period: str
    variance: Optional[float] = None
    variance_percentage: Optional[float] = None

class InvestmentData(BaseModel):
    """Model for investment information"""
    asset_class: str
    symbol: str
    quantity: float
    current_price: float
    purchase_price: float
    market_value: float
    unrealized_gain_loss: Optional[float] = None
    allocation_percentage: Optional[float] = None

class ComplianceCheck(BaseModel):
    """Model for compliance verification"""
    rule_id: str
    rule_description: str
    status: str  # COMPLIANT, NON_COMPLIANT, WARNING
    severity: str  # LOW, MEDIUM, HIGH, CRITICAL
    details: Optional[str] = None
    remediation_steps: Optional[List[str]] = None

class WorkflowExecution(BaseModel):
    """Model for tracking workflow execution"""
    workflow_id: str
    user_id: str
    organization_id: str
    workflow_type: WorkflowType
    status: WorkflowStatus
    input_data: FinanceWorkflowInput
    output_data: Optional[FinanceWorkflowOutput] = None
    started_at: datetime
    completed_at: Optional[datetime] = None
    error_details: Optional[str] = None