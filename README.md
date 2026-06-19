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
