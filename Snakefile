rule all:
    input:
        "results/annual_co2_range.png",
        "results/regression_residuals.png",
        "results/annual_vs_seasonal_range.png"


rule generate_graphs:
    input:
        "data/archive.csv",
        "src/explore_data.py"
    output:
        "results/annual_co2_range.png",
        "results/regression_residuals.png",
        "results/annual_vs_seasonal_range.png"
    shell:
        "MPLBACKEND=Agg python src/explore_data.py"