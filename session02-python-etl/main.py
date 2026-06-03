import time
from extract import extract_data
from transform import transform_data
from load import load_data

def run_complete_etl_pipeline():
    start_time = time.time()

    extract_data()
    print("-" * 50)

    transform_data()
    print("-" * 50)

    load_data()

    end_time = time.time()
    duration = round(end_time - start_time, 2)
    print(f"Pipeline executed successfully in {duration} seconds")

if __name__ == "__main__":
   run_complete_etl_pipeline()
