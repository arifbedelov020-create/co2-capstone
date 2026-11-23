rule all: # Define the final output files needed for the project
    input:
        "results/annual_co2_range.png",
        "results/regression_residuals.png",
        "results/annual_vs_seasonal_range.png"


rule generate_graphs: # Run the Python analysis to generate the CO2 graphs
    input:  # These files are required to run the analysis
        "data/archive.csv",
        "src/explore_data.py"
    output:  # These graphs should be created by the Python script
        "results/annual_co2_range.png",
        "results/regression_residuals.png",
        "results/annual_vs_seasonal_range.png"
    shell:  # Run the analysis without opening graph windows
        "MPLBACKEND=Agg python src/explore_data.py"