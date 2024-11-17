import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm

# Define the row limit based on LosingData
row_limit = 722891

# Load datasets with row limit for BTCUSDC.csv and WinningData.csv
losing_data = pd.read_csv('Crypto_Forex_Market_Analysis/Data/LosingData.csv', delimiter='|', 
                          names=['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume', 'X', 'Y', 'Z', 'ZZ'], 
                          skiprows=1)
winning_data = pd.read_csv('Crypto_Forex_Market_Analysis/Data/WinningData.csv', delimiter='|', 
                           names=['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume', 'X', 'Y', 'Z', 'ZZ'])

# Convert Timestamp to datetime for both datasets
winning_data['Date'] = pd.to_datetime(winning_data['Timestamp'], unit='s')
losing_data['Date'] = pd.to_datetime(losing_data['Timestamp'], unit='s')

# Summary statistics function, updated for volume calculations
def get_summary_stats(df, name):
    non_zero_volume = df[df['Volume'] > 0]
    summary = {
        'Dataset': name,
        'Earliest Date': df['Date'].min(),
        'Latest Date': df['Date'].max(),
        'Mean Price': df['Close'].mean(),
        'Median Price': df['Close'].median(),
        'Mode Price': df['Close'].mode()[0] if not df['Close'].mode().empty else None,
        'Std Dev Price': df['Close'].std(),
        'Variance Price': df['Close'].var(),
        'Min Price': df['Close'].min(),
        'Max Price': df['Close'].max(),
        'Total Volume': df['Volume'].sum(),
        'Average Volume': df['Volume'].mean(),
        'Median Volume': df['Volume'].median(),
        'Non-Zero Volume Count': len(non_zero_volume),
        'Average Volume (Excluding Zero)': non_zero_volume['Volume'].mean(),
        'Median Volume (Excluding Zero)': non_zero_volume['Volume'].median()
    }
    return pd.Series(summary)

# Calculate and print summary statistics for each dataset
winning_summary = get_summary_stats(winning_data, 'WinningData')
losing_summary = get_summary_stats(losing_data, 'LosingData')
summary_df = pd.DataFrame([winning_summary, losing_summary])
print(summary_df)

def plot_price_and_volume(df, title):
    # Aggregate data for plotting volume
    df['Date'] = pd.to_datetime(df['Date'])
    df_aggregated = df.resample('D', on='Date').agg({'Close': 'mean', 'Volume': 'sum'}).reset_index()

    # Plot Close Price
    plt.figure(figsize=(12, 8))
    plt.subplot(2, 1, 1)
    plt.plot(df['Date'], df['Close'], label='Close Price', color='blue')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(f"{title} - Price Over Time")
    plt.legend()
    plt.grid(True)

    # Plot Aggregated Volume
    plt.subplot(2, 1, 2)
    plt.bar(df_aggregated['Date'], df_aggregated['Volume'], label='Daily Volume', color='green', alpha=0.6)
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.title(f"{title} - Daily Aggregated Volume")
    plt.legend()
    plt.grid(True)

    # Save the figure
    filename = f'Crypto_Forex_Market_Analysis/Graphs/{title.replace(" ", "_")}_Price_Volume.png'
    plt.tight_layout()
    plt.savefig(filename)  # Save before showing
    print(f"Plot saved as {filename}")

    # Show the figure
    plt.show()
    plt.close()

# Plot both datasets with price and volume
plot_price_and_volume(winning_data, 'WinningData')
plot_price_and_volume(losing_data, 'LosingData')

# Perform OLS regression for WinningData (Price only)
X_winning = sm.add_constant(winning_data['Timestamp'])
ols_model_winning = sm.OLS(winning_data['Close'], X_winning).fit()
print("\nWinningData OLS Regression Summary (Price):")
print(ols_model_winning.summary())

# Perform OLS regression for LosingData (Price only)
X_losing = sm.add_constant(losing_data['Timestamp'])
ols_model_losing = sm.OLS(losing_data['Close'], X_losing).fit()
print("\nLosingData OLS Regression Summary (Price):")
print(ols_model_losing.summary())
