from binance.client import Client
from binance.enums import *
from logger import logger

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
        logger.info("Binance client initialized in testnet mode")

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side.lower() == 'buy' else SIDE_SELL,
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )
            logger.info(f"Market Order Response: {order}")
            return order
        except Exception as e:
            logger.error(f"Market order error: {e}")
            return {'error': str(e)}

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side.lower() == 'buy' else SIDE_SELL,
                type=ORDER_TYPE_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=str(price)
            )
            logger.info(f"Limit Order Response: {order}")
            return order
        except Exception as e:
            logger.error(f"Limit order error: {e}")
            return {'error': str(e)}

    def place_stop_limit_order(self, symbol, side, quantity, stop_price, limit_price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side.lower() == 'buy' else SIDE_SELL,
                type=ORDER_TYPE_STOP,
                quantity=quantity,
                stopPrice=str(stop_price),
                price=str(limit_price),
                timeInForce=TIME_IN_FORCE_GTC
            )
            logger.info(f"Stop-Limit Order Response: {order}")
            return order
        except Exception as e:
            logger.error(f"Stop-limit order error: {e}")
            return {'error': str(e)}
