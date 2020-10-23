from libs.openexchange import OpenExchangeClient

APP_ID = "89d6f51913934be1ae8c901bfe44a458"

client = OpenExchangeClient(APP_ID)
usd_amount = 1
inr_amount = client.convert(usd_amount, "USD", "INR")

print(f"USD{usd_amount} is INR : {inr_amount:.2f}")