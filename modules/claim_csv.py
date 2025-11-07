import pandas as pd

def get_claim_status(claim_id):
    df = pd.read_csv("data/claims.csv")
    row = df[df['ClaimID'] == claim_id]
    if not row.empty:
        claim = row.iloc[0]
        return claim["ClaimID"], claim["Status"], claim["DateFiled"], claim["Amount"]
    return None
