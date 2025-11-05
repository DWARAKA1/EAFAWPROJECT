import streamlit as st
import requests
import pandas as pd
import time

# Configure Streamlit page
st.set_page_config(
    page_title="Enterprise Finance Workflow Automation",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# API Configuration
API_BASE_URL = "http://localhost:8000/api/v1"

def main():
    st.title("🏢 Enterprise Agentic Finance Automation Workflow")
    st.markdown("---")
    
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox(
        "Choose a workflow",
        ["Dashboard", "Financial Analysis", "Budget Management", "Investment Advisory", "Comprehensive Analysis"]
    )
    
    if page == "Dashboard":
        show_dashboard()
    elif page == "Financial Analysis":
        show_financial_analysis()
    elif page == "Budget Management":
        show_budget_management()
    elif page == "Investment Advisory":
        show_investment_advisory()
    elif page == "Comprehensive Analysis":
        show_comprehensive_analysis()

def show_dashboard():
    st.header("📊 Finance Automation Dashboard")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Active Workflows", "12", "↑ 3")
    with col2:
        st.metric("Completed Today", "8", "↑ 2")
    with col3:
        st.metric("Success Rate", "94%", "↑ 1%")
    with col4:
        st.metric("Avg Processing Time", "2.3 min", "↓ 0.5 min")
    
    # Recent workflows
    st.subheader("Recent Workflow Executions")
    sample_data = {
        "Workflow ID": ["WF001", "WF002", "WF003", "WF004"],
        "Type": ["Financial Analysis", "Budget Management", "Investment Advisory", "Comprehensive"],
        "Status": ["Completed", "Running", "Completed", "Failed"],
        "Started": ["10:30 AM", "10:45 AM", "11:00 AM", "11:15 AM"],
        "Duration": ["2.1 min", "Running...", "3.2 min", "Error"]
    }
    st.dataframe(pd.DataFrame(sample_data), width='stretch')

def show_financial_analysis():
    st.header("📈 Financial Analysis Workflow")
    
    with st.form("financial_analysis_form"):
        st.subheader("Input Financial Data")
        
        col1, col2 = st.columns(2)
        
        with col1:
            company_symbol = st.text_input("Company Symbol", "AAPL")
            revenue = st.number_input("Annual Revenue ($M)", value=100000)
            profit_margin = st.number_input("Profit Margin (%)", value=25.0)
            
        with col2:
            debt_equity = st.number_input("Debt-to-Equity Ratio", value=0.5)
            current_ratio = st.number_input("Current Ratio", value=1.2)
            cash_flow = st.number_input("Operating Cash Flow ($M)", value=25000)
        
        user_id = st.text_input("User ID", "user123")
        org_id = st.text_input("Organization ID", "org456")
        
        submitted = st.form_submit_button("Execute Financial Analysis")
        
        if submitted:
            financial_data = {
                "company_symbol": company_symbol,
                "revenue": revenue,
                "profit_margin": profit_margin,
                "debt_equity_ratio": debt_equity,
                "current_ratio": current_ratio,
                "cash_flow": cash_flow
            }
            
            payload = {
                "workflow_type": "FINANCIAL_ANALYSIS",
                "financial_data": financial_data,
                "user_id": user_id,
                "organization_id": org_id
            }
            
            execute_workflow("financial-analysis", payload)

def show_budget_management():
    st.header("💼 Budget Management Workflow")
    
    with st.form("budget_management_form"):
        st.subheader("Budget Data Input")
        
        # Budget categories
        departments = ["Marketing", "Sales", "IT", "HR", "Operations"]
        
        budget_data = {}
        for dept in departments:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write(f"**{dept}**")
            with col2:
                budgeted = st.number_input(f"Budgeted ({dept})", value=50000, key=f"budget_{dept}")
            with col3:
                actual = st.number_input(f"Actual ({dept})", value=45000, key=f"actual_{dept}")
            
            budget_data[dept] = {"budgeted": budgeted, "actual": actual}
        
        user_id = st.text_input("User ID", "user123", key="budget_user")
        org_id = st.text_input("Organization ID", "org456", key="budget_org")
        
        submitted = st.form_submit_button("Execute Budget Analysis")
        
        if submitted:
            payload = {
                "workflow_type": "BUDGET_MANAGEMENT",
                "budget_data": budget_data,
                "user_id": user_id,
                "organization_id": org_id
            }
            
            execute_workflow("budget-management", payload)

def show_investment_advisory():
    st.header("📊 Investment Advisory Workflow")
    
    with st.form("investment_advisory_form"):
        st.subheader("Investment Portfolio Data")
        
        # Portfolio allocation
        col1, col2 = st.columns(2)
        
        with col1:
            stocks_allocation = st.slider("Stocks (%)", 0, 100, 60)
            bonds_allocation = st.slider("Bonds (%)", 0, 100, 30)
            
        with col2:
            commodities_allocation = st.slider("Commodities (%)", 0, 100, 5)
            cash_allocation = st.slider("Cash (%)", 0, 100, 5)
        
        risk_tolerance = st.selectbox("Risk Tolerance", ["Conservative", "Moderate", "Aggressive"])
        investment_horizon = st.selectbox("Investment Horizon", ["Short-term (1-3 years)", "Medium-term (3-7 years)", "Long-term (7+ years)"])
        
        portfolio_value = st.number_input("Total Portfolio Value ($)", value=1000000)
        
        user_id = st.text_input("User ID", "user123", key="invest_user")
        org_id = st.text_input("Organization ID", "org456", key="invest_org")
        
        submitted = st.form_submit_button("Execute Investment Analysis")
        
        if submitted:
            investment_data = {
                "portfolio_allocation": {
                    "stocks": stocks_allocation,
                    "bonds": bonds_allocation,
                    "commodities": commodities_allocation,
                    "cash": cash_allocation
                },
                "risk_tolerance": risk_tolerance,
                "investment_horizon": investment_horizon,
                "portfolio_value": portfolio_value
            }
            
            payload = {
                "workflow_type": "INVESTMENT_ADVISORY",
                "investment_data": investment_data,
                "user_id": user_id,
                "organization_id": org_id
            }
            
            execute_workflow("investment-advisory", payload)

def show_comprehensive_analysis():
    st.header("🔄 Comprehensive Finance Analysis")
    st.info("This workflow combines financial analysis, budget management, and investment advisory into a single comprehensive report.")
    
    with st.form("comprehensive_form"):
        st.subheader("Complete Financial Data")
        
        # Simplified inputs for comprehensive analysis
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.write("**Financial Metrics**")
            revenue = st.number_input("Revenue ($M)", value=100000, key="comp_revenue")
            profit_margin = st.number_input("Profit Margin (%)", value=25.0, key="comp_margin")
            
        with col2:
            st.write("**Budget Summary**")
            total_budget = st.number_input("Total Budget ($M)", value=50, key="comp_budget")
            actual_spend = st.number_input("Actual Spend ($M)", value=48, key="comp_spend")
            
        with col3:
            st.write("**Investment Portfolio**")
            portfolio_value = st.number_input("Portfolio Value ($M)", value=10, key="comp_portfolio")
            target_return = st.number_input("Target Return (%)", value=8.0, key="comp_return")
        
        user_id = st.text_input("User ID", "user123", key="comp_user")
        org_id = st.text_input("Organization ID", "org456", key="comp_org")
        
        submitted = st.form_submit_button("Execute Comprehensive Analysis")
        
        if submitted:
            payload = {
                "workflow_type": "COMPREHENSIVE",
                "financial_data": {"revenue": revenue, "profit_margin": profit_margin},
                "budget_data": {"total_budget": total_budget, "actual_spend": actual_spend},
                "investment_data": {"portfolio_value": portfolio_value, "target_return": target_return},
                "user_id": user_id,
                "organization_id": org_id
            }
            
            execute_workflow("comprehensive", payload)

def execute_workflow(endpoint, payload):
    """Execute workflow and show results"""
    try:
        with st.spinner("Executing workflow..."):
            response = requests.post(f"{API_BASE_URL}/workflows/{endpoint}", json=payload)
            
            if response.status_code == 200:
                result = response.json()
                workflow_id = result.get("workflow_id")
                
                st.success(f"Workflow started successfully! ID: {workflow_id}")
                
                # Poll for results
                progress_bar = st.progress(0)
                status_placeholder = st.empty()
                
                for i in range(10):  # Poll for 10 iterations
                    time.sleep(2)  # Wait 2 seconds between polls
                    
                    status_response = requests.get(f"{API_BASE_URL}/workflows/{workflow_id}/status")
                    if status_response.status_code == 200:
                        status_data = status_response.json()
                        current_status = status_data.get("status")
                        
                        progress_bar.progress((i + 1) * 10)
                        status_placeholder.info(f"Status: {current_status}")
                        
                        if current_status == "SUCCESS":
                            st.success("Workflow completed successfully!")
                            
                            # Get results
                            results_response = requests.get(f"{API_BASE_URL}/workflows/{workflow_id}/results")
                            if results_response.status_code == 200:
                                results_data = results_response.json()
                                display_results(results_data)
                            break
                        elif current_status == "FAILED":
                            st.error("Workflow failed!")
                            break
                
            else:
                st.error(f"Failed to start workflow: {response.text}")
                
    except Exception as e:
        st.error(f"Error executing workflow: {str(e)}")

def display_results(results_data):
    """Display workflow results"""
    st.subheader("📋 Workflow Results")
    
    if "recommendations" in results_data:
        recommendations = results_data["recommendations"]
        
        for category, items in recommendations.items():
            if items:
                st.write(f"**{category.replace('_', ' ').title()}:**")
                for item in items:
                    st.write(f"• {item}")
                st.write("")
    
    # Display raw results in expandable section
    with st.expander("View Raw Results"):
        st.json(results_data)

if __name__ == "__main__":
    main()