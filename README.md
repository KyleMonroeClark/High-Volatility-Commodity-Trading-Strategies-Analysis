# Crypto and Forex Market Analysis

This project is an in-depth exploration of algorithmic trading techniques applied to cryptocurrencies and Forex markets. By using historical market data and rigorous analysis, it aims to identify and backtest profitable trading strategies while maintaining a focus on scalability and risk management.

---

## **Workflow**

### **1. Data Transformation**

The first step involved preparing the historical minute-level BTC-USDC candlestick data into two datasets:

- **WinningData:** Represents periods of sustained upward price movement.  
- **LosingData:** Represents periods of sustained downward price movement.  

These datasets were created by analyzing price trends and segmenting the data into distinct subsets based on performance criteria. This transformation allowed for a clear distinction between market conditions, enabling focused analysis for each scenario.

---

### **2. Baseline Analysis**

With the data segmented into WinningData and LosingData, an initial analysis was conducted to understand baseline behaviors. Metrics such as average price, standard deviation, and overall trends were calculated for each dataset to establish key insights into their characteristics.

**Key Analysis Metrics:**  
- Price distributions (mean, median, mode).  
- Volatility measures (standard deviation, range).  
- Regression analysis to identify overarching trends.  

_[Insert findings here once the analysis is complete.]_

---

### **3. Backtesting Trading Strategies**

The prepared datasets were then input into a backtesting program designed to simulate trades based on predefined technical indicators and rules. These simulations generated a **mock portfolio** that reflected hypothetical performance over multiple trades.  

Key trading indicators used during backtesting included:  
- Moving Averages  
- RSI (Relative Strength Index)  
- Stochastic RSI  

The program logged each trade, detailing:  
- **Timestamp** of the trade.  
- **Trigger reason** for buying or selling.  
- **Portfolio state** (cash and BTC levels).  
- **Cumulative trade metrics**, such as volume and portfolio value over time.  

These trade logs served as the foundation for subsequent analysis.

---

### **4. Trade Log Analysis**

Using the trade logs generated from backtesting, we performed detailed analyses to evaluate the strategy's effectiveness. This included:  
- Tracking **portfolio value** over time.  
- Reviewing the **frequency and outcomes** of buy/sell signals.  
- Analyzing the **reasons for trades**, identifying patterns or anomalies in trigger conditions.  
- Visualizing the **distribution of returns** and **performance consistency**.  

_[Insert findings here based on trade log analysis.]_

---

### **5. Project Scope and Future Work**

This project represents an iterative approach to building robust trading strategies. To date, the work has encompassed data preparation, exploratory analysis, backtesting, and trade log evaluation.  

**Planned Future Enhancements:**  
- **Indicator Optimization:** Fine-tuning the parameters for RSI, moving averages, and other indicators to maximize profitability.  
- **Risk Management Enhancements:** Incorporating advanced stop-loss techniques and volatility-based position sizing.  
- **Expanded Backtesting:** Testing across multiple assets and market conditions to ensure generalizability.  
- **Real-Time Implementation:** Transitioning the strategy to a live trading environment with automated decision-making.

---

This ongoing project reflects the dynamic nature of financial markets, emphasizing continuous learning and adaptation. By systematically analyzing data and refining strategies, it lays the groundwork for effective and scalable algorithmic trading.
