# Smart Invoice & Receipt Processor 🧾

## 🎯 Project Overview

An enterprise-grade AI agent that automates invoice processing, expense categorization, and anomaly detection for small businesses and freelancers. Built using Google ADK 2.0 with a multi-layer security architecture.

**Track:** Agents for Business  
**Course:** 5-Day AI Agents: Intensive Vibe Coding Course With Google

---

## 💡 Problem Statement

Small businesses and freelancers spend **hours manually processing invoices**, categorizing expenses, and preparing tax reports. This leads to:
- ❌ Human errors in data entry
- ❌ Missed policy violations (e.g., weekend transactions, high-value expenses)
- ❌ Security vulnerabilities (prompt injection attacks)
- ❌ Time wasted on repetitive tasks

---

## 🚀 Solution

The **Smart Invoice Processor** is an AI-powered agent that:
1. **Validates** incoming invoice data using Pydantic schemas
2. **Detects** prompt injection attacks using regex-based security scanning
3. **Classifies** expenses automatically based on vendor and description
4. **Flags** anomalies (high-value transactions, weekend spending)
5. **Routes** suspicious invoices for Human-in-the-Loop (HITL) review

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────┐
│         FastAPI Server (8080)           │
│         POST /process                   │
└────────────────┬────────────────────────┘
                 │
                 ▼
        ┌────────┴────────┐
        │  Security Layer │ ← Prompt Injection Detection
        └────────┬────────┘
                 │
        ┌────────┴────────┐
        │  Orchestrator   │ ← Main Agent (ADK)
        └────────┬────────┘
                 │
        ┌────────┼────────┬────────┐
        │        │        │        │
        ▼        ▼        ▼        ▼
   extractor  classifier analyzer  reporter
   (validate) (categorize) (anomaly) (PDF)
```

### 🧩 Components:

1. **FastAPI Server**: REST API endpoint for invoice processing
2. **Security Layer**: Regex-based prompt injection detection
3. **Orchestrator**: Main ADK agent coordinating specialized tools
4. **Extractor Tool**: Data validation and parsing
5. **Classifier Tool**: Expense categorization
6. **Analyzer Tool**: Anomaly detection (high-value, weekend transactions)
7. **Reporter Tool**: PDF report generation

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Google ADK 2.0** | Agent orchestration |
| **FastAPI** | REST API server |
| **Pydantic** | Data validation |
| **Pytest** | Automated testing |
| **MCP** | Model Context Protocol server |
| **Gherkin BDD** | Behavior-driven specifications |
| **Antigravity** | AI-powered development environment for building and testing agents |

---

## 📦 Installation

### Prerequisites
- Python 3.10+
- Anaconda or Miniconda

### Setup Steps

1. **Clone the repository**
```bash
git clone https://github.com/JALILOHUB/smart-invoice-processor.git
cd smart-invoice-processor
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure environment variables**
Create a `.env` file:
```env
GOOGLE_API_KEY=your_api_key_here
GOOGLE_GENAI_USE_VERTEXAI=FALSE
```

---

## ▶️ How to Run

### Start the API Server
```bash
set PYTHONPATH=. && uvicorn app.server:app --reload --port 8080
```

### Test the Health Endpoint
```bash
curl http://localhost:8080/health
```

### Process an Invoice
```bash
curl -X POST http://localhost:8080/process \
  -H "Content-Type: application/json" \
  -d '{
    "invoice_number": "INV-001",
    "vendor": "Office Supplies Co",
    "amount": 50.00,
    "currency": "USD",
    "date": "2026-06-18T10:00:00",
    "category": "office_supplies",
    "description": "Monthly office supplies",
    "submitter": "user@company.com"
  }'
```

---

## 🧪 Testing

### Run Security Tests
```bash
set PYTHONPATH=. && pytest tests/test_security.py -v
```

**Expected Output:**
```
tests/test_security.py::TestPromptInjectionDefense::test_detects_ignore_rules PASSED
tests/test_security.py::TestPromptInjectionDefense::test_detects_sql_injection PASSED
tests/test_security.py::TestPromptInjectionDefense::test_detects_roleplay_jailbreak PASSED
tests/test_security.py::TestPromptInjectionDefense::test_allows_normal_text PASSED
tests/test_security.py::TestPromptInjectionDefense::test_handles_empty_input PASSED

============================== 5 passed ==============================
```

---

## 🔐 Security Features

### 1. Prompt Injection Defense
The agent uses regex-based pattern matching to detect malicious inputs:
```python
INJECTION_PATTERNS = [
    r"ignore\s+(all\s+)?rules",
    r"bypass\s+(all\s+)?rules",
    r"approve\s+immediately",
    r"drop\s+table",
]
```

### 2. Pydantic Validation
All inputs are validated at the schema level:
- Amount must be > 0 and ≤ 1,000,000
- Submitter must be a valid email format
- Date must be a valid datetime object

### 3. Anomaly Detection
Business rules are enforced:
- High-value transactions (> $5,000) are flagged
- Weekend transactions trigger alerts
- Category mismatches are detected

---

## 📚 Course Concepts Applied

This project demonstrates mastery of the following concepts from the 5-Day AI Agents course:

| Concept | Implementation |
|---|---|
| **Agent / Multi-agent (ADK)** | Orchestrator agent coordinates specialized tools |
| **MCP Server** | Invoice knowledge base exposed via MCP |
| **Security Features** | Prompt injection detection, Pydantic validation, HITL routing |
| **Agent Skills** | `.agents/skills/invoice-processing/SKILL.md` defines SOP |
| **Spec-Driven Development** | Gherkin BDD specs in `specs/invoice_processing.feature` |
| **Outcome-Based Testing** | 5 security tests assert on results, not interactions |

---

## 📂 Project Structure

```
capstone-project/
├── .agents/
│   └── skills/
│       └── invoice-processing/
│           └── SKILL.md
├── app/
│   ├── __init__.py
│   ├── agent.py              # Main orchestrator agent
│   ├── schemas.py            # Pydantic models
│   ├── server.py             # FastAPI endpoints
│   ├── security.py           # Prompt injection detection
│   ├── mcp_server.py         # MCP server for invoice DB
│   └── tools/
│       ├── extractor.py      # Data validation
│       ├── classifier.py     # Expense categorization
│       └── analyzer.py       # Anomaly detection
├── specs/
│   └── invoice_processing.feature  # Gherkin BDD specs
├── tests/
│   └── test_security.py      # Security test suite
├── .env                      # Environment variables
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🎓 Lessons Learned

1. **Shift Left Security**: Security must be enforced at code-writing time, not post-deployment
2. **Defense in Depth**: Multiple layers (Pydantic + Regex + HITL) prevent single points of failure
3. **Outcome-Based Testing**: Assert on results, not internal interactions
4. **Spec-Driven Development**: Gherkin BDD specs keep agents on strict behavioral tracks

---

## 📄 License

This project was built as part of the **5-Day AI Agents: Intensive Vibe Coding Course With Google** capstone project.

---

## 👨‍💻 Author

**ABDELJALIL EL KHYATI**  
Kaggle Participant | AI Agent Developer 🚀
