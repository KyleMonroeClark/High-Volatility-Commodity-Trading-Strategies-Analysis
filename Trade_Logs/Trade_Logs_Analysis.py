import pandas as pd
import matplotlib.pyplot as plt

# Enter trade log name here
trade_log_name = 'sma_LosingData_trade_log'  # Change this to the trade log you want to examine

# Load the specified trade log
trade_log_path = f'Crypto_Forex_Market_Analysis/Trade_Logs/{trade_log_name}.csv'
trade_log = pd.read_csv(trade_log_path)

# Add portfolio value and percentage change columns
trade_log['portfolio_value'] = trade_log['cash_level'] + (trade_log['btc_level'] * trade_log['price'])
trade_log['pct_change'] = trade_log['portfolio_value'].pct_change() * 100

# Filter out rows where portfolio value drops below 0.01 for the portfolio value graph
filtered_trade_log = trade_log[trade_log['portfolio_value'] >= 0.01]

# Histogram of iterations since trade
plt.figure(figsize=(10, 6))
plt.hist(trade_log['iterations_since_trade'], bins=20, edgecolor='black', color='skyblue')
plt.title('Histogram of Iterations Since Trade')
plt.xlabel('Iterations Since Trade')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig(f'Crypto_Forex_Market_Analysis/Graphs/{trade_log_name}_iterations_histogram.png')
plt.show()

# Simulated portfolio value over time (filtered)
plt.figure(figsize=(10, 6))
plt.plot(filtered_trade_log.index, filtered_trade_log['portfolio_value'], color='purple', label='Portfolio Value')
plt.title('Portfolio Value Over Time')
plt.xlabel('Trade Number')
plt.ylabel('Portfolio Value')
plt.legend()
plt.tight_layout()
plt.savefig(f'Crypto_Forex_Market_Analysis/Graphs/{trade_log_name}_portfolio_value.png')
plt.show()

# Count of each reason
reason_counts = trade_log['reason'].value_counts()

# Bar chart for reasons and portfolio changes
reason_summary = trade_log.groupby('reason')['pct_change'].mean()

# Plot average portfolio change by trade reason
plt.figure(figsize=(10, 6))
reason_summary.plot(kind='bar', color='coral', edgecolor='black')
plt.title('Average Portfolio Change by Trade Reason')
plt.xlabel('Reason for Trade')
plt.ylabel('Average Portfolio % Change')
plt.tight_layout()
plt.savefig(f'Crypto_Forex_Market_Analysis/Graphs/{trade_log_name}_reason_vs_change.png')
plt.show()

# Count bar chart
plt.figure(figsize=(10, 6))
reason_counts.plot(kind='bar', color='lightgreen', edgecolor='black')
plt.title('Count of Trades by Reason')
plt.xlabel('Reason for Trade')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig(f'Crypto_Forex_Market_Analysis/Graphs/{trade_log_name}_reason_counts.png')
plt.show()

# Summary statistics
print("Summary statistics for iterations since trade:")
print(trade_log['iterations_since_trade'].describe())

print("\nSummary of average portfolio changes by trade reason:")
print(reason_summary)

print("\nCounts of trades by reason:")
print(reason_counts)
