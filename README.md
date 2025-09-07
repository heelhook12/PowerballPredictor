# Powerball Predictor & Analysis

## Script 1: Basic Number Analysis & Prediction

**Purpose:**
Predict potential Powerball numbers based on historical draws since 2020. Provides “hot numbers,” “cold numbers,” and a weighted random pick.

**Features:**
- Load CSV of Powerball draws (`Draw Date`, `Winning Numbers`, `Multiplier`).
- Split winning numbers into 5 main numbers (N1–N5) and Powerball.
- Frequency Analysis:
  - Hot numbers: most frequently drawn numbers.
  - Cold numbers: least frequently drawn numbers.
- Weighted Random Pick:
  - Generates a set of numbers based on the frequency distribution of past draws.
- Python int conversion:
  - Ensures all numbers are standard Python integers (no `numpy.int64`).

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
- Numbers are unordered (Powerball rules).
- Weighted random numbers are drawn separately for main numbers (1–69) and Powerball (1–26).

---

## Script 2: Advanced Data Analysis & Rolling Frequency Visualization

**Purpose:**
Perform deeper analysis on historical Powerball data. Includes **sum/range analysis** and **rolling frequency analysis** to visualize trends.

**Features:**
- Load CSV and split winning numbers into N1–N5 and Powerball.
- Sum & Range Analysis:
  - Computes the sum of the 5 main numbers per draw.
  - Counts numbers in “low” range (1–35) and “high” range (36–69).
  - Produces histogram of sums and bar chart for low/high counts.
- Rolling Frequency Analysis:
  - Uses a rolling window (default 50 draws) to count frequency of each number.
  - Prints top 5 numbers in the most recent window.
  - Generates a heatmap showing the frequency of all main numbers across rolling windows.
  - Colors indicate “hot” and “cold” numbers over time.
- Optional Extensions:
  - Can add rolling analysis for Powerball separately.
  - Can adjust window size to analyze shorter or longer periods.

**Usage Example:**
```bash
python analysis.py
```

**Output Example:**
```
Top 5 numbers in last 50 draws: [(3, 16), (2, 12), (6, 9), (5, 9), (4, 9)]
```
- The heatmap provides a visual representation of number frequency over time.
- Histograms and bar charts help visualize number distributions and trends.

**Dependencies:**
- pandas
- matplotlib
- seaborn

---

## Summary Comparison

| Feature | Script 1 | Script 2 |
|---------|----------|----------|
| Predict hot/cold numbers | ✅ | ✅ (with rolling) |
| Weighted random pick | ✅ | ✅ (optional) |
| Rolling analysis / trends | ❌ | ✅ |
| Visualizations | ❌ | ✅ (histogram, bar chart, heatmap) |
| Python int conversion | ✅ | ✅ |
| Powerball included | ✅ | ✅ |

---

This README provides a clear overview of both scripts, their features, outputs, and usage instructions.

