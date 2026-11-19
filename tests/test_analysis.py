import pandas as pd
from src.analysis import calculate_annual_range

def test_annual_range():
    # Create a small dataset
    # Call calculate_annual_range()
    # Check the expected result using assert
    data = pd.DataFrame({
        "Year": [2000, 2000, 2000],
        "Carbon Dioxide (ppm)": [370, 375, 372]
        })
    
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
