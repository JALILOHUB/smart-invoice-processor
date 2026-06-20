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

┌─────────────────────────────────────────┐
│ FastAPI Server (8080) │
│ POST /process │
└────────────────────────────────────────┘
│
▼
┌────────┴────────┐
│ Security Layer │ ← Prompt Injection Detection
└────────┬────────┘
│
┌────────┴────────┐
│ Orchestrator │ ← Main Agent (ADK)
└────────┬────────┘
│
┌────────┼────────┬────────┐
│ │ │ │
▼ ▼ ▼ ▼
extractor classifier analyzer reporter
(validate) (categorize) (anomaly) (PDF)


### Components:

1. **FastAPI Server**: REST API endpoint for invoice processing
2. **Security Layer**: Regex-based prompt injection detection
3. **Orchestrator**: Main ADK agent coordinating specialized tools
4. **Extractor Tool**: Data validation and parsing
5. **Classifier Tool**: Expense categorization
6. **Analyzer Tool**: Anomaly detection (high-value, weekend transactions)
7. **Reporter Tool**: PDF report generation
