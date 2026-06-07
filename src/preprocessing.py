import pandas as pd


def remove_duplicates(df):
    """
    Remove duplicate rows from a dataframe.
    """
    if df is None:
        raise ValueError("Input dataframe is None.")

    return df.drop_duplicates()


def convert_datetime_columns(df, columns):
    """
    Convert selected columns to datetime format.
    """
    for col in columns:
        if col not in df.columns:
            raise KeyError(f"Column not found: {col}")

        df[col] = pd.to_datetime(df[col], errors="coerce")

    return df


def convert_column_to_int(df, column):
    """
    Convert selected column to integer.
    """
    if column not in df.columns:
        raise KeyError(f"Column not found: {column}")

    df[column] = df[column].astype(int)

    return df


def check_missing_values(df):
    """
    Return missing value counts.
    """
    if df is None:
        raise ValueError("Input dataframe is None.")

    return df.isnull().sum()