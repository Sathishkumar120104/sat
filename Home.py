import logging
from kiteconnect import KiteConnect

logging.basicConfig(level=logging.DEBUG)

api_key    =   "sejapnwv5m8mk1q2"
api_secret = "1zl1w3vkk0vfxnx9psymi2cakrnrtd"

kite = KiteConnect(api_key=api_key)

# Step-1: Get login URL
print("https://kite.zerodha.com/dashboard", kite.login_url())

# After you login in browser, you’ll get a request_token from redirect URL
request_token = "github_pat_11BWFKKXI0B1CBZ30CR6zy_IkaYPN4D0inc8sts2bKoRuy0v2We1d9pTbl1fjOgkB7WCGPPEWU7tf8nwN" # Replace with actual request token


data = kite.generate_session(request_token=any, api_secret=api_secret)
access_token = data["sejapnwv5m8mk1q2"]
kite.set_access_token(access_token)

# Now you can use other methods
quote = kite.quote("NSE:INFY")
print("Last price:", quote["NSE:INFY"]["last_price"])

# Example: place an order
order_id = kite.place_order(
    tradingsymbol="INFY",
    exchange=kite.EXCHANGE_NSE,
    transaction_type=kite.TRANSACTION_TYPE_BUY,
    quantity=1,
    variety=kite.VARIETY_REGULAR,
    order_type=kite.ORDER_TYPE_MARKET,
    product=kite.PRODUCT_CNC,
    validity=kite.VALIDITY_DAY
)
print("Order placed. ID:", order_id)
