import matplotlib.pyplot as plt
from data_loader import load_data, clean_data

def show_summary_stats(df):
    print(df.describe())

def plot_cost_vs_titles(df):
    plt.figure(figsize=(8, 5))
    plt.scatter(df["Monthly Cost"], df["Total Titles"], color="skyblue")
    for i, row in df.iterrows():
        plt.text(row["Monthly Cost"], row["Total Titles"], row["Service"])
    plt.xlabel("Monthly Cost ($)")
    plt.ylabel("Total Titles")
    plt.title("Streaming Services: Cost vs. Content")
    plt.grid(True)
    plt.tight_layout()
    plt.show()