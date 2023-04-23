import yfinance as yf
import matplotlib.pyplot as plt

# Create a Ticker object for Apple stock
ticker = yf.Ticker("AAPL")

# Get the current price
current_price = ticker.info["currentPrice"]
# print("Current Price:", current_price)
# print("Current Price: $", stock_info["currentPrice"])
# print("Market Cap: ", stock_info["marketCap"])
# print("PE Ratio: ", stock_info["trailingPE"])
# print("Dividend Yield: ", stock_info["dividendYield"])

# Get the 1-year historical data
historical_data = ticker.history(period="2y")

# Plot the historical data
historical_data["Close"].plot(figsize=(12,6))
plt.title("AAPL 1-Year Stock Price Chart")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.show()
