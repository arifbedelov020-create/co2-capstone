import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
from statsmodels.stats.stattools import durbin_watson

df = pd.read_csv("data/archive.csv")

print(df.head())

df.info()

missing = df[df["Carbon Dioxide (ppm)"].isna()]
print(missing[["Year", "Month"]].to_string(index=False))

yearly_counts = df.groupby("Year")["Carbon Dioxide (ppm)"].count()

print(yearly_counts.loc[1958])
print(yearly_counts.loc[1964])

complete_years = yearly_counts[yearly_counts == 12]

complete_years = complete_years.loc[1958:2016]

print("Complete years:", len(complete_years))

yearly_max = df.groupby("Year")["Carbon Dioxide (ppm)"].max()
yearly_min = df.groupby("Year")["Carbon Dioxide (ppm)"].min()

yearly_range = yearly_max - yearly_min

print(yearly_range.head())

complete_yearly_range = yearly_range.loc[complete_years.index]

print(complete_yearly_range.head())
print("Number of complete years:", len(complete_yearly_range))

#--------------------------------------------

x = complete_yearly_range.index
y = complete_yearly_range.values

result = linregress(x, y)

print("X values:", x[:5])
print("Y values:", y[:5])

print("Slope:", result.slope)
print("P-value:", result.pvalue)
print("R-squared:", result.rvalue ** 2)

predicted_y = result.intercept + result.slope * x

residuals = y - predicted_y

print("First five residuals:", residuals[:5])

dw_result = durbin_watson(residuals)

print("Durbin-Watson:", dw_result)




plt.plot(complete_yearly_range.index, complete_yearly_range.values,marker="o", label="Observed annual range")
plt.plot(x, predicted_y, label="Linear regression" )
plt.legend()
plt.xlabel("Year")
plt.ylabel("Annual ppm (CO2 range)")
plt.title("CO2 range at Mauna Loa (1959-2016)")
plt.savefig("results/annual_co2_range.png", dpi=300, bbox_inches="tight")
plt.show()

plt.figure()
plt.scatter(x, residuals)
plt.axhline(y=0, linestyle="--")
plt.xlabel("Year")
plt.ylabel("Residual (ppm)")
plt.title("Regression Residuals Over Time")
plt.savefig("results/regression_residuals.png", dpi=300, bbox_inches="tight")
plt.show()

