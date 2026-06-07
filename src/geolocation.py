import numpy as np
import pandas as pd


def merge_ip_country(fraud_df, ip_df):
    """
    Merge Fraud_Data with IP-to-country data using range-based lookup.
    """
    required_fraud_cols = ["ip_address"]
    required_ip_cols = ["lower_bound_ip_address", "upper_bound_ip_address", "country"]

    for col in required_fraud_cols:
        if col not in fraud_df.columns:
            raise KeyError(f"Fraud dataframe missing column: {col}")

    for col in required_ip_cols:
        if col not in ip_df.columns:
            raise KeyError(f"IP dataframe missing column: {col}")

    fraud_df["ip_address"] = fraud_df["ip_address"].astype(int)
    ip_df["lower_bound_ip_address"] = ip_df["lower_bound_ip_address"].astype(int)
    ip_df["upper_bound_ip_address"] = ip_df["upper_bound_ip_address"].astype(int)

    fraud_sorted = fraud_df.sort_values("ip_address")
    ip_sorted = ip_df.sort_values("lower_bound_ip_address")

    fraud_geo = pd.merge_asof(
        fraud_sorted,
        ip_sorted,
        left_on="ip_address",
        right_on="lower_bound_ip_address",
        direction="backward"
    )

    fraud_geo["country"] = np.where(
        fraud_geo["ip_address"] <= fraud_geo["upper_bound_ip_address"],
        fraud_geo["country"],
        "Unknown"
    )

    return fraud_geo