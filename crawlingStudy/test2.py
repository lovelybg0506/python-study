import yfinance as yf
import matplotlib.pyplot as plt

# Create Ticker objects for Apple and Samsung stocks
apple_ticker = yf.Ticker("AAPL")
samsung_ticker = yf.Ticker("035720.KS")

# Get the current prices
apple_price = apple_ticker.info["currentPrice"]
samsung_price = samsung_ticker.info["currentPrice"]
print("Apple Current Price:", apple_price)
print("Samsung Current Price:", samsung_price)

# Get the 1-year historical data
apple_historical_data = apple_ticker.history(period="1y")
samsung_historical_data = samsung_ticker.history(period="1y")

# Plot the historical data side by side
fig, axs = plt.subplots(1, 2, figsize=(18, 6))
apple_historical_data["Close"].plot(ax=axs[0])
axs[0].set_title("AAPL 1-Year Stock Price Chart")
axs[0].set_xlabel("Date")
axs[0].set_ylabel("Closing Price")
samsung_historical_data["Close"].plot(ax=axs[1])
axs[1].set_title("Fucking Kakao 1-Year Stock Price Chart")
axs[1].set_xlabel("Date")
axs[1].set_ylabel("Closing Price")
plt.show()