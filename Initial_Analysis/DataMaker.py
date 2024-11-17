import pandas as pd

# Load BTCUSDC.csv with a row limit and specific column names
row_limit = 722891
btc_data = pd.read_csv('Crypto_Forex_Market_Analysis/Data/BTCUSDC.csv', delimiter='|', 
                       names=['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume', 'X', 'Y', 'Z', 'ZZ'], 
                       nrows=row_limit)

# Save as WinningData.csv in the Data folder
btc_data.to_csv('Crypto_Forex_Market_Analysis/Data/WinningData.csv', sep='|', index=False, header=False)
