# Netflix Reviews Dashboard 🎬

A complete end-to-end data analysis project built from scratch.

## 📊 Project Overview
Analysed 150,000+ Netflix app reviews from Kaggle to uncover insights about user sentiment, ratings distribution, and review trends over time.

## 🛠️ Tools Used
- **Git & GitHub** — version control and project management
- **Python 3.13** — data cleaning and processing
- **Pandas** — data manipulation
- **Power BI (Web)** — dashboard and visualisations

## 📁 Project Structure
- `netflix_reviews 2.csv` — original raw dataset from Kaggle
- `netflix_reviews_cleaned.csv` — cleaned dataset ready for analysis
- `clean_data.py` — Python script used to clean the data
- `git_commands.md` — all Git commands used in this project

## 🔍 Key Insights
- Nearly 48% of reviews are Negative
- 1-star reviews are the most common (~60,000)
- Review volume spiked dramatically in 2024 and 2026
- 1-star reviews get the most thumbs up — people agree with complaints!

## 🧹 Data Cleaning Steps
- Removed duplicate rows
- Dropped rows with missing review content or score
- Converted date column to datetime format
- Extracted month and year from date
- Added sentiment column based on score (Positive/Neutral/Negative)

## 📈 Dashboard Charts
1. Rating Distribution (Bar Chart)
2. Sentiment Breakdown (Pie Chart)
3. Reviews Over Time (Line Chart)
4. Thumbs Up by Score (Bar Chart)
