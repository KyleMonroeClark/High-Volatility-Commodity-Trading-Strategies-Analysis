# Crypto and Forex Market Analysis

This project explores algorithmic trading techniques applied to highly volatile markets, focusing on cryptocurrencies (primarily Bitcoin) and Forex. By leveraging historical market data and advanced technical indicators, the goal is to develop scalable and risk-managed trading strategies that can generate small, consistent, compounding returns. While the project as a whole evaluates various strategies and indicators, this specific segment showcases an early-stage trading strategy that uses a basic technical indicator (Simple Moving Average) alongside a stop loss for risk management.

This analysis is part of a larger effort to explore combinations of technical indicators, such as Relative Strength Index (RSI), Stochastic RSI, and Bayesian regression, alongside real-time market data. The overarching goal is to build models that can dynamically adjust to changing market conditions and maximize long-term profitability, independent of large price movements typical of cryptocurrencies and Forex.

---

## **Workflow**

### **1. Data Transformation**

The initial step in this project was to prepare historical candlestick data sourced from Binance USA. Since Bitcoin prices have shown dramatic upward trends over time, directly using this data in a strategy could introduce biases towards long positions. To overcome this, the data was segmented into two subsets:

- **WinningData:** Represents periods of sustained upward price movement.  
- **LosingData:** Represents periods of sustained downward price movement.  

The segmentation was done manually by visually identifying periods in the price data that exhibited clear trends. Although this approach served its purpose for this initial demonstration, future iterations will employ algorithmic methods to segment the data more accurately. 

This transformation allowed for easy adjustments to be made in the backtesting phase. 

**Note**: This analysis currently uses only Bitcoin (BTC) data. The larger project has expanded to include multiple cryptocurrencies and Forex markets to evaluate which indicators perform best under various market conditions.

---

### **2. Initial Data Analysis**

After segmenting the data into WinningData and LosingData, the next step was to perform some exploratory analysis to better understand the characteristics of these datasets.

#### Price Trends and OLS Regression

The first analysis conducted was an Ordinary Least Squares (OLS) regression to identify the general trend of prices over time in both datasets.

- **WinningData OLS Regression Results**:
  - **R-squared**: 0.277 (Indicating a weak positive correlation between price and time)
  - **Coefficient for `Timestamp`**: 0.0001 (A slight upward movement over time)

- **LosingData OLS Regression Results**:
  - **R-squared**: 0.343 (Indicating a slightly stronger negative correlation)
  - **Coefficient for `Timestamp`**: -0.0006 (A slight downward movement over time)

The regression analysis of both datasets showed clear trends:
- **WinningData** had a weak but consistent upward trend.
- **LosingData** exhibited a stronger downward trend.

#### Price and Volume Analysis

In addition to price trends, trading volume was also examined. The price and volume graphs revealed a pattern where periods of high volume corresponded with higher volatility in price movements. This insight could be useful for future strategies, but the current analysis does not incorporate volume directly into the trading strategy. 

Graphs for both datasets were saved as:
- ![WinningData Price and Volume](./WinningData_Price_Volume.png)
- ![LosingData Price and Volume](./LosingData_Price_Volume.png)
- ![LosingData Price Over Time with Regression](./LosingData_Price_Over_Time_with_Regression.png)
- ![WinningData Price Over Time with Regression](./WinningData_Price_Over_Time_with_Regression.png)

These visualizations show the relationship between price and volume, providing additional context for understanding market behavior during these periods.

---

### **3. Backtesting Trading Strategy: Moving Average**

In this step, we implemented a simple backtesting strategy based on the **Simple Moving Average (SMA)**, a common technical indicator used in trading. The idea behind this strategy is simple: when the price of Bitcoin is above the moving average, a buy signal is triggered, and when the price drops below the moving average, a sell signal is triggered. Additionally, we incorporated a **stop-loss** mechanism to limit potential losses by automatically selling if the price falls by more than 10% from the most recent purchase price.

#### **Strategy Details**
- **Indicator Used**: Simple Moving Average (SMA) with a 10-minute period. This means that at each minute, the SMA is calculated based on the average closing price of the previous 10 minutes.
- **Buy Condition**: If the price is above the SMA, the strategy will buy.
- **Sell Condition**: If the price is below the SMA, or if the price drops below the last purchase price by more than 10% (stop-loss), the strategy will sell.

#### **Trade Log and Portfolio Value**

The backtest was run on both the **WinningData** and **LosingData** datasets, and a detailed trade log was generated for each dataset. The trade log contains the following key information for each trade:
- **Timestamp** of the trade.
- **Trade Type** (buy, sell, or stop-loss).
- **Price** at the time of the trade.
- **Reason** for the trade (either the moving average signal or stop-loss condition).
- **Cash and BTC levels** at the time of the trade.
- **Volume data** for the trade.

After running the backtest, the final portfolio value was calculated based on the remaining cash and any Bitcoin holdings at the end of the data period.

#### **Limitations of the Strategy**

As mentioned earlier, this backtest used only a **Simple Moving Average (SMA)**, which is a basic indicator and does not account for more advanced strategies like combining multiple indicators. The SMA-based strategy is quite simplistic, and while it serves as a proof of concept for the broader project, it is unlikely to be effective in real-world trading conditions without further optimization. 

Additionally, this backtest does not consider trading **volume**, which can be a critical factor in determining the strength of price movements. Future iterations will incorporate volume-based indicators and more sophisticated strategies.

#### **Results**

The backtesting process produced a **trade log** for each dataset, and we were able to evaluate the overall performance of the strategy. The final value of the portfolio was calculated after all trades were executed, and the strategy was able to demonstrate its potential for generating small, consistent returns. However, the results are highly dependent on the market conditions during the periods analyzed (the **WinningData** and **LosingData**), and future backtests will aim to include more diverse market conditions for better generalization.

You can find the trade logs for each dataset saved as CSV files:
- *WinningData_trade_log.csv*
- *LosingData_trade_log.csv*

These logs provide detailed information on each trade, which will help in evaluating the strategy's performance and making adjustments for future iterations.

---

### **4. Trade Log Analysis**

After executing the backtest strategy, the next step was to analyze the generated **trade logs** to evaluate the effectiveness of the strategy and identify any key patterns or insights. The trade logs contain valuable information about the frequency of trades, portfolio value changes, and the reasons for each trade. The following analysis was conducted on the **LosingData** trade log to assess the strategy's performance and to identify potential areas for improvement.

#### **Key Findings from the Trade Log Analysis**

1. **Frequency of Trades**:
    - **Histogram of Iterations Since Trade**: The histogram reveals that the majority of trades occurred within **10 minutes** of each other, with most trades being executed very frequently. This suggests that the moving average strategy is overly sensitive, triggering buy and sell signals too often. Given that we lost money over time, this could indicate that the strategy may be trading too frequently, capturing only small price fluctuations, and ultimately resulting in negative returns.

    ![Iterations Since Trade](./sma_LosingData_trade_log_iterations_histogram.png)

2. **Portfolio Value Over Time**:
    - **Simulated Portfolio Value**: Both the **WinningData** and **LosingData** portfolio value graphs showed a **decline** in portfolio value over time, reinforcing the idea that the strategy is not profitable under the given conditions. The **LosingData** dataset still had some residual value left at the end, while the **WinningData** dataset lost all its value, suggesting that this strategy may have performed marginally better during periods of downward price movement. However, the general trend indicates that the strategy is overall unprofitable, which was expected given the simplicity of the approach.

    ![Portfolio Value](./sma_LosingData_trade_log_portfolio_value.png)

3. **Reasons for Trades**:
    - **Reasons and Portfolio Changes**: The **reason for trade** analysis confirmed that the **Moving Averages Indicator** was the only condition triggering buy and sell actions, with no stop-loss triggers occurring. The strategy was entirely driven by the moving average crossing signals, which means that the stop-loss feature was not needed because no prices ever dropped enough to activate the stop-loss condition.

    - The **average portfolio change by trade reason** showed a **100% gain** for buy trades, and a **-50% loss** for sell trades, which is a direct result of the trading logic: when a buy occurs, it is followed by a sell that tends to be significantly lower, often causing a large drop in portfolio value.

    ![Reason vs. Portfolio Change](./sma_LosingData_trade_log_reason_vs_change.png)

    - **Counts of Trades by Reason**: The count of trades shows that **66840 buy** trades and **66840 sell** trades were executed, suggesting that every buy signal was followed by a sell signal, but no stop-loss condition was triggered.

    ![Reason Counts](./sma_LosingData_trade_log_reason_counts.png)

4. **Limitations and Insights**:
    - **Overfitting and Data Issues**: Given the small scale and basic nature of the strategy, it's important to note that this is primarily a **proof of concept**. The data used for segmentation was manually eyeballed, which could introduce significant biases. Additionally, this backtest only used the **Simple Moving Average (SMA)** and did not incorporate other potentially useful indicators, such as volume or momentum-based indicators.
    
    - **Stop-Loss Effectiveness**: The stop-loss mechanism was never triggered, which may indicate that the stop-loss level (set at 10%) is too **lenient**. In a real-world scenario, a more aggressive or dynamic stop-loss strategy might be necessary to limit losses during periods of high volatility.

    - **Potential for Improvement**: Future iterations will aim to improve the strategy by:
        - Incorporating more complex indicators or combinations of indicators.
        - Adjusting the stop-loss threshold to better protect against sudden market swings.
        - Expanding the backtest to include more assets and diverse market conditions.

#### **Summary Statistics**

Here are some summary statistics that provide insight into the performance and behavior of the trades:

- **Iterations Since Trade**:
    - **Average**: 2.11 minutes
    - **Standard Deviation**: 4.10 minutes
    - **Max**: 76 minutes
    - Most trades occurred very quickly, within the first few minutes after the previous trade.

- **Average Portfolio Changes by Trade Reason**:
    - **Buy**: +100%
    - **Sell**: -50.01%

- **Counts of Trades by Reason**:
    - **Buy**: 69,884
    - **Sell**: 69,883

While the strategy showed that frequent trading (based on moving averages) is the main contributor to trades, it also showed that this approach did not lead to positive returns in the backtest.

This trade log analysis emphasizes the limitations of using a **Simple Moving Average (SMA)** strategy on its own, especially in highly volatile markets like cryptocurrency. While the strategy was able to demonstrate the core principles of backtesting, it also highlighted the need for more sophisticated models, better risk management, and adjustments to prevent overtrading. This is an area for future refinement as we continue to evolve the broader trading project.

---

### **5. Project Scope and Reflections**

This project started as an exploration of algorithmic trading in volatile markets like cryptocurrencies, with the goal of identifying and backtesting simple strategies that could scale over time. We've gone through multiple stages, including data preparation, initial exploratory analysis, strategy development, and backtesting. Using a basic moving average crossover strategy, we tested the effectiveness of a simple, frequent trading model based on historical price data.

**What We Found:**  
The backtest results highlighted some key insights:
- **Excessive Frequency of Trades:** The strategy executed trades too frequently, often within a few minutes, leading to high transaction costs and minimal profits. This was expected given the simplicity of the model and the lack of more advanced risk management tools.
- **Strategy Performance:** Both the "winning" and "losing" datasets showed a loss in portfolio value, with the winning data eventually depleting all funds, and the losing data retaining some value. This suggests that the simple moving average strategy, while not profitable overall, may have had better performance in downtrending markets—though this could also be due to issues with the data segmentation.
- **Stop-Loss Limitations:** The stop-loss condition didn’t come into play often enough to be meaningful, pointing to a possible gap in the strategy’s risk management.

These findings were in line with expectations, given the simplicity of the strategy used. The results confirmed that more complex models, incorporating additional indicators and more sophisticated risk management strategies, are likely needed for more reliable, profitable outcomes.

**Improvements and Ongoing Development:**  
While this portion of the project serves as a proof of concept, it has already led to several improvements on my end:
- **Indicator Expansion:** The initial strategy only used moving averages, but I have expanded the project to incorporate more complex indicators like RSI, stochastic RSI, and Bayesian regression to improve decision-making.
- **Risk Management Enhancements:** I've implemented more robust stop-loss mechanisms linked to market volatility and active portfolio management. In future versions, I plan to explore dynamic position sizing and more advanced risk controls.
- **Multi-Asset Testing:** The scope has been broadened to include multiple cryptocurrencies, allowing for cross-market strategies, and I'm now exploring Forex trading as well. This will help determine if the strategy can be generalized to other volatile markets.
- **Live Implementation:** While this analysis focused on backtesting, I have been working toward transitioning the strategy to real-time trading with automated decision-making, leveraging live market data.

---

This project has been a valuable exercise in developing algorithmic trading strategies, and the lessons learned will continue to shape future iterations. As the model evolves, it will increasingly rely on more sophisticated techniques and real-time adjustments to adapt to the unpredictable nature of financial markets.
