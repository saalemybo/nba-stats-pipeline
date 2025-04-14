import pandas as pd
import os

# Load raw Curry game data
df = pd.read_csv("data/raw_stats.csv")

# Select relevant columns
columns_to_keep = [
    'GAME_DATE', 'MATCHUP', 'WL', 'MIN', 'PTS', 'REB', 'AST',
    'STL', 'BLK', 'TOV', 'FGM', 'FGA', 'FG3M', 'FG3A', 'PLUS_MINUS'
]
df = df[columns_to_keep]

# Clean column names (optional)
df.columns = df.columns.str.lower()

# Convert game_date to datetime
df['game_date'] = pd.to_datetime(df['game_date'])

# Save cleaned data
df.to_csv("data/clean_stats.csv", index=False)
print(f"✅ Saved cleaned Curry stats to data/clean_stats.csv with {len(df)} rows.")
