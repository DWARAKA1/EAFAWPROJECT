# Enterprise Agentic Finance Automation Workflow (EAFAW)

A comprehensive AI-powered finance automation system built with CrewAI, featuring intelligent agents for financial analysis, risk management, budget control, investment advisory, and compliance monitoring.

## 🏗️ Architecture Overview

```
EAFAWPROJECT/
├── src/
│   ├── agents/           # AI Agents (Financial Analyst, Risk Manager, etc.)
│   ├── tasks/            # Task definitions for each workflow
│   ├── crews/            # Crew orchestration and management
│   ├── tools/            # Custom tools for financial operations
│   ├── workflows/        # Main workflow orchestrators
│   ├── models/           # Pydantic data models
│   ├── api/              # FastAPI REST endpoints
│   ├── frontend/         # Streamlit web interface
│   ├── database/         # Database models and connections
│   └── main.py           # Application entry point
├── requirements.txt      # Python dependencies
├── setup.py             # Package setup
└── .env                 # Environment variables
```

## 🤖 AI Agents

### 1. Financial Analyst Agent
- **Role**: Senior Financial Analyst
- **Capabilities**: Revenue analysis, profitability assessment, KPI calculation
- **Tools**: Financial data retrieval, ratio analysis, trend identification

### 2. Risk Manager Agent
- **Role**: Risk Management Specialist
- **Capabilities**: Risk assessment, VaR calculation, portfolio analysis
- **Tools**: Risk calculator, volatility analysis, correlation matrices

### 3. Budget Controller Agent
- **Role**: Budget Controller
- **Capabilities**: Budget monitoring, variance analysis, expense tracking
- **Tools**: Budget analyzer, forecast accuracy, cost optimization

### 4. Investment Advisor Agent
- **Role**: Investment Advisor
- **Capabilities**: Portfolio optimization, asset allocation, investment recommendations
- **Tools**: Market data analysis, performance evaluation, risk-return optimization

### 5. Compliance Officer Agent
- **Role**: Compliance Officer
- **Capabilities**: Regulatory compliance, audit trail verification, policy adherence
- **Tools**: Compliance checker, documentation validator, risk control assessment

## 🔄 Workflow Types

### 1. Financial Analysis Workflow
- Comprehensive financial health assessment
- Revenue and profitability analysis
- Liquidity and solvency evaluation
- Performance benchmarking

### 2. Budget Management Workflow
- Budget vs actual variance analysis
- Expense categorization and tracking
- Forecast accuracy assessment
- Cost optimization recommendations

### 3. Investment Advisory Workflow
- Portfolio performance evaluation
- Risk-adjusted return analysis
- Asset allocation optimization
- Investment opportunity identification

### 4. Comprehensive Workflow
- Integrated analysis across all financial domains
- Cross-functional insights and recommendations
- Holistic risk assessment
- Strategic financial planning

## 🛠️ Custom Tools

### Financial Data Tool
- Real-time market data retrieval
- Company financial information
- Historical price analysis
- Market indicators and ratios

### Risk Calculator Tool
- Value at Risk (VaR) calculation
- Volatility and correlation analysis
- Sharpe ratio computation
- Maximum drawdown assessment

### Budget Analyzer Tool
- Variance analysis and reporting
- Trend identification
- Forecast accuracy metrics
- Budget optimization suggestions

### Compliance Checker Tool
- Regulatory requirement validation
- Policy adherence verification
- Audit trail completeness
- Risk control effectiveness

## 🚀 Quick Start

### 1. Installation
```bash
# Clone the repository
git clone <repository-url>
cd EAFAWPROJECT

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys
```

### 2. Environment Setup
```bash
# Required environment variables
GROQ_API_KEY=your_groq_api_key_here
CREW_API_KEY=your_crew_api_key_here
```

### 3. Run the Application

#### Option A: Command Line Interface
```bash
python src/main.py
```

#### Option B: API Server
```bash
# Start FastAPI server
python -m src.api.finance_api

# API will be available at http://localhost:8000
# Interactive docs at http://localhost:8000/docs
```

#### Option C: Web Interface
```bash
# Start Streamlit app
streamlit run src/frontend/streamlit_app.py

# Web app will be available at http://localhost:8501
```

## 📡 API Endpoints

### Workflow Execution
- `POST /api/v1/workflows/financial-analysis` - Execute financial analysis
- `POST /api/v1/workflows/budget-management` - Execute budget management
- `POST /api/v1/workflows/investment-advisory` - Execute investment advisory
- `POST /api/v1/workflows/comprehensive` - Execute comprehensive analysis

### Workflow Management
- `GET /api/v1/workflows/{workflow_id}/status` - Get workflow status
- `GET /api/v1/workflows/{workflow_id}/results` - Get workflow results
- `GET /api/v1/health` - Health check

## 📊 Usage Examples

### Financial Analysis
```python
from src.workflows.finance_workflow import FinanceWorkflow
from src.models.finance_models import FinanceWorkflowInput, WorkflowType

# Initialize workflow
workflow = FinanceWorkflow()

# Prepare input data
input_data = FinanceWorkflowInput(
    workflow_type=WorkflowType.FINANCIAL_ANALYSIS,
    financial_data={
        "revenue": 1000000,
        "expenses": 800000,
        "assets": 2000000,
        "liabilities": 500000
    },
    user_id="user123",
    organization_id="org456"
)

# Execute workflow
result = workflow.execute_financial_analysis_workflow(input_data)
print(f"Status: {result.status}")
print(f"Recommendations: {result.recommendations}")
```

### API Usage
```bash
# Execute financial analysis via API
curl -X POST "http://localhost:8000/api/v1/workflows/financial-analysis" \
  -H "Content-Type: application/json" \
  -d '{
    "workflow_type": "FINANCIAL_ANALYSIS",
    "financial_data": {
      "revenue": 1000000,
      "expenses": 800000
    },
    "user_id": "user123",
    "organization_id": "org456"
  }'

# Check workflow status
curl "http://localhost:8000/api/v1/workflows/{workflow_id}/status"

# Get results
curl "http://localhost:8000/api/v1/workflows/{workflow_id}/results"
```

## 🔧 Configuration

### Agent Configuration
Agents can be customized in `src/agents/finance_agents.py`:
- Model selection (Groq, OpenAI, etc.)
- Temperature and creativity settings
- Role and backstory customization
- Tool assignment and permissions

### Workflow Configuration
Workflows can be modified in `src/workflows/finance_workflow.py`:
- Task sequencing and dependencies
- Error handling and retry logic
- Result processing and formatting
- Performance monitoring

## 📈 Monitoring and Logging

The system includes comprehensive logging and monitoring:
- Workflow execution tracking
- Performance metrics collection
- Error logging and alerting
- Agent interaction monitoring

## 🔒 Security and Compliance

- API key management and rotation
- Data encryption in transit and at rest
- Audit trail maintenance
- Regulatory compliance validation
- Access control and authentication

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- Create an issue in the repository
- Check the documentation
- Review the API documentation at `/docs`

## 🚀 Future Enhancements

- Real-time data streaming integration
- Advanced ML model integration
- Multi-tenant architecture
- Mobile application support
- Advanced visualization dashboards
- Integration with external financial systems