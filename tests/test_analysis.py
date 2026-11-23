import pandas as pd # Import pandas to create small datasets for testing
from src.analysis import calculate_annual_range # Import the function we want to test

def test_annual_range():
    # Create a small dataset
    # Call calculate_annual_range()
    # Check the expected result using assert
    data = pd.DataFrame({ # Create a small dataset with three CO2 values for the year 2000
        "Year": [2000, 2000, 2000],
        "Carbon Dioxide (ppm)": [370, 375, 372]
        })
    # The highest value is 375 and the lowest is 370
    # Check if the function returns the expected difference of 5 ppm
    assert calculate_annual_range(data).loc[2000] == 5


def test_multiple_years():
    data = pd.DataFrame({
        "Year": [2000, 2000, 2001, 2001],
        "Carbon Dioxide (ppm)": [370, 375, 380, 387]
    })

    result = calculate_annual_range(data)

    assert result.loc[2000] == 5
    assert result.loc[2001] == 7


def test_missing_values():
    data = pd.DataFrame({
        "Year": [2000, 2000, 2000, 2000],
        "Carbon Dioxide (ppm)": [370, None, 375, 372]
    })
    # Pandas does not consider NaN values according to min() and max() standarts

    result = calculate_annual_range(data)

    assert result.loc[2000] == 5


def test_same_co2_values():
    # Check if the annual range is zero when all CO2 values are equal
    data = pd.DataFrame({
        "Year": [2000, 2000, 2000],
        "Carbon Dioxide (ppm)": [370, 370, 370]
    })

    result = calculate_annual_range(data)

    assert result.loc[2000] == 0


def test_single_measurement():
    # Check the result when a year has only one CO2 measurement
    data = pd.DataFrame({
        "Year": [2000],
        "Carbon Dioxide (ppm)": [375]
    })

    result = calculate_annual_range(data)

    assert result.loc[2000] == 0


def test_unsorted_years():
    # Check if the function works when years are not in order
    data = pd.DataFrame({
        "Year": [2001, 2000, 2001, 2000],
        "Carbon Dioxide (ppm)": [385, 370, 390, 378]
    })

    result = calculate_annual_range(data)

    # Check the difference between maximum and minimum CO2
    assert result.loc[2000] == 8
    assert result.loc[2001] == 5
