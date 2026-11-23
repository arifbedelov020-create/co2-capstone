import pandas as pd # Import pandas to create small datasets for testing
from src.analysis import calculate_annual_range, calculate_complete_year_ranges # Import the function we want to test

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


def test_incomplete_year_behavior():
    # Check how the function handles a year with only two measurements
    data = pd.DataFrame({
        "Year": [2000, 2000],
        "Carbon Dioxide (ppm)": [370, 375]
    })

    result = calculate_annual_range(data)

    # The current function calculates a range even for an incomplete year
    assert result.loc[2000] == 5


    
def test_complete_year_filter():
    # Create one complete year and one incomplete year
    data = pd.DataFrame({
        "Year": [2000] * 12 + [2001] * 2,
        "Month": list(range(1, 13)) + [1, 2],
        "Carbon Dioxide (ppm)": [
            370, 371, 372, 373, 374, 375,
            376, 377, 378, 379, 380, 381,
            390, 395
        ]
    })

    result = calculate_complete_year_ranges(data)

    # Year 2000 has 12 months, so its range is 11 ppm
    assert result.loc[2000] == 11

    # Year 2001 has only 2 months and must be excluded
    assert 2001 not in result.index



def test_duplicate_months():
    # A year with repeated months should not be treated as complete
    data = pd.DataFrame({
        "Year": [2000] * 12,
        "Month": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11],
        "Carbon Dioxide (ppm)": [
            370, 371, 372, 373, 374, 375,
            376, 377, 378, 379, 380, 381
        ]
    })

    result = calculate_complete_year_ranges(data)

    # Year 2000 must be excluded because December is missing
    assert 2000 not in result.index




def test_invalid_month_values():
    # Check if a year with invalid month numbers is excluded
    data = pd.DataFrame({
        "Year": [2000] * 12,
        "Month": list(range(2, 14)),
        "Carbon Dioxide (ppm)": [
            370, 371, 372, 373, 374, 375,
            376, 377, 378, 379, 380, 381
        ]
    })

    result = calculate_complete_year_ranges(data)

    # Month 13 is invalid, so year 2000 must be excluded
    assert 2000 not in result.index
