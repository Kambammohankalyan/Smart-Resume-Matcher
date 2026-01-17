import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def export_results(results, filename="ranking_report.csv"):
    """
    Saves the list of tuples [('Name', Score)] to a CSV file.
    """
    df = pd.DataFrame(results, columns=["Candidate Name", "Match Score"])
    df.to_csv(filename, index=False)
    print(f"📊 Report saved successfully: {filename}")

def plot_results(results):
    """
    Generates a visual bar chart of the candidate rankings.
    """
    df = pd.DataFrame(results, columns=["Candidate Name", "Match Score"])
    
    plt.figure(figsize=(10, 6))
    sns.set_theme(style="whitegrid")
    
    ax = sns.barplot(x="Match Score", y="Candidate Name", data=df, palette="viridis")
    
    plt.title("Candidate Relevance to Job Description", fontsize=16)
    plt.xlabel("Match Percentage (%)", fontsize=12)
    plt.ylabel("Candidate", fontsize=12)
    plt.xlim(0, 100) 

    for i in ax.containers:
        ax.bar_label(i, fmt='%.1f%%', padding=3)

    plt.tight_layout()
    plt.show()
