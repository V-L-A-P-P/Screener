from tvDatafeed import TvDatafeed, Interval


def select_valid_pairs(tv, pairs, strictness=3):
    """

    selects valid pairs from the list

    """
    valid_pairs = []
    for pair in pairs:
        if is_pair_valid(tv, pair, strictness):
            valid_pairs.append(pair)
    return valid_pairs


def is_pair_valid(tv, pair, strictness=3):
    """

    check if pair may be used with tvDataFeedLibrary with connection to Binance( edit if add optional exchange checking)
    strictness because may be data loss sometimes ( more than two losses in a row is rare )

    """
    lim = 0
    data = tv.get_hist(symbol=pair, exchange="Binance", interval=Interval.in_4_hour, n_bars=2)
    while data is None:
        data = tv.get_hist(symbol=pair, exchange="Binance", interval=Interval.in_4_hour, n_bars=2)
        lim += 1

        if lim == strictness:
            print('invalid: ', pair)
            return False
    if not (data is None):
        return True
