from crewai import Agent
from langchain_groq import ChatGroq
import os

class InvoiceAgents:
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0,
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name="mixtral-8x7b-32768"
        )

    def invoice_ingestion_agent(self):
        return Agent(
            role='Invoice Ingestion Specialist',
            goal='Extract and structure data from invoice documents accurately',
            backstory="""You are an expert in document processing and data extraction, 
            specializing in financial documents. You have extensive experience with OCR 
            technologies and data validation.""",
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )

    def validation_agent(self):
        return Agent(
            role='Invoice Validation Specialist',
            goal='Validate invoice data against ERP records and company policies',
            backstory="""You are a meticulous validation specialist with deep knowledge 
            of accounting principles and ERP systems. You ensure all invoice data matches 
            purchase orders and vendor records.""",
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )

    def approval_routing_agent(self):
        return Agent(
            role='Approval Workflow Manager',
            goal='Route invoices to appropriate approvers and track approval status',
            backstory="""You manage the approval workflow process, ensuring invoices 
            are routed to the correct approvers based on amount, department, and 
            company policies.""",
            verbose=True,
            allow_delegation=True,  # Allows delegation to human approvers
            llm=self.llm
        )

    def payment_agent(self):
        return Agent(
            role='Payment Processing Specialist',
            goal='Execute approved payments and maintain payment records',
            backstory="""You handle the payment execution process, ensuring accurate 
            and timely payments while maintaining proper financial records and audit 
            trails.""",
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )

    def compliance_agent(self):
        return Agent(
            role='Compliance Officer',
            goal='Ensure all invoice processing complies with policies and regulations',
            backstory="""You oversee regulatory compliance and policy adherence 
            throughout the invoice processing workflow, maintaining audit trails and 
            ensuring SOX compliance.""",
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )