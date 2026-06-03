import httpx
import json
import os

def extract_data():
	#Define URL API, get ASIA countries list
	API_URL = "https://restcountries.com/v3.1/region/asia"
	OUTPUT_FILE = "raw_countries.json"

	print(f"[INFO] Starting connect and loading data from: {API_URL}...")

	try:
		response = httpx.get(API_URL, timeout=10.0)
		response.raise_for_status()
		raw_data = response.json()

		print(f"[SUCCESS] Downloaded successfully the information of {len(raw_data)} countries!")

		#Write the raw data into a file JSON
		with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
		  json.dump(raw_data, f, ensure_ascii=False, indent=4)

		print(f"[SUCCESS] The raw data saved into a file: {OUTPUT_FILE}")

	except httpx.HTTPStatusError as exc:
		print(f"[ERROR] Response error from Server: {exc.response.status_code}")
	except Exception as e:
		print(f"[ERROR] handle unexpected error: {e}")

if __name__ == "__main__":
	extract_data()

