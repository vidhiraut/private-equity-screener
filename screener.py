import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def filter_data(df, min_revenue, min_margin, max_pe):
    filtered = df[
        (df["Revenue_Cr"] >= min_revenue) &
        (df["Profit_Margin"] >= min_margin) &
        (df["PE_Ratio"] <= max_pe)
    ]
    return filtered.sort_values(by="Revenue_Cr", ascending=False)
