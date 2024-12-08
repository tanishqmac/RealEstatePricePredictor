import matplotlib.pyplot as plt
import seaborn as sns

def analyze_data(data):
    if 'Price' not in data.columns or data.empty:
        print("Data is missing or 'Price' column not found. Skipping analysis.")
        return
    
    # Visualize the distribution of real estate prices
    plt.figure(figsize=(10, 6))
    plt.hist(data['Price'], bins=30, edgecolor='black')
    plt.title('Distribution of Real Estate Prices')
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.show()

    # Correlation heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(data.select_dtypes(include=['number']).corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.show()