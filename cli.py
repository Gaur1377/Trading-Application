import argparse
from client import BinanceFutureClient

def Validate_inputs(args):
    if args.side not in ["BUY","SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if args.order_type not in ["MARKET","LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")

    if args.order_type == "LIMIT" and args.price is None:
        raise ValueError("LIMIT order require --price")

def main():

    parser = argparse.ArgumentParser(description="Binance Future CLI Trader")

    parser.add_argument("--symbol", required=True, help="Trading symbol, e.g., BTCUSDT")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"], help="BUY or SELL")
    parser.add_argument("--order_type", required=True, choices=["MARKET", "LIMIT"], help="MARKET or LIMIT order type")
    parser.add_argument("--quantity", type=float, required=True, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price for LIMIT orders")

    args = parser.parse_args()

    try:

        Validate_inputs(args)

        client = BinanceFutureClient()

        print("\n===== ORDER REQUEST =====")
        print(f"Symbol   : {args.symbol}")
        print(f"Side     : {args.side}")
        print(f"Type     : {args.order_type}")
        print(f"Quantity : {args.quantity}")
        print(f"Price    : {args.price}")



        response = client.place_order(
            symbol=args.symbol,
            side= args.side,
            order_type=args.order_type,
            quantity=args.quantity,
            price=args.price
        )

        print("\n===== ORDER RESPONSE =====")
        print(f"Order ID      : {response.get('orderId')}")
        print(f"Status        : {response.get('status')}")
        print(f"Executed Qty  : {response.get('executedQty')}")
        print(f"Avg Price     : {response.get('avgPrice')}")

        print("\n✅ Order placed successfully")

    except Exception as e:
        print("\n Order failed:", str(e))

if __name__ == "__main__":
    main()
