from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import players
import pandas as pd
import os

# Create data directory if needed
os.makedirs("data", exist_ok=True)

# Find Steph Curry's player ID
player_dict = players.find_players_by_full_name("Stephen Curry")[0]
player_id = player_dict['id']

# Get player game logs for the 2023-24 season
gamelog = playergamelog.PlayerGameLog(player_id=player_id, season="2023")
df = gamelog.get_data_frames()[0]

# Preview and save
print(df.head())

df.to_csv("data/raw_stats.csv", index=False)
print(f"✅ Saved {len(df)} rows to data/raw_stats.csv")
