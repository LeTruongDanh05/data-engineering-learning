import json
import pandas as pd
from pydantic import BaseModel, Field
from typing import List, Optional

# Defind data (PYDANTIC)
class RawCountryModel(BaseModel):
    cca3: str = Field(..., min_length=3, max_length=3)
    name: dict
    capital: Optional[List[str]] = []
    region: str
    population: int = Field(..., ge=0)

# Transform
def transform_data():
    INPUT_FILE = "raw_countries.json"
    OUTPUT_FILE = "cleaned_countries.csv"

    print(f"[INFO] Starting the process Transform data...")

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
      raw_list = json.load(f)

    validated_countries = []

    for item in raw_list:
        try:
                country_clean = RawCountryModel(**item)

                flattened_item = {
                "country_code": country_clean.cca3,
                "country_name": country_clean.name.get("common", "Unknown"),
                "capital": country_clean.capital[0] if country_clean.capital else None,
                "region": country_clean.region,
                "population": country_clean.population
            	}
                validated_countries.append(flattened_item)

        except Exception as e:
                print(f"[WARNING] Ignore a faulty record due to: {e}")

    # Transform into a clean table (PANDAS)

    df = pd.DataFrame(validated_countries)

    df = df.sort_values(by="population", ascending=False)

    df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")

    print(f"[SUCCESS] Data cleaned and saved as table: {OUTPUT_FILE}")
    print(f"\n------- The 5 most populous countries in Asia -------")
    print(df.head(5).to_string(index=False))

if __name__ == "__main__":
	transform_data()
