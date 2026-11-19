import pandas as pd # Help to read csv files
import matplotlib.pyplot as plt # HElp to create graphs
from scipy.stats import linregress # give us linear regression function from SciPy library 
from statsmodels.stats.stattools import durbin_watson # give DW function to evaluate autocorrelation in regression remains

df = pd.read_csv("data/archive.csv") #  df is Data Frame that looks like Excel

print(df.head()) # head() give us first 5 row

df.info() # give us general info about dataset

seasonal_component = df["Carbon Dioxide (ppm)"] - df["Seasonally Adjusted CO2 (ppm)"]
#seasonal_component shows repeated increasing and decreasing according to seasons of years
df["Seasonal Component"] = seasonal_component

print("Seasonal component:")
print(seasonal_component.head())

missing = df[df["Carbon Dioxide (ppm)"].isna()] # isna (NaN) operation determines blank values in selected column 
print(missing[["Year", "Month"]].to_string(index=False))

yearly_counts = df.groupby("Year")["Carbon Dioxide (ppm)"].count()
#count operation determines nonblank values counts in selected column

print(yearly_counts.loc[1958])
print(yearly_counts.loc[1964])
#loc operation is used to select info according to label in pandas

complete_years = yearly_counts[yearly_counts == 12] # it determines year that is TRUE(each month in year has values so it equals to 12)

complete_years = complete_years.loc[1958:2016]

print("Complete years:", len(complete_years))

yearly_max = df.groupby("Year")["Carbon Dioxide (ppm)"].max()# max() finds maximum monthly ppm
yearly_min = df.groupby("Year")["Carbon Dioxide (ppm)"].min()# min() finds minimmum monthly ppm
seasonal_max = df.groupby("Year")["Seasonal Component"].max()
seasonal_min = df.groupby("Year")["Seasonal Component"].min()

yearly_range = yearly_max - yearly_min
seasonal_range = seasonal_max - seasonal_min

print(yearly_range.head())# give us first 5 range
print("Seasonal range: ",seasonal_range.head())



complete_yearly_range = yearly_range.loc[complete_years.index]
#complete_years.index give us list of years that consist of nonblank values

complete_seasonal_range = seasonal_range.loc[complete_years.index]

print(complete_yearly_range.head())
print("Number of complete years:", len(complete_yearly_range))

print("Complete seasonal range:")
print(complete_seasonal_range.head())

range_difference = complete_yearly_range - complete_seasonal_range
#range_difference show how much differ CO2 differences that are calculated via 2 different method, from each other

print("Difference between ranges:")
print(range_difference.head())

seasonal_x = complete_seasonal_range.index
seasonal_y = complete_seasonal_range.values

seasonal_result = linregress(seasonal_x, seasonal_y)

print("Seasonal slope:", seasonal_result.slope)
print("Seasonal p-value:", seasonal_result.pvalue)
print("Seasonal R-squared:", seasonal_result.rvalue ** 2)




x = complete_yearly_range.index
y = complete_yearly_range.values # subtraction of max and min ppm for those years

result = linregress(x, y) # linregress operation adjusts obtained info to linear model

print("X values:", x[:5])
print("Y values:", y[:5])

print("Slope:", result.slope)
print("P-value:", result.pvalue)# P-value helps us understand how likely it is to get a result like ours just by chance, assuming there is no real relationship.
# In answer, The p-value is 0.00184 which is lower than 0.05.
# This means there is a statistically significant trend in the annual CO2 range if the regression assumptions are correct.
# However, this result does not explain why the CO2 range is changing.
print("R-squared:", result.rvalue ** 2)# rvalue is Pearson correlation coefficient

predicted_y = result.intercept + result.slope * x
#predicted_y is values that is calculated by linearmodel for each year
#result.intercept is constant coefficient of line
#result.slope is annual trend

residuals = y - predicted_y # residuals is difference between real observation and value of model

print("First five residuals:", residuals[:5])

dw_result = durbin_watson(residuals)
# ths function evaluates the relationship between successive regression residuals
print("Durbin-Watson:", dw_result)
#Close to 2: There may be little or no first-order autocorrelation
#Below 2: There may be positive autocorrelation
#Above 2: There may be negative autocorrelation

data_1964 = df[df["Year"] == 1964]

print(data_1964[["Month", "Carbon Dioxide (ppm)"]].head(5))

estimated_1964 = data_1964.copy() # copy() create another dataset totally similar with original one

estimated_1964["Carbon Dioxide (ppm)"] = estimated_1964["Carbon Dioxide (ppm)"].interpolate(method="linear")
#.interpolate(method="linear") guess nongiven values among the two measurement on straight line

print(estimated_1964[["Month", "Carbon Dioxide (ppm)"]].head(5))

original_range_1964 = data_1964["Carbon Dioxide (ppm)"].max() - data_1964["Carbon Dioxide (ppm)"].min()

interpolated_range_1964 = estimated_1964["Carbon Dioxide (ppm)"].max() - estimated_1964["Carbon Dioxide (ppm)"].min()

print("Original range 1964:", original_range_1964)
print("Interpolated range 1964:", interpolated_range_1964)


#First Graph - Annual ppm difference and regression
plt.plot(complete_yearly_range.index, complete_yearly_range.values,marker="o", label="Observed annual range") # plt.plot() combines info points via line
plt.plot(x, predicted_y, label="Linear regression" )# marker = "0" demonstrates every measurement with circle
plt.legend()# demonstrates name of lines
plt.xlabel("Year")
plt.ylabel("Annual ppm (CO2 range)")
plt.title("CO2 range at Mauna Loa (1959-2016)")
plt.savefig("results/annual_co2_range.png", dpi=300, bbox_inches="tight")
#plt.savefig() keeps graph as a file
#DPI is dots per inch
#bbox is Bounding Box (parameter) which help to manage area of the graph when we keep it as photo 
plt.show()

#Second Graph - Regression residuals over the time
plt.figure() # creates new graph
plt.scatter(x, residuals) # scatter crate plot
plt.axhline(y=0, linestyle="--")#axhline is horizontal line 
plt.xlabel("Year")
plt.ylabel("Residual (ppm)")
plt.title("Regression Residuals Over Time")
plt.savefig("results/regression_residuals.png", dpi=300, bbox_inches="tight")
plt.show()

#Third Graph - Annual vs. Seasonal CO₂ Range (1959–2016)
plt.figure()
plt.plot(complete_yearly_range.index, complete_yearly_range.values, label="Annual Range")
plt.plot(complete_seasonal_range.index, complete_seasonal_range.values, label="Seasonal Component Range")
plt.xlabel("Year")
plt.ylabel("CO₂ Range (ppm)")
plt.title("Annual vs. Seasonal CO₂ Range (1959–2016)")
plt.legend()
plt.savefig("results/annual_vs_seasonal_range.png", dpi=300, bbox_inches="tight")
plt.show()

