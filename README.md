# 🎰 Powerball Predictor & Analysis 🎰

## Script 1: Basic Number Analysis & Prediction

**Purpose:**
Want to see which numbers might be "lucky" based on past draws? This script predicts potential Powerball numbers using historical data since 2020. It gives you hot numbers, cold numbers, and a weighted random pick! 🍀

**Features:**
- Load your Powerball CSV (`Draw Date`, `Winning Numbers`, `Multiplier`).
- Split winning numbers into 5 main numbers (N1–N5) and the all-important Powerball.
- Frequency Analysis:
  - **Hot numbers**: the crowd favorites appearing most often.
  - **Cold numbers**: those shy numbers that barely show up.
- Weighted Random Pick:
  - Pick numbers based on past frequency. 


**Usage Example:**
```bash
python main.py
```

**Output Example:**
```
Hot Numbers: ([21, 23, 28, 36, 39], 24)
Cold Numbers: ([60, 65, 66, 67, 68], 37)
Weighted Random Pick: ([10, 15, 16, 58, 63], 17)
```

**Notes:**
- Order doesn’t matter for main numbers.
- Powerball is picked separately (1–26).

---

## Script 2: Advanced Data Analysis & Rolling Frequency Visualization 📊

**Purpose:**
Dive deep into the numbers! This script gives you visual insights, rolling trends, and helps show which numbers are "hot" or "cold" over time.

**Features:**
- Load CSV and split winning numbers into N1–N5 and Powerball.
- **Sum & Range Analysis:**
  - Compute the sum of main numbers per draw.
  - Count low (1–35) vs high (36–69) numbers.
  - Beautiful histogram of sums and a bar chart showing low/high frequency.
- **Rolling Frequency Analysis:**
  - Check number trends over the last N draws (default 50). 
  - See the top 5 numbers in recent windows.
  - Heatmap of number frequency over rolling windows
- Optional: Add Powerball analysis and adjust window size to zoom in or out.

**Usage Example:**
```bash
python analysis.py
```

**Output Example:**
```
Top 5 numbers in last 50 draws: [(3, 16), (2, 12), (6, 9), (5, 9), (4, 9)]
```
- Charts make using eyes easy.

**Dependencies:**
- pandas
- matplotlib
- seaborn

---
