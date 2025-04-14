import pandas as pd
import sqlite3
import os

# Load cleaned data
df = pd.read_csv("data/clean_stats.csv")

# Create or connect to SQLite DB
db_path = "database/nba_stats.db"
os.makedirs("database", exist_ok=True)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Drop old table (optional)
cursor.execute("DROP TABLE IF EXISTS curry_game_logs")

# Load into SQL
df.to_sql("curry_game_logs", conn, index=False)

# Check row count
cursor.execute("SELECT COUNT(*) FROM curry_game_logs")
print(f"✅ Loaded {cursor.fetchone()[0]} rows into curry_game_logs table.")

conn.commit()
conn.close()
