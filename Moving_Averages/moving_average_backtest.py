import pandas as pd
import os

# Set up directories
data_dir = 'Crypto_Forex_Market_Analysis/Data'
trade_log_dir = 'Crypto_Forex_Market_Analysis/Trade_Logs'
os.makedirs(trade_log_dir, exist_ok=True)

# Customize trade log filenames
trade_log_prefix = 'sma'  # Prefix for trade log filenames

# Load both data files
datasets = {
    'WinningData': pd.read_csv(f'{data_dir}/WinningData.csv', delimiter='|', 
                               names=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'col7', 'col8', 'col9', 'col10']),
    'LosingData': pd.read_csv(f'{data_dir}/LosingData.csv', delimiter='|', 
                              names=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'col7', 'col8', 'col9', 'col10'])
}

# Define initial parameters
initial_money = 1000  # Starting cash
ma_period = 10  # Moving average period
stop_loss = 0.10  # Stop-loss threshold (10%)

# Strategy execution function for a dataset
def execute_strategy(data, dataset_name):
    # Initialize variables
    money = initial_money
    btc = 0
    last_trade = 'sell'
    last_bought_price = 0
    iterations_since_trade = 0
    total_volume_since_trade = 0
    trade_log = []

    # Calculate the moving average (MA)
    data['moving_avg'] = data['close'].rolling(window=ma_period).mean()

    # Buy function
    def buy(index):
        nonlocal money, btc, last_trade, last_bought_price, iterations_since_trade, total_volume_since_trade
        current_price = data['close'][index]
        reason = "Moving averages indicator buy"
        
        if current_price > data['moving_avg'][index]:  # Buy signal
            btc = money / current_price
            last_bought_price = current_price
            last_trade = 'buy'
            trade_log.append((data['timestamp'][index], 'buy', current_price, iterations_since_trade, 
                              money, btc, reason, data['volume'][index], total_volume_since_trade))
            money = 0  # All money converted to BTC
            iterations_since_trade = 0  # Reset counter
            total_volume_since_trade = 0  # Reset volume tracker

    # Sell function
    def sell(index):
        nonlocal money, btc, last_trade, iterations_since_trade, total_volume_since_trade
        current_price = data['close'][index]

        # Regular sell condition
        if current_price < data['moving_avg'][index]:
            reason = "Moving averages indicator sell"
            money = btc * current_price
            btc = 0
            last_trade = 'sell'
            trade_log.append((data['timestamp'][index], 'sell', current_price, iterations_since_trade, 
                              money, btc, reason, data['volume'][index], total_volume_since_trade))
            iterations_since_trade = 0  # Reset counter
            total_volume_since_trade = 0  # Reset volume tracker
        
        # Stop-loss condition
        elif current_price <= last_bought_price * (1 - stop_loss):
            reason = "Stop-loss sell"
            money = btc * current_price
            btc = 0
            last_trade = 'sell'
            trade_log.append((data['timestamp'][index], 'sell-stoploss', current_price, iterations_since_trade, 
                              money, btc, reason, data['volume'][index], total_volume_since_trade))
            iterations_since_trade = 0  # Reset counter
            total_volume_since_trade = 0  # Reset volume tracker
        else:
            iterations_since_trade += 1  # Increment counter if no trade
            total_volume_since_trade += data['volume'][index]  # Add volume since no trade

    # Loop over data to execute buy/sell strategy
    for i in range(ma_period, len(data)):
        if last_trade == 'sell':
            buy(i)
        elif last_trade == 'buy':
            sell(i)
        else:
            total_volume_since_trade += data['volume'][i]  # Accumulate volume if no trade

    # Calculate final portfolio value
    final_money = money + (btc * data['close'].iloc[-1])  # Value of remaining BTC
    print(f"Final value for {dataset_name}: ${final_money:.2f}")

    # Save the trade log
    trade_log_df = pd.DataFrame(trade_log, columns=[
        'timestamp', 'trade_type', 'price', 'iterations_since_trade', 
        'cash_level', 'btc_level', 'reason', 'current_volume', 'total_volume_since_trade'
    ])
    filename = f'{trade_log_dir}/{trade_log_prefix}_{dataset_name}_trade_log.csv'
    trade_log_df.to_csv(filename, index=False)
    print(f"Trade log saved: {filename}")

# Run the strategy for both datasets
for name, dataset in datasets.items():
    execute_strategy(dataset, name)
