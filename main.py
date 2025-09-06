import pandas as pd
import random
from collections import Counter



def load_data(file_path):
    #loading csv file
    df = pd.read_csv(file_path)

    #data format
    numbers = df["Winning Numbers"].str.split(" ", expand=True).astype(int)
    numbers.columns = ["N1", "N2", "N3", "N4", "N5", "Powerball"]


    #merge back into df
    df = pd.concat([df[["Draw Date"]], numbers], axis=1)
    return df


def analyze_and_predict(df, main_count=5):
    # Flatten all main numbers (first 5 columns)
    all_main = [int(num) for num in df[["N1","N2","N3","N4","N5"]].values.flatten()]
    all_powerballs = [int(num) for num in df["Powerball"].values]

    
    # Count frequencies
    main_freq = Counter(all_main)
    power_freq = Counter(all_powerballs)
    
    # most common
    hot_main = [int(num) for num, _ in main_freq.most_common(main_count)]
    hot_power = int(power_freq.most_common(1)[0][0])
    
    # least common
    cold_main = [int(num) for num, _ in main_freq.most_common()[-main_count:]]
    cold_power = int(power_freq.most_common()[-1][0])
    
    # Weighted random pick
    weighted_main = random.sample(list(main_freq.elements()), main_count)
    weighted_power = int(random.choice(list(power_freq.elements())))
    
    return {
        "hot_pick": (sorted(hot_main), hot_power),
        "cold_pick": (sorted(cold_main), cold_power),
        "weighted_pick": (sorted(weighted_main), weighted_power)
    }

if __name__ == "__main__":
    file_path = "Lottery_Powerball_Winning_Numbers__Beginning_2010.csv"
    df = load_data(file_path)
    predictions = analyze_and_predict(df)
    
    print("Hot Numbers:", predictions["hot_pick"])
    print("Cold Numbers:", predictions["cold_pick"])
    print("Weighted Random Pick:", predictions["weighted_pick"])