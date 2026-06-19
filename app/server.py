import uuid
from datetime import datetime
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from .schemas import InvoiceData, ProcessingResult, ProcessingStatus, AnomalyAlert
from .tools.extractor import process_invoice_data
from .tools.classifier import auto_classify_expense
from .tools.analyzer import detect_anomalies
from .security import detect_prompt_injection

app = FastAPI(
    title="Smart Invoice Processor API",
    description="Enterprise-grade invoice processing agent",
    version="1.0.0"
)

@app.get("/")
def root():
    """Root endpoint with API information."""
    return {
        "service": "Smart Invoice Processor API",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "process": "/process"
        }
    }

@app.get("/health")
def health_check():
    """Check if the server is running."""
    return {"status": "ok", "service": "Smart Invoice Processor"}

@app.post("/process")
async def process_invoice(invoice: InvoiceData):
    """Process an incoming invoice through the agent pipeline."""
    try:
        # Generate unique expense ID
        expense_id = f"EXP-{uuid.uuid4().hex[:8].upper()}"
        
        # Security Check: Detect prompt injection in description
        if detect_prompt_injection(invoice.description):
            result = ProcessingResult(
                expense_id=expense_id,
                status=ProcessingStatus.REJECTED,
                amount=invoice.amount,
                submitter=invoice.submitter,
                category=invoice.category,
                review_notes="Security Alert: Potential prompt injection detected in description.",
                anomalies=[AnomalyAlert(
                    alert_type="SECURITY_THREAT",
                    severity="high",
                    message="Malicious content detected in description field.",
                    recommendation="Reject this submission immediately."
                )]
            )
            return JSONResponse(content=result.model_dump(mode='json'))
        
        # Step 1: Process and validate invoice data
        validated_invoice = process_invoice_data(invoice.model_dump())
        
        # Step 2: Auto-classify expense category
        classification_result = auto_classify_expense(validated_invoice)
        
        # Step 3: Detect anomalies based on business rules
        detected_anomalies = detect_anomalies(validated_invoice)
        
        # Step 4: Determine final status based on anomalies
        if len(detected_anomalies) > 0:
            final_status = ProcessingStatus.FLAGGED
            review_notes = f"Flagged for human review. {classification_result} Anomalies detected: {len(detected_anomalies)}."
        else:
            final_status = ProcessingStatus.AUTO_APPROVED
            review_notes = f"Auto-approved. {classification_result}"
        
        # Build final result
        result = ProcessingResult(
            expense_id=expense_id,
            status=final_status,
            amount=validated_invoice.amount,
            submitter=validated_invoice.submitter,
            category=validated_invoice.category,
            review_notes=review_notes,
            anomalies=detected_anomalies if detected_anomalies else None,
            created_at=datetime.now()
        )
        
        # Use mode='json' to convert datetime objects to ISO format strings
        return JSONResponse(content=result.model_dump(mode='json'))
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))