from binance.um_futures import UMFutures


# only for binance (to be continued...)
def get_pairs():
    client = UMFutures()
    tickers = client.mark_price()

    pairs = []

    for i in tickers:
        pairs.append(i['symbol'])

    return pairs

