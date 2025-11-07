import re

def classify_intent(query: str) -> str:
    query = query.lower()
    if "claim" in query or "status" in query:
        return "claim_status"
    elif "policy" in query or "premium" in query or "document" in query:
        return "policy_faq"
    else:
        return "escalation"
    
def extract_claim_id(text: str) -> list:
    """
    Extract claim IDs from a string.
    Assumes claim IDs follow a pattern like CLM123456, CLAIM-12345, etc.
    """
    # Example pattern: CLM followed by 3-10 digits
    pattern = r'\bCLM[-]?\d{3,10}\b'
    claim_ids = re.findall(pattern, text.upper())
    return claim_ids
