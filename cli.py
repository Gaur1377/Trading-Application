import argparse
from client import BinanceFutureClient

def Validate_inputs(args):
    if args.side not in ["BUY","SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if args.type not in ["MARKET","LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")

    if args.type == "LIMIT" and args.price is None:
        raise ValueError("LIMIT order require --price")

def main():

    parser = argparse.ArgumentParser(description="Binance Future CLI Trader")


    parser.add_argument("--symbol",required=True)
    parser.add_argument("--side",required=True)
    parser.add_argument("--type",required=True)
    parser.add_argument("--quantity",type=float,required=True)
    parser.add_argument("--price",type=float)

    args = parser.parse_args()

    try:

        Validate_inputs(args)

        client = BinanceFutureClient()

        print("\n===== ORDER REQUEST =====")
        print(f"Symbol   : {args.symbol}")
        print(f"Side     : {args.side}")
        print(f"Type     : {args.type}")
        print(f"Quantity : {args.quantity}")
        print(f"Price    : {args.price}")



        response = client.place_order(
            symbol=args.symbol,
            side= args.side,
            order_type=args.type,
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
