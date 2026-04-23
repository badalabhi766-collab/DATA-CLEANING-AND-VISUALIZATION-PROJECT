def generate_insights(df):
    print("\n--- Insights ---")

    print("Average Math Score:", df['math_score'].mean())
    print("Average Science Score:", df['science_score'].mean())
    print("Average English Score:", df['english_score'].mean())

    print("\nTop Math Score:", df['math_score'].max())
    print("Lowest Math Score:", df['math_score'].min())