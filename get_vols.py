import gdax
import math as m
import time
import random

public_client = gdax.PublicClient()

def get_volumes():
    pairs = ['BTC-USD', 'ETH-USD', 'LTC-USD', 'LTC-EUR', 'ETH-BTC', 'BTC-EUR', 'ETH-EUR']
    #response = public_client.get_product_ticker(product_id='BTC-USD')
    n = float(random.randint(0, 20000))
    volumes = {}
    for pair in pairs:
        volumes[pair] = round(float(public_client.get_product_ticker(product_id = pair)["volume"].encode("utf-8")), 4) + n
    return volumes

get_volumes()
