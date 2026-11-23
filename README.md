# co2-capstone

## Project Overview 

This project analyzes changes in atmospheric CO2 levels using monthly CO2 data from Mauna Loa. The study focuses on the period from 1958 to 2016. The main goal is to investigate these changes through annual difference between the highest and lowest CO2 levels.

## Research Question

How has the annual difference between the highest and lowest atmospheric CO2 levels at Mauna Loa changed from 1958 to 2016?

## Dataset

This project uses monthly atmospheric CO2 data measured at Mauna Loa, Hawaii. The dataset was downloaded from Kaggle and includes data from 1958 to 2017. However, we focus on the periiod from 1958-2016 because of the missing values of data from 2017.  Some earlier years also consist of missing measurements, so only years with all 12 monthly values are included in the main regression analysis.

Dataset source: https://www.kaggle.com/ucsandiego/carbon-dioxide/home

## Methods

We used Python and Pandas to analyze monthly CO2 measurements. Firstly, we identified missing values and selected years with 12 valid monthly measurements. Next, we calculated the annual CO2 range by subtracting the lowest monthly value from the highest monthly value for each year.

We used linear regression to examine how the annual range changed over time. We also analyzed regression residuals and calculated the Durbin-Watson statistic. Finally, we compared the annual CO2 range with the range of the seasonal component derived from the dataset's seasonally adjusted measurements.

## Key Results

The analysis included 57 years with complete monthly CO2 measurements. Linear regression showed a small positive trend in the annual CO2 range, with an estimated increase of 0.0121 ppm per year.

The p-value was approximately 0.00184, suggesting that the trend is statistically significant under the assumptions of the regression model. However, the R-squared value was only 0.163, meaning that the model explained about 16.3% of the variation in the annual CO2 range.

The Durbin-Watson statistic was approximately 1.78. This result does not provide enough evidence on its own to confirm that the regression residuals are independent.


We also examined the seasonal component of CO2 by subtracting the seasonally adjusted values from the original measurements. The regression showed a positive slope of approximately 0.0220 ppm per year, with an R-squared value close to 1.

However, this result should be interpreted carefully. The seasonal component was calculated using values already adjusted by the data provider. Therefore, the very strong linear relationship may be influenced by the adjustment method and should not be treated as independent proof of increasing seasonal variation.
## Project Structure

CO2-Capstone/
├── data/
│   └── archive.csv
├── results/
│   ├── annual_co2_range.png
│   ├── regression_residuals.png
│   └── annual_vs_seasonal_range.png
├── src/
│   ├── analysis.py
│   └── explore_data.py
├── tests/
│   └── test_analysis.py
├── Snakefile
├── requirements.txt
├── .gitignore
└── README.md

The `data` folder contains the original CO2 dataset. The `src` folder contains the Python scripts used for data analysis. The `tests` folder includes tests to check some calculations. The `results` folder stores the generated graphs.

The `Snakefile` automates the process of creating graphs, while `requirements.txt` lists the Python packages needed for the project. The `.gitignore` file specifies which files Git should ignore.

## Installation

This project requires Python and several Python libraries. Follow these steps to set up the project.

1. Clone the Github repository:
   git clone https://github.com/arifbedelov020-create/co2-capstone.git
   cd co2-capstone

2. Create a virtual environment for Python:
   python3 -m venv .venv
   source .venv/bin/activate

3. Install the required Python data:
   python -m pip install -r requirements.txt

4. Install Snakemake:
   python -m pip install snakemake

5. Download the dataset:
   Download archive.csv from:
   https://www.kaggle.com/ucsandiego/carbon-dioxide/home
   Place the file inside the data folder.

   Note: These commands are intended for Ubuntu/Linux. Windows users need different commands to activate the virtual environment. Snakemake was tested using WSL Ubuntu.


## How to Run

The project can be run using Python, Pytest, and Snakemake.

1. Run automated tests:
   python -m pytest tests/ -v
This command runs the tests in the tests folder to check the annual CO2 range calculations.

2. Run the CO2 analysis directly:
   MPLBACKEND=Agg python src/explore_data.py
This command runs the Python analysis and generates the graphs.

3. Run the Snakemake workflow:
First, check which tasks Snakemake plans to execute:
   snakemake --cores 1 --dry-run
Then run the workflow:
   snakemake --cores 1
Snakemake automatically generates the required graphs when the input files have changed or the output files are missing.

4. View th results:
The generated graphs are saved in the results folder:

1 - annual_co2_range.png
2 - regression_residuals.png
3 - annual_vs_seasonal_range.png

Note: These commands are intended for Ubuntu/Linux or WSL Ubuntu with the required packages installed and the virtual environment activated.

## Limitations

The study has several limitations. First, some monthly CO2 measurements are missing from the dataset. The main regression analysis uses only 57 years with complete monthly records excluding 1958 and 1964 from the period ending in 2016.

Second, the difference between the highest and lowest monthly CO2 values does not measure seasonal changes perfectly because the long-term increase in CO2 can also affect this difference.

Third, the seasonal component was calculated using the dataset's existing seasonally adjusted values. Therefore, the results depend on the adjustment method used by the data provider.

Finally, linear regression describes trends in the data but does not prove what caused these changes.


*Missing Data and Interpolation*

Some CO2 measurements were missing in 1964, especially from February to April. We used linear interpolation to estimate these missing values based on the measurements from January and May.

The annual CO2 range remained approximately 5.55 ppm before and after interpolation. However, interpolation cannot guarantee that the estimated values match the real measurements. For this reason, 1964 was excluded from the main regression analysis, and interpolation was used only as an additional check.