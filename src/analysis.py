def calculate_annual_range(data): # def create new function
    # Calculate the annual CO2 range
    yearly_max = data.groupby("Year")["Carbon Dioxide (ppm)"].max()  # Group CO2 values by year and find the highest value for each year
    yearly_min = data.groupby("Year")["Carbon Dioxide (ppm)"].min()  # Find the lowest CO2 value for each year
    yearly_range = yearly_max - yearly_min
    return yearly_range # Calculate the difference between the highest and lowest values

# in explore_data.py file we write that code that is similar with this but we alter df with data




def calculate_complete_year_ranges(data):
    # Count valid CO2 measurements for each year
    yearly_counts = data.groupby("Year")["Carbon Dioxide (ppm)"].count()

    # Find the different months available in each year
    yearly_months = data.groupby("Year")["Month"].agg(
        lambda months: set(months)
    )

    # Define the 12 valid months
    expected_months = set(range(1, 13))

    # Select years with 12 measurements and all correct months
    complete_years = yearly_counts[
        (yearly_counts == 12) &
        (yearly_months == expected_months)
    ].index

    # Keep only data from complete years
    complete_data = data[data["Year"].isin(complete_years)]

    # Calculate the annual CO2 ranges
    return calculate_annual_range(complete_data)

