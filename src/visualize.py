import os
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure output folder exists
os.makedirs("output", exist_ok=True)

def gender_count_plot(df):
    df['gender'].value_counts().plot(kind='bar')
    plt.title("Gender Count")
    plt.savefig("output/gender_count.png")
    plt.close()

def math_score_hist(df):
    plt.hist(df['math_score'])
    plt.title("Math Scores Distribution")
    plt.savefig("output/math_scores.png")
    plt.close()

def science_hist(df):
    plt.hist(df['science_score'])
    plt.title("Science Scores Distribution")
    plt.savefig("output/science_hist.png")
    plt.close()

def heatmap(df):
    sns.heatmap(df.corr(numeric_only=True), annot=True)
    plt.title("Correlation Heatmap")
    plt.savefig("output/heatmap.png")
    plt.close()