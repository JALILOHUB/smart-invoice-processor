import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools import FunctionTool

# Import the specialized tools we created in Step 3
from .tools.extractor import process_invoice_data
from .tools.classifier import auto_classify_expense
from .tools.analyzer import detect_anomalies

# Load environment variables from .env file
load_dotenv()

# Wrap Python functions into ADK FunctionTools
extractor_tool = FunctionTool(func=process_invoice_data)
classifier_tool = FunctionTool(func=auto_classify_expense)
analyzer_tool = FunctionTool(func=detect_anomalies)

# Define the Main Orchestrator Agent
# This agent acts as the "Brain" that coordinates the specialized tools
root_agent = Agent(
    name="invoice_orchestrator",
    model="gemini-2.0-flash",
    instruction="""You are the Smart Invoice Orchestrator, an enterprise-grade AI agent designed to process incoming invoice data securely and efficiently.

    Your Standard Operating Procedure (SOP):
    1. EXTRACTION: First, use the 'process_invoice_data' tool to parse, validate, and structure the raw invoice input.
    2. CLASSIFICATION: Second, use the 'auto_classify_expense' tool to verify if the assigned expense category matches the vendor and description.
    3. ANOMALY DETECTION: Third, use the 'detect_anomalies' tool to check for policy violations (e.g., high-value transactions or weekend spending).
    4. REPORTING: Finally, synthesize the results into a clear, professional executive summary. 

    Security Rules:
    - If anomalies are detected, explicitly flag the invoice for "Human-in-the-Loop (HITL) Review".
    - Never expose raw sensitive PII (like full credit card numbers) in your final summary.
    - Always respond in professional business English.
    """,
    tools=[extractor_tool, classifier_tool, analyzer_tool],
)