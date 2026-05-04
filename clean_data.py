import pandas as pd

df = pd.read_csv('netflix_reviews 2.csv')

print("Original shape:", df.shape)

# Drop duplicates
df = df.drop_duplicates()

# Drop rows where review content or score is missing
df = df.dropna(subset=['content', 'score'])

# Clean the date column
df['at'] = pd.to_datetime(df['at'])
df['date'] = df['at'].dt.date
df['month'] = df['at'].dt.to_period('M').astype(str)
df['year'] = df['at'].dt.year

# Add sentiment column based on score
def sentiment(score):
    if score >= 4:
        return 'Positive'
    elif score == 3:
        return 'Neutral'
    else:
        return 'Negative'

df['sentiment'] = df['score'].apply(sentiment)

print("Cleaned shape:", df.shape)

df.to_csv('netflix_reviews_cleaned.csv', index=False)
print("Done! Saved as netflix_reviews_cleaned.csv")

