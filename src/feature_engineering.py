import numpy as np
import pandas as pd


def add_time_features(df):
    """
    Add hour_of_day, day_of_week, and time_since_signup_hours.
    """
    required_columns = ["signup_time", "purchase_time"]

    for col in required_columns:
        if col not in df.columns:
            raise KeyError(f"Required column missing: {col}")

    df["hour_of_day"] = df["purchase_time"].dt.hour
    df["day_of_week"] = df["purchase_time"].dt.dayofweek

    df["time_since_signup_hours"] = (
        df["purchase_time"] - df["signup_time"]
    ).dt.total_seconds() / 3600

    return df


def add_transaction_features(df):
    """
    Add transaction frequency and velocity features.
    """
    required_columns = ["user_id", "device_id", "purchase_time", "time_since_signup_hours"]

    for col in required_columns:
        if col not in df.columns:
            raise KeyError(f"Required column missing: {col}")

    df["user_transaction_count"] = df.groupby("user_id")["purchase_time"].transform("count")
    df["device_transaction_count"] = df.groupby("device_id")["purchase_time"].transform("count")

    df["transaction_velocity"] = df["user_transaction_count"] / (
        df["time_since_signup_hours"] + 1
    )

    df["transaction_velocity"] = df["transaction_velocity"].replace(
        [np.inf, -np.inf], 0
    )

    return df