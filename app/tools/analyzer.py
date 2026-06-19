from app.schemas import InvoiceData, AnomalyAlert

def detect_anomalies(invoice: InvoiceData) -> list:
    """
    Checks the invoice against basic business rules to detect anomalies.
    Returns a list of AnomalyAlert objects.
    """
    alerts = []

    # Rule 1: High-value transaction threshold
    if invoice.amount > 5000:
        alerts.append(AnomalyAlert(
            alert_type="HIGH_VALUE",
            severity="high",
            message=f"Transaction amount ${invoice.amount} exceeds the standard $5000 limit.",
            amount=invoice.amount,
            recommendation="Requires executive approval."
        ))

    # Rule 2: Weekend transaction check
    if invoice.date.weekday() >= 5:  # 5 is Saturday, 6 is Sunday
        alerts.append(AnomalyAlert(
            alert_type="WEEKEND_TRANSACTION",
            severity="medium",
            message=f"Transaction occurred on a weekend ({invoice.date.strftime('%A')}).",
            amount=invoice.amount,
            recommendation="Verify if this was a legitimate business expense."
        ))

    return alerts