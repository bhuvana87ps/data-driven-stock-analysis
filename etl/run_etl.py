import sys
import os

# Ensure the project root is added to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from etl.extract import get_all_yaml_files, process_yaml_file
from etl.transform import Transformer
from etl.load import Loader


def run_etl():

    print("\n=========== ETL PIPELINE STARTED ===========\n")

    # ---------------------------------------------------------
    # 1. INITIALIZE TRANSFORMER + LOADER
    # ---------------------------------------------------------
    transformer = Transformer()

    loader = Loader(
        output_csv_dir="output_csv",
        output_combined_dir="output_combined",
        output_reports_dir="output_reports"
    )

    # ---------------------------------------------------------
    # 2. GET ALL YAML FILES FROM DATA FOLDER
    # ---------------------------------------------------------
    yaml_files = get_all_yaml_files()

    if not yaml_files:
        print("No YAML files found. ETL stopped.")
        return

    print(f"Total YAML files found: {len(yaml_files)}\n")

    # ---------------------------------------------------------
    # 3. PROCESS EACH YAML FILE
    # ---------------------------------------------------------
    for file in yaml_files:
        print(f"Processing File: {file}")

        raw_rows = process_yaml_file(file)

        # -----------------------------------------------------
        # 4. TRANSFORM EACH RAW ROW
        # -----------------------------------------------------
        for raw in raw_rows:

            clean_row = transformer.normalize(raw)

            if not transformer.is_valid(clean_row):
                print("Skipping invalid row:", clean_row)
                continue

            # Send clean row to Loader (write symbol CSV)
            loader.write_symbol_csv(clean_row)

    # ---------------------------------------------------------
    # 5. AFTER ALL ROWS DONE → CREATE FINAL DATASETS
    # ---------------------------------------------------------

    print("\nWriting combined CSV...")
    loader.write_combined_csv()

    print("Writing monthly summary reports...")
    loader.write_monthly_reports()

    print("\n=========== ETL PIPELINE COMPLETED SUCCESSFULLY ===========\n")


if __name__ == "__main__":
    run_etl()
