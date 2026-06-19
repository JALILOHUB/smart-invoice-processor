from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import datetime
from enum import Enum

class ExpenseCategory(str, Enum):
    MEALS = "meals"
    TRAVEL = "travel"
    EQUIPMENT = "equipment"
    OFFICE_SUPPLIES = "office_supplies"
    SOFTWARE = "software"
    UTILITIES = "utilities"
    OTHER = "other"

class ProcessingStatus(str, Enum):
    PENDING = "pending"
    AUTO_APPROVED = "auto_approved"
    APPROVED = "approved"
    REJECTED = "rejected"
    FLAGGED = "flagged"

class InvoiceData(BaseModel):
    """Schema for incoming invoice or receipt data."""
    invoice_number: str = Field(description="Unique invoice or receipt number")
    vendor: str = Field(description="Name of the vendor or merchant")
    amount: float = Field(description="Total amount of the invoice", gt=0, le=1000000)
    currency: str = Field(default="USD", description="Currency code")
    date: datetime = Field(description="Date of the invoice")
    category: ExpenseCategory = Field(description="Expense category")
    description: str = Field(description="Description of the expense")
    submitter: EmailStr = Field(description="Email of the person submitting the invoice")

class AnomalyAlert(BaseModel):
    """Schema for anomaly alerts."""
    alert_type: str = Field(description="Type of the alert")
    severity: str = Field(description="Severity level: low, medium, high")
    message: str = Field(description="Alert message")
    amount: Optional[float] = Field(default=None, description="Related amount")
    recommendation: str = Field(description="Actionable recommendation")

class ProcessingResult(BaseModel):
    """Final output schema after processing the invoice."""
    expense_id: str = Field(description="Unique ID for the processed expense")
    status: ProcessingStatus = Field(description="Final processing status")
    amount: float = Field(description="Processed amount")
    submitter: EmailStr = Field(description="Submitter email")
    category: ExpenseCategory = Field(description="Assigned category")
    review_notes: str = Field(description="Notes from the review process")
    anomalies: Optional[List[AnomalyAlert]] = Field(default=None, description="List of detected anomalies")
    created_at: datetime = Field(default_factory=datetime.now, description="Timestamp of creation")