import uuid
from datetime import datetime
from app.schemas import InvoiceData, ExpenseCategory

def process_invoice_data(raw_data: dict) -> InvoiceData:
    """
    Processes raw invoice data and converts it into a validated InvoiceData model.
    In a production environment, this function would be replaced by an OCR pipeline.
    For this capstone, it simulates the extraction of structured data.
    """
    # Generate a unique ID if not provided
    invoice_number = raw_data.get("invoice_number", f"INV-{uuid.uuid4().hex[:8].upper()}")

    # Map category string to Enum if necessary, or default to OTHER
    category_str = raw_data.get("category", "other")
    try:
        category = ExpenseCategory(category_str)
    except ValueError:
        category = ExpenseCategory.OTHER

    # Parse date
    date_str = raw_data.get("date", datetime.now().isoformat())
    if isinstance(date_str, str):
        try:
            parsed_date = datetime.fromisoformat(date_str)
        except ValueError:
            parsed_date = datetime.now()
    else:
        parsed_date = date_str

    return InvoiceData(
        invoice_number=invoice_number,
        vendor=raw_data.get("vendor", "Unknown Vendor"),
        amount=float(raw_data.get("amount", 0.0)),
        currency=raw_data.get("currency", "USD"),
        date=parsed_date,
        category=category,
        description=raw_data.get("description", "No description provided"),
        submitter=raw_data.get("submitter", "unknown@example.com")
    )