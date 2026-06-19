from app.schemas import InvoiceData, ExpenseCategory

def auto_classify_expense(invoice: InvoiceData) -> str:
    """
    Analyzes the vendor and description to suggest or confirm the expense category.
    Returns a string indicating the classification result.
    """
    vendor = invoice.vendor.lower()
    description = invoice.description.lower()

    # Simple keyword-based classification logic
    if any(word in vendor or word in description for word in ["uber", "taxi", "airline", "hotel", "marriott"]):
        suggested_category = ExpenseCategory.TRAVEL
    elif any(word in vendor or word in description for word in ["restaurant", "cafe", "mcdonalds", "starbucks"]):
        suggested_category = ExpenseCategory.MEALS
    elif any(word in vendor or word in description for word in ["amazon", "staples", "dell", "apple"]):
        suggested_category = ExpenseCategory.EQUIPMENT
    else:
        suggested_category = ExpenseCategory.OTHER

    # Check if the suggested category matches the provided one
    if invoice.category == suggested_category:
        return f"Category '{invoice.category.value}' verified successfully."
    else:
        return f"Category mismatch detected. Provided: '{invoice.category.value}', Suggested: '{suggested_category.value}'."