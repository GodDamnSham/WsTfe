import pandas as pd
import glob

# Path to the directory containing your CSV files
path = '/Users/malik/Downloads/csv'

all_files = glob.glob(path + "/*.csv")

# List to hold all data frames
dataframes = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    dataframes.append(df)
combined_df = pd.concat(dataframes, axis=0, ignore_index=True)

# Write the combined data frame to a new CSV file
combined_df.to_csv('combined.csv', index=False)
