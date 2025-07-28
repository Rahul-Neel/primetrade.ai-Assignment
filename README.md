This is a Binance Testnet-based trading bot developed for the PrimeTrade.ai assignment. The bot allows you to place various types of crypto orders (Market, Limit, Stop-Limit) using Binance's official API on the testnet environment.

---

Features

- ✅ Supports the following order types:
  - Market Order
  - Limit Order
  - Stop-Limit Order
- 🔒 Secure handling of API credentials using `.env`
- 📈 Trade logs stored in a local file (`logs/`)
- 🧪 Testnet trading using [Binance Testnet](https://testnet.binancefuture.com/)
- 📂 Clean project structure with logging and error handling

---

## ⚙️ Technologies Used

- `python-binance` (Binance API wrapper)
- `python-dotenv` (for managing environment variables)
- `logging` (to store bot activity logs)



HOW TO RUN THE BOT 
##  create virtual Environment 
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate

## Install Dependencies
pip install -r requirements.txt

## Run the bot
python main.py
