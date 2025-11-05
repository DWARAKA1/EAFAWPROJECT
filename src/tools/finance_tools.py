from crewai.tools import tool
import pandas as pd
import yfinance as yf
import numpy as np
from typing import Dict, List, Any
import requests

@tool
def financial_data_tool(symbol: str, period: str = "1y") -> Dict[str, Any]:
    """Retrieves financial data from various sources including stock prices, company financials, and market data"""
    try:
        ticker = yf.Ticker(symbol)
        hist = ticker.history(period=period)
        info = ticker.info
        
        return {
            "symbol": symbol,
            "current_price": hist['Close'].iloc[-1],
            "price_change": hist['Close'].iloc[-1] - hist['Close'].iloc[-2],
            "volume": hist['Volume'].iloc[-1],
            "market_cap": info.get('marketCap', 'N/A'),
            "pe_ratio": info.get('trailingPE', 'N/A'),
            "dividend_yield": info.get('dividendYield', 'N/A'),
            "historical_data": hist.to_dict()
        }
    except Exception as e:
        return {"error": f"Failed to retrieve data for {symbol}: {str(e)}"}

@tool
def risk_calculator_tool(returns_data: List[float], confidence_level: float = 0.95) -> Dict[str, float]:
    """Calculates various risk metrics including VaR, volatility, and correlation analysis"""
    try:
        returns = np.array(returns_data)
        
        # Calculate risk metrics
        volatility = np.std(returns) * np.sqrt(252)  # Annualized volatility
        var_95 = np.percentile(returns, (1 - confidence_level) * 100)
        sharpe_ratio = np.mean(returns) / np.std(returns) * np.sqrt(252)
        max_drawdown = _calculate_max_drawdown(returns)
        
        return {
            "volatility": volatility,
            "value_at_risk": var_95,
            "sharpe_ratio": sharpe_ratio,
            "max_drawdown": max_drawdown,
            "mean_return": np.mean(returns),
            "std_deviation": np.std(returns)
        }
    except Exception as e:
        return {"error": f"Risk calculation failed: {str(e)}"}

def _calculate_max_drawdown(returns: np.ndarray) -> float:
    cumulative = np.cumprod(1 + returns)
    running_max = np.maximum.accumulate(cumulative)
    drawdown = (cumulative - running_max) / running_max
    return np.min(drawdown)

@tool
def budget_analyzer_tool(budget_data: Dict[str, Any]) -> Dict[str, Any]:
    """Analyzes budget data and calculates variances, trends, and forecasts"""
    try:
        actual = budget_data.get('actual', [])
        budgeted = budget_data.get('budgeted', [])
        
        if len(actual) != len(budgeted):
            return {"error": "Actual and budgeted data must have same length"}
        
        variance = [a - b for a, b in zip(actual, budgeted)]
        variance_pct = [(a - b) / b * 100 if b != 0 else 0 for a, b in zip(actual, budgeted)]
        
        return {
            "total_actual": sum(actual),
            "total_budgeted": sum(budgeted),
            "total_variance": sum(variance),
            "variance_percentage": sum(variance) / sum(budgeted) * 100 if sum(budgeted) != 0 else 0,
            "monthly_variances": variance,
            "monthly_variance_percentages": variance_pct,
            "over_budget_months": len([v for v in variance if v > 0]),
            "under_budget_months": len([v for v in variance if v < 0])
        }
    except Exception as e:
        return {"error": f"Budget analysis failed: {str(e)}"}

@tool
def compliance_checker_tool(transaction_data: Dict[str, Any]) -> Dict[str, Any]:
    """Checks financial processes and transactions for regulatory compliance"""
    try:
        compliance_score = 100
        issues = []
        
        # Check for required fields
        required_fields = ['amount', 'date', 'description', 'approver']
        for field in required_fields:
            if field not in transaction_data:
                compliance_score -= 20
                issues.append(f"Missing required field: {field}")
        
        # Check amount limits
        amount = transaction_data.get('amount', 0)
        if amount > 10000 and 'secondary_approver' not in transaction_data:
            compliance_score -= 15
            issues.append("Transactions over $10,000 require secondary approval")
        
        # Check documentation
        if amount > 5000 and 'supporting_documents' not in transaction_data:
            compliance_score -= 10
            issues.append("Transactions over $5,000 require supporting documentation")
        
        return {
            "compliance_score": max(0, compliance_score),
            "status": "COMPLIANT" if compliance_score >= 80 else "NON_COMPLIANT",
            "issues": issues,
            "recommendations": _get_recommendations(issues)
        }
    except Exception as e:
        return {"error": f"Compliance check failed: {str(e)}"}

def _get_recommendations(issues: List[str]) -> List[str]:
    recommendations = []
    for issue in issues:
        if "Missing required field" in issue:
            recommendations.append("Ensure all required fields are completed before submission")
        elif "secondary approval" in issue:
            recommendations.append("Obtain secondary approver signature for high-value transactions")
        elif "supporting documentation" in issue:
            recommendations.append("Attach relevant supporting documents (receipts, invoices, contracts)")
    return recommendations