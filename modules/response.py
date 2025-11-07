# def generate_response(intent, query, data=None):
#     if intent == "claim_status":
#         if data:
#             return f"Your claim {data[0]} filed on {data[2]} for amount {data[3]} is currently {data[1]}."
#         else:
#             return "I couldn’t find that claim ID. Please re-check."
    
#     elif intent == "policy_faq":
#         if data:
#             return f"Here’s what I found: {data}"
#         else:
#             return "Sorry, I couldn’t find a matching policy FAQ."
    
#     else:
#         return "I’ll escalate your query to a customer service representative."

#working
# def generate_response(intent, query, data):
#     if intent == "claim_status" and data:
#         # Access by column names
#         return f"Your claim {data['ClaimID']} filed on {data['DateFiled']} for amount {data['Amount']} is currently {data['claim_Status']}."
#     elif intent == "policy_faq" and data:
#         return data  # assuming FAQ answer is a string
#     else:
#         return "Sorry, I couldn't find the information you requested."

def generate_response(intent, query, data):
    if intent == "claim_status" and data:
        # Check if user is asking about date
        if "date" in query.lower() or "when" in query.lower():
            return f"Claim {data['ClaimID']} was filed on {data['DateFiled']}."
        # Check if user is asking about amount
        elif "amount" in query.lower() or "how much" in query.lower():
            return f"Claim {data['ClaimID']} amount is {data['Amount']}."
        # Default response (status)
        else:
            return f"Your claim {data['ClaimID']} filed on {data['DateFiled']} for amount {data['Amount']} is currently {data['claim_Status']}."
    elif intent == "policy_faq":
        return data  # fetched from FAQ KB
    else:
        return "Sorry, I could not understand your query."
