def rank_by_cost(df):
    return df.sort_values(by="Monthly Cost")

def rank_by_content(df):
    return df.sort_values(by="Total Titles", ascending=False)

def rank_by_rating(df):
    return df.sort_values(by="User Rating", ascending=False)