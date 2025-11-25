from ucimlrepo import fetch_ucirepo
import pandas as pd
import numpy as np
import os
  
# Fetch dataset 
online_news_popularity = fetch_ucirepo(id=332) 
  
# Data (as pandas dataframes) 
X = online_news_popularity.data.features 
y = online_news_popularity.data.targets 
df = pd.concat([X, y], axis=1)

# Clean column names
df.columns = df.columns.str.strip()
  
# Drop non-predictive columns
cols_to_drop = ["url", "timedelta"]
df = df.drop(columns=cols_to_drop, errors="ignore")

# Remove duplicates
df = df.drop_duplicates()

df["log_shares"] = np.log1p(df["shares"])

output_dir = "data"
os.makedirs(output_dir, exist_ok=True)

df.to_csv(f"{output_dir}/online_news_cleaned.csv", index=False)