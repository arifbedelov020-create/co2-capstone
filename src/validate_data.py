import pandas as pd

# Read the original CO2 dataset
df = pd.read_csv("data/archive.csv")

# Show the number of rows and columns
print("Dataset shape:", df.shape)

# Count missing CO2 measurements
missing = df["Carbon Dioxide (ppm)"].isna().sum()
print("Missing CO2 values:", missing)

# Find repeated Year-Month combinations
duplicates = df.duplicated(subset=["Year", "Month"]).sum()
print("Duplicate Year-Month rows:", duplicates)

# Find invalid month numbers
invalid_months = df[~df["Month"].isin(range(1, 13))]
print("Invalid month rows:", len(invalid_months))

# Count valid measurements for each year
yearly_counts = df.groupby("Year")["Carbon Dioxide (ppm)"].count()

# Count the different months in each year
unique_months = df.groupby("Year")["Month"].nunique()

# Select years with 12 measurements and all 12 different months
complete_years = yearly_counts[
    (yearly_counts == 12) & (unique_months == 12)
].index

print("Complete years:", len(complete_years))
print("Incomplete years:", sorted(set(df["Year"]) - set(complete_years)))



# Save the dataset quality results to a text file
summary = f"""CO2 Dataset Quality Summary

Dataset: Mauna Loa atmospheric CO2
Source: Kaggle (UC San Diego)
Total rows: {df.shape[0]}
Total columns: {df.shape[1]}
Missing CO2 measurements: {missing}
Duplicate Year-Month rows: {duplicates}
Invalid month rows: {len(invalid_months)}
Complete years: {len(complete_years)}
Incomplete years: {sorted(set(df["Year"]) - set(complete_years))}

Main regression uses complete years only.
The year 2017 is excluded from the study period.
"""

with open("results/data_quality_summary.txt", "w", encoding="utf-8") as file:
    file.write(summary)

print("Data quality summary saved successfully.")
