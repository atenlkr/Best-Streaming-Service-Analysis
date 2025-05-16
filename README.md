# 📊 Streaming Service Analysis

This Python-based project provides a comprehensive analysis of the most popular streaming platforms available today. It includes data processing, visualization, ranking, sentiment analysis (mocked), and a recommendation system.

---

## 📁 Project Structure

```
streaming_service_analysis/
│
├── data/
│   └── streaming_data.csv         # Main dataset for streaming services
│
├── analysis/
│   ├── data_loader.py             # Load and clean the dataset
│   ├── exploratory_analysis.py    # Visualize and summarize insights
│   ├── ranking_services.py        # Rank platforms by cost, content, rating
│   ├── sentiment_analysis.py      # Mock sentiment scores for services
│   └── recommendation.py          # Recommend the best service
│
├── README.md                      # Project documentation
```

---

## 📌 Features

- 📥 **Data Loader**: Efficient CSV reader and cleaner
- 📊 **Exploratory Analysis**: Summary statistics, scatter plots, and more
- 🏆 **Ranking System**: Sort services by cost, content, or user rating
- 💬 **Sentiment Analysis**: Adds a mock sentiment score to services
- 🎯 **Recommendation Engine**: Suggests a service based on user preference

---

## 🧪 Technologies Used

- Python 3
- pandas
- matplotlib
- numpy

---

## 🚀 How to Run

1. Clone the project or unzip the downloaded folder.
2. Install required libraries:

```bash
pip install pandas matplotlib numpy
```

3. Run individual scripts from the `analysis/` folder as needed, for example:

```bash
python analysis/exploratory_analysis.py
```

---

## 👤 Credits

Developed by **Atenshen Longkumer** with help from ChatGPT.

---

## 📂 Data Snapshot

| Service         | Monthly Cost | Total Titles | Originals Count | User Rating |
|----------------|--------------|---------------|------------------|--------------|
| Netflix         | $15.49       | 5000          | 1500             | 4.5          |
| Hulu            | $7.99        | 3000          | 800              | 4.0          |
| Disney+         | $7.99        | 2000          | 900              | 4.2          |
| Amazon Prime    | $8.99        | 4000          | 700              | 4.1          |
| HBO Max         | $9.99        | 2500          | 1000             | 4.3          |
| ...             | ...          | ...           | ...              | ...          |

---

Enjoy analyzing and comparing your favorite streaming services!