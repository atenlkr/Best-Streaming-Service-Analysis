def recommend(df, preference="content"):
    if preference == "cost":
        return df.sort_values(by="Monthly Cost").iloc[0]
    elif preference == "content":
        return df.sort_values(by="Total Titles", ascending=False).iloc[0]
    elif preference == "rating":
        return df.sort_values(by="User Rating", ascending=False).iloc[0]
    else:
        return df.iloc[0]