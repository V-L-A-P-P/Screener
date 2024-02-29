from tvDatafeed import Interval


# calculates the average of volumes in the last "n_bars" bars at the selected interval
# "lim" because may be data loss sometimes ( more than two losses in a row is rare )
def get_average_volume(tv, symbol, exchange, interval: Interval, n_bars: int):
    """

    calculates the average of volumes in the last "n_bars" bars at the selected interval
    "lim" because may be data loss sometimes ( more than two losses in a row is rare )

    """

    data = None
    lim = 0
    while data is None:

        data = tv.get_hist(symbol=symbol, exchange=exchange, interval=interval, n_bars=n_bars + 2)
        lim += 1
        if lim > 10: print('Братан, серьёзные проблемы с этой парой', symbol)

    # Решение для Future Warning : list(data.volume)

    return sum(data.volume[:-2]) / n_bars


def get_average_price(tv, symbol, exchange, interval: Interval, n_bars: int):
    data = None
    lim = 0
    while data is None:

        data = tv.get_hist(symbol=symbol, exchange=exchange, interval=interval, n_bars=n_bars)
        lim += 1
        if lim > 10: print('Братан, серьёзные проблемы с этой парой', symbol)
    return sum(data.close) / n_bars
