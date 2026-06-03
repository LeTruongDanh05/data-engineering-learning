import pandas as pd
from sqlalchemy import create_engine

def load_data():
    INPUT_FILE = "cleaned_countries.csv"
    DB_FILE = "warehouse.db"
    TABLE_NAME = "asia_countries"

    print(f"[INFO] Starting the process Load data into Database...")

    try:
       df = pd.read_csv(INPUT_FILE)

       engine = create_engine(f"sqlite:///{DB_FILE}")

       df.to_sql(TABLE_NAME, con=engine, if_exists="replace", index=False)

       print(f"[SUCCESS] Loaded successfully {len(df)} countries into a table '{TABLE_NAME}'!")

       query = f"SELECT country_code, country_name, population FROM {TABLE_NAME} LIMIT 3"

       with engine.connect() as connection:
            # Use pandas to run SQL SELECT directly in Database
            db_result = pd.read_sql(query, connection)
            print(db_result.to_string(index=False))

    except Exception as e:
       print(f"[ERROR] The loading process is failed due to {e}")

if __name__ == "__main__":
   load_data()
