import os
import pandas as pd


def load_csv(file_path):
    """
    Load a CSV file with basic error handling.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        df = pd.read_csv(file_path)

        if df.empty:
            raise ValueError(f"The file is empty: {file_path}")

        return df

    except pd.errors.EmptyDataError:
        raise ValueError(f"The CSV file is empty or invalid: {file_path}")

    except Exception as e:
        raise RuntimeError(f"Error loading file {file_path}: {e}")