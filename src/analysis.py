def calculate_annual_range(data): # def create new function
    # Calculate the annual CO2 range
    yearly_max = data.groupby("Year")["Carbon Dioxide (ppm)"].max()  # Group CO2 values by year and find the highest value for each year
    yearly_min = data.groupby("Year")["Carbon Dioxide (ppm)"].min()  # Find the lowest CO2 value for each year
    yearly_range = yearly_max - yearly_min
    return yearly_range # Calculate the difference between the highest and lowest values

# in explore_data.py file we write that code that is similar with this but we alter df with data
