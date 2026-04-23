def clean_data(df):
    print("Cleaning data...")

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.dropna()

    # Reset index
    df = df.reset_index(drop=True)

    print("Data cleaned")
    return df