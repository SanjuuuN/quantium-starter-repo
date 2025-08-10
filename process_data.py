import pandas as pd
import glob

# Step 1: Find all CSV files in data folder
csv_files = glob.glob("data/*.csv")

# Step 2: Read and combine them into one DataFrame
df_list = []
for file in csv_files:
    temp_df = pd.read_csv(file)
    df_list.append(temp_df)

df = pd.concat(df_list, ignore_index=True)

# Step 3: Filter only Pink Morsels
df = df[df["product"].str.lower() == "pink morsel"]

# Step 4: Create sales column
df["sales"] = df["quantity"] * df["price"]

# Step 5: Keep only required columns
final_df = df[["sales", "date", "region"]]

# Step 6: Save to new CSV
final_df.to_csv("formatted_output.csv", index=False)

print("Data processed! Output saved to formatted_output.csv")
