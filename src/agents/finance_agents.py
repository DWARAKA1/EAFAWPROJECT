# USAGE NOTE:
# Run this file from the project root using:
#   python -m src.agents.finance_agents
# This ensures all imports work correctly in a modular Python project.

import os
from dotenv import load_dotenv
from crewai import Agent
from langchain_groq import ChatGroq
from src.common.logger import get_logger
from src.common.custom_exception import CustomException

class FinanceAgents:
    def __init__(self):
        self.logger = get_logger(__name__)
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            self.logger.error("GROQ_API_KEY environment variable not set")
            raise CustomException("GROQ_API_KEY environment variable not set")
        self.llm = ChatGroq(
            temperature=0,
            groq_api_key=api_key,
            model_name="llama-3.1-8b-instant"
        )
        self.logger.info("FinanceAgents initialized with Groq LLM.")

    def financial_analyst_agent(self):
        self.logger.info("Creating Senior Financial Analyst agent.")
        return Agent(
            role='Senior Financial Analyst',
            goal='Analyze financial data and provide insights for decision making',
            backstory="Senior financial analyst with 15+ years experience in corporate finance and financial modeling.",
            verbose=False,
            allow_delegation=False,
            llm=self.llm
        )

    def risk_manager_agent(self):
        self.logger.info("Creating Risk Management Specialist agent.")
        return Agent(
            role='Risk Management Specialist',
            goal='Identify, assess, and mitigate financial risks across the organization',
            backstory="Expert risk manager with deep knowledge of financial markets and regulatory compliance.",
            verbose=False,
            allow_delegation=False,
            llm=self.llm
        )

def main():
    load_dotenv()
    try:
        agents = FinanceAgents()
        analyst = agents.financial_analyst_agent()
        risk_mgr = agents.risk_manager_agent()
        agents.logger.info("Finance agents created successfully.")
        print("Finance agents initialized.")
    except CustomException as e:
        logger = get_logger(__name__)
        logger.exception(f"CustomException occurred: {str(e)}")
    except Exception as e:
        logger = get_logger(__name__)
        logger.exception(f"Unhandled exception: {str(e)}")

if __name__ == "__main__":
    main()