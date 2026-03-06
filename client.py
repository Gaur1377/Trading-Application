from binance.client import Client
from config import API_KEY,API_SECRET
from logger import logger

class BinanceFutureClient:

    def __init__(self):
        self.client = Client(API_KEY,API_SECRET)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/en/futures/BTCUSDT"

    def place_order(self,symbol,side,order_type,quantity,price=None):
        try:

            params = {
                "symbol" : symbol,
                "side":side,
                "type": order_type,
                "quantity":quantity
            }

            if order_type == "LIMIT":
                params["price"] = price
                params["timeInForce"] = "GTC"

            logger.info(f"Sending order request: {params}")

            response = self.client.futures_create_order(**params)

            logger.info(f"API Response: {response}")

            return response

        except Exception as e :
            logger.error(f"Order failed : {str(e)}")
            raise


