import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, String, BigInteger
from sqlalchemy.dialects.postgresql import insert

def load_data():
    INPUT_FILE = "cleaned_countries.csv"
    DB_URL = "postgresql://Danh_Le:14005@localhost:5432/warehouse"
    TABLE_NAME = "asia_countries"

    print(f"[INFO] Starting the process Load data into Database...")

    try:
       df = pd.read_csv(INPUT_FILE)

       engine = create_engine(DB_URL)

       metadata = MetaData()

       asia_countries_table = Table(
            TABLE_NAME, metadata,
            # Set primary key
            Column('country_code', String, primary_key=True),
            Column('country_name', String),
            Column('population', BigInteger),
            Column('region', String),
            Column('capital', String)
        )

       metadata.create_all(engine)
       print(f"[INFO] Table '{TABLE_NAME}' created successfully.")

       records = df.to_dict(orient="records")

       with engine.begin() as connection:
            for record in records:
                # Create an INSERT command
                stmt = insert(asia_countries_table).values(record)

                # Configuration UPSERT behavior: If duplicated 'country_code', automatically UPDATE the remaining columns
                upsert_stmt = stmt.on_conflict_do_update(
                    index_elements=['country_code'],
                    set_={
                        'country_name': stmt.excluded.country_name,
                        'population': stmt.excluded.population,
                        'region': stmt.excluded.region,
                        'capital': stmt.excluded.capital
                    }
                )
                connection.execute(upsert_stmt)

       print(f"[SUCCESS] Upserted successfully {len(df)} countries into PostgreSQL table '{TABLE_NAME}'!")

       query = f"SELECT country_code, country_name, population FROM {TABLE_NAME} LIMIT 3"

       db_result = pd.read_sql(query, engine)
       print("\n[INFO] Preview data from PostgreSQL:")
       print(db_result.to_string(index=False))

    except Exception as e:
       print(f"[ERROR] The loading process failed due to {e}")

if __name__ == "__main__":
   load_data()
