import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import seaborn as sns


def load_data(file_path):
    df = pd.read_csv(file_path)
    numbers = df["Winning Numbers"].str.split(" ", expand=True).astype(int)
    numbers.columns = ["N1", "N2", "N3", "N4", "N5", "Powerball"]
    df = pd.concat([df[["Draw Date"]], numbers], axis=1)
    return df


def sum_and_range_analysis(df):
    df["Draw_Sum"] = df[["N1","N2","N3","N4","N5"]].sum(axis=1)
    df["Low_Count"] = (df[["N1","N2","N3","N4","N5"]] <= 35).sum(axis=1)
    df["High_Count"] = (df[["N1","N2","N3","N4","N5"]] > 35).sum(axis=1)
    
 
    plt.figure(figsize=(10,5))
    plt.hist(df["Draw_Sum"], bins=20, color='skyblue', edgecolor='black')
    plt.title("Distribution of Sum of Main Numbers")
    plt.xlabel("Sum of 5 Main Numbers")
    plt.ylabel("Frequency")
    plt.show()
    

    low_high = pd.DataFrame({
        "Low (1-35)": df["Low_Count"].value_counts(),
        "High (36-69)": df["High_Count"].value_counts()
    }).sort_index()
    
    low_high.plot(kind="bar", figsize=(10,5), color=['orange','green'])
    plt.title("Frequency of Low vs High Numbers in Draws")
    plt.xlabel("Count of Numbers in Range")
    plt.ylabel("Frequency")
    plt.show()


def rolling_frequency_analysis(df, window=50):
    all_numbers = df[["N1","N2","N3","N4","N5"]]
    rolling_counts = []
    for i in range(window, len(df)+1):
        window_data = all_numbers.iloc[i-window:i].values.flatten()
        count = Counter(window_data)
        rolling_counts.append([count.get(num, 0) for num in range(1, 70)]) 
    

    rolling_df = pd.DataFrame(rolling_counts, columns=range(1,70))
    
    # Plot heatmap
    plt.figure(figsize=(20,8))
    sns.heatmap(rolling_df.T, cmap="YlGnBu", cbar_kws={'label': 'Frequency'})
    plt.xlabel(f"Rolling Window Index (window={window})")
    plt.ylabel("Main Numbers (1-69)")
    plt.title(f"Rolling Frequency Heatmap of Main Numbers over {window} Draws")
    plt.show()
    

    print("Top 5 numbers in last", window, "draws:", Counter(rolling_df.iloc[-1]).most_common(5))


if __name__ == "__main__":
    file_path = "Lottery_Powerball_Winning_Numbers__Beginning_2010.csv"
    df = load_data(file_path)
    
    sum_and_range_analysis(df)
    rolling_frequency_analysis(df, window=50)
