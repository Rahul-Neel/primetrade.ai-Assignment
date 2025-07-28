from bot import BasicBot
from getpass import getpass

print("Welcome to Binance Testnet Trading Bot 🤖")
print("Supported order types: market, limit, stop_limit")

# Input your Binance Futures Testnet credentials
api_key = input("Enter your Binance API Key: ")
api_secret = getpass("Enter your Binance API Secret: ")

bot = BasicBot(api_key, api_secret, testnet=True)

while True:
    symbol = input("Enter trading symbol (e.g., BTCUSDT): ").strip().upper()
    side = input("Enter side (buy/sell): ").strip().lower()
    order_type = input("Enter order type (market/limit/stop_limit): ").strip().lower()
    quantity = float(input("Enter quantity: ").strip())

    if order_type == "market":
        response = bot.place_market_order(symbol, side, quantity)
    elif order_type == "limit":
        price = float(input("Enter limit price: ").strip())
        response = bot.place_limit_order(symbol, side, quantity, price)
    elif order_type == "stop_limit":
        stop_price = float(input("Enter stop price: ").strip())
        confirm1 = input(f"Confirm stop-limit order to {side} {quantity} {symbol} with stop price {stop_price}? (y/n): ")
        if confirm1.lower() != 'y':
            continue
        limit_price = float(input("Enter limit price (the price at which order will be placed when stop is hit): ").strip())
        confirm2 = input(f"Confirm stop-limit order to {side} {quantity} {symbol} with stop price {stop_price} and limit price {limit_price}? (y/n): ")
        if confirm2.lower() != 'y':
            continue
        response = bot.place_stop_limit_order(symbol, side, quantity, stop_price, limit_price)
    else:
        print("Invalid order type.")
        continue

    print("Order Response:", response)

    repeat = input("Place another order? (y/n): ").strip().lower()
    if repeat != 'y':
        break
