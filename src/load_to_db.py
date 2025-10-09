import pandas as pd
from sqlalchemy import create_engine, text

# Database connection details
DB_USER = "postgres"
DB_PASSWORD = "1234"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "transparency_bi"

CSV_PATH = "data/raw/seattle_operating_budget.csv"

df = pd.read_csv(CSV_PATH)

df.columns = df.columns.str.lower().str.replace(" ", "_").str.replace("[^a-zA-Z0-9_]", "", regex=True)

# Connect to PostgreSQL
engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Load into a table
table_name = "seattle_operating_budget"
df.to_sql(table_name, engine, if_exists="replace", index=False)

print(f"Loaded {len(df)} rows into table '{table_name}' in database '{DB_NAME}'.")

# Validation Checks
with engine.connect() as conn:
    # Row count
    row_count = conn.execute(text(f"SELECT COUNT(*) FROM public.{table_name};")).scalar()
    # Column count
    col_count = len(df.columns)
    # Sample data
    result = conn.execute(text(f"SELECT * FROM public.{table_name} LIMIT 3;"))
    sample_rows = result.mappings().all()  # ✅ Convert to list of dict-like objects

    print("📊 Validation Summary")
    print(f"   • Total rows in DB: {row_count}")
    print(f"   • Total columns: {col_count}")
    print("   • Sample rows:")
    for r in sample_rows:
        print("     ", dict(r))
