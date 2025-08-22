import pandas as pd
import glob 

def clean_sales_data():
    """
    This function read all the daily sales data, combine it
    and filter out the sales information in a new csv file
    """
    # Take the location of all the dailY_sales file and read the csv
    all_files = glob.glob("../data/daily_sales_data_*.csv")
    all_dfs = [pd.read_csv(file) for file in all_files]

    # Concatenate every sales csv into one
    combined_df = pd.concat(all_dfs, ignore_index = False)

    # create a new dataframe with only Pink morsel sales summary
    df = combined_df[(combined_df["product"] == "pink morsel")].copy()
    
    # Debug Statement
    # print(df.head())
    # print(df.tail())

    df["price"] = df["price"].str.strip('$').astype(float)

    df["sales"] = df["price"] * df["quantity"]

    final_df = df[["sales", "date", "region"]]

    # output csv for a newly generated dataframe
    output_path = "pink_morsel_sales_summary.csv"
    final_df.to_csv(output_path, index = False)

    print("New sale summary of Pink Morsel is created at: ", output_path)

if __name__ == "__main__":
    clean_sales_data()
    