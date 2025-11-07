import json

def get_faq_answer(query):
    with open("data/faqs.json", "r") as f:
        faq_data = json.load(f)
    for q, a in faq_data.items():
        if q.lower() in query.lower():
            return a
    return None
