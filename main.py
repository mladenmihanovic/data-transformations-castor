import pandas as pd
from pandas import DataFrame
import typer
import os

from src.data_transformations import (
    map_user_guids_to_user_ids,
    obfuscate_data,
    transform_date
)

from src.utils import obfuscate_email_address


OUTPUT_DIR = "data/output"
INPUT_DIR = "data/input"
DATE_FORMAT = "%Y-%m-%d"

def load_data(data_path:str) -> DataFrame:
    """
    Load data from a CSV file into a pandas DataFrame.
    Args:
        data_path (str): Path to the CSV file.
    Returns:
        DataFrame: Loaded data as a pandas DataFrame.
    """
    df = pd.read_csv(data_path)
    return df

def main(input_file: str, output_file: str) -> None: 

    input_filepath = f"{INPUT_DIR}/{input_file}"

    if not os.path.exists(input_filepath):
        raise FileNotFoundError(f"Input file {input_filepath} does not exist.")
    
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    output_file_path = f"{OUTPUT_DIR}/{output_file}"

    df = load_data(input_filepath)

    df = map_user_guids_to_user_ids(df)
    df = obfuscate_data(df, column_name="email_address", obfuscate_func=obfuscate_email_address)
    df = transform_date(df, column_name="last_login", input_date_format="%Y-%m-%d %H:%M:%S %Z", output_date_format=DATE_FORMAT)
    df = transform_date(df, column_name="start_date", input_date_format="%Y-%b-%d", output_date_format=DATE_FORMAT)
    df.to_csv(output_file_path, index=False)


if __name__ == "__main__":
   typer.run(main)
