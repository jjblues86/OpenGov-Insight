"""
extract.py
Extracts City of Seattle Budget data from the Open Data API and saves to /data/raw/.
"""

import os
import pandas as pd
from sodapy import Socrata

def extract_operating_budget(limit: int = 50000, save_path: str = "data/raw/seattle_operating_budget.csv"):
    """
    Extracts the Seattle Operating Budget dataset via Socrata and saves to CSV.
    """
    DOMAIN = "data.seattle.gov"
    DATASET_ID = "8u2j-imqx"
    APP_TOKEN = os.getenv("SOCRATA_APP_TOKEN", None)

    client = Socrata(DOMAIN, APP_TOKEN)

    # Fetch data
    results = client.get(DATASET_ID, limit=limit)
    df = pd.DataFrame.from_records(results)

    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    df.to_csv(save_path, index=False)
    print(f"Extracted {len(df)} rows; saved to {save_path}")

    return df

if __name__ == "__main__":
    extract_operating_budget()

# # 1. Initialize Socrata client
# DOMAIN = "data.seattle.gov"
# DATASET_ID = "8u2j-imqx"
#
# # You can register for an app token
# APP_TOKEN = os.getenv("SOCRATA_APP_TOKEN", None)
#
# client = Socrata(DOMAIN, APP_TOKEN)
#
# # 2. Extract Data
# LIMIT = 1000
# results = client.get(DATASET_ID, limit=LIMIT)
# df = pd.DataFrame.from_records(results)
#
# # 3. Ensure numeric and date fields are correctly typed
# df["fiscal_year"] = pd.to_numeric(df["fiscal_year"], errors="coerce")
# df["adopted_budget"] = pd.to_numeric(df["adopted_budget"], errors="coerce")
#
# # 4. Save Raw Data
# os.makedirs("data/raw", exist_ok=True)
# output_path = "data/raw/seattle_budget_raw.csv"
# df.to_csv(output_path, index=False)
#
# print(f"Data successfully extracted! Saved {len(df)} rows to {output_path}")