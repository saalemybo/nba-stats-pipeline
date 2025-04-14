# 🏀 NBA Player Stats Pipeline

This project builds a full data pipeline that extracts NBA player stats from the `balldontlie` API, processes and cleans the data using Python, and stores it in a SQL database for analysis and visualization.

## 🔁 Features
- Extract player data from an open NBA API
- Transform and clean raw stats using `pandas`
- Load structured data into a local SQLite database
- Analyze trends (e.g., top scorers, team averages)
- Set up for optional visualizations with `matplotlib` or `seaborn`

## 🛠 Tech Stack
- Python
- Requests
- Pandas
- SQLite3
- SQLAlchemy (optional)
- Matplotlib / Seaborn

## 📂 Project Structure

nba-stats-pipeline/ ├── scripts/ │ ├── extract.py │ ├── transform.py │ └── load.py ├── database/ │ └── schema.sql ├── analysis/ │ └── player_trends.ipynb ├── data/ (ignored) ├── README.md ├── .gitignore └── requirements.txt

## 🚀 How to Run

1. Clone this repo  
2. Run the scripts in order: `extract.py` → `transform.py` → `load.py`  
3. Open the notebook to explore the data

## 📊 Sample Questions to Answer
- Who are the top 10 scorers this season?
- Which teams have the most efficient players?
- How do players' stats change over the season?

## 📌 To Do
- [ ] Add advanced metrics (e.g., PER, usage rate)
- [ ] Automate daily updates
- [ ] Add Streamlit dashboard

---
