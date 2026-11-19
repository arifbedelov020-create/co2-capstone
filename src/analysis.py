def calculate_annual_range(data): # def create new function
    # Calculate the annual CO2 range
    yearly_max = data.groupby("Year")["Carbon Dioxide (ppm)"].max()
    yearly_min = data.groupby("Year")["Carbon Dioxide (ppm)"].min()
    yearly_range = yearly_max - yearly_min
    return yearly_range

# in explore_data.py file we write that code that is similar with this but we alter df with data
