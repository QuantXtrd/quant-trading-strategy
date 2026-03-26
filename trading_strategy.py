def run_strategy(prices, short_window=3, long_window=5):
    position = 0
    buy_price = 0
    total_profit = 0
    trades = []

    for i in range(long_window - 1, len(prices)):
        short_ma = sum(prices[i - short_window + 1:i + 1]) / short_window
        long_ma = sum(prices[i - long_window + 1:i + 1]) / long_window
        current_price = prices[i]

        if short_ma > long_ma and position == 0:
            position = 1
            buy_price = current_price
            trades.append(f"BUY at {current_price}")

        elif short_ma < long_ma and position == 1:
            position = 0
            profit = current_price - buy_price
            total_profit += profit
            trades.append(f"SELL at {current_price} | Profit: {profit}")

    if position == 1:
        profit = prices[-1] - buy_price
        total_profit += profit
        trades.append(f"FINAL SELL at {prices[-1]} | Profit: {profit}")

    return trades, total_profit


if __name__ == "__main__":
    prices = [100, 102, 101, 104, 107, 106, 109, 111, 108, 112, 115, 113]

    trades, profit = run_strategy(prices)

    print("Trades:")
    for trade in trades:
        print(trade)

    print("\nTotal Profit:", profit)
