from src.load_data import load_data
from src.clean_data import clean_data
from src.visualize import (
    gender_count_plot,
    math_score_hist,
    science_hist,
    heatmap
)
from src.insights import generate_insights

def main():
    # Load data
    df = load_data("data/dataset.csv")

    if df is None:
        return

    # Clean data
    df = clean_data(df)

    # Generate visualizations
    gender_count_plot(df)
    math_score_hist(df)
    science_hist(df)
    heatmap(df)

    # Generate insights
    generate_insights(df)

if __name__ == "__main__":
    main()