# Placeholder for review-based sentiment analysis
def mock_sentiment_scores(df):
    import numpy as np
    df["Sentiment Score"] = np.random.uniform(3.5, 4.8, size=len(df))
    return df