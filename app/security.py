import re

# List of common prompt injection patterns
INJECTION_PATTERNS = [
    r"ignore\s+(all\s+)?rules",
    r"bypass\s+(all\s+)?rules",
    r"approve\s+immediately",
    r"disregard\s+previous",
    r"you\s+are\s+now\s+an?\s+unrestricted",
    r"drop\s+table",
    r";\s*--",
]

def detect_prompt_injection(text: str) -> bool:
    """
    Scans the input text for potential prompt injection attacks.
    Returns True if a malicious pattern is detected, False otherwise.
    """
    if not text:
        return False
    
    text_lower = text.lower()
    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, text_lower):
            return True
            
    return False