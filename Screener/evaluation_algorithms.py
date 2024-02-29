import average_values_getting
from tvDatafeed import Interval

tf_coefs = {Interval.in_1_minute.value: 60*24*5, Interval.in_5_minute.value: 200}


def estimate_the_volume_surge(tv, symbol, exchange, interval: Interval, now_volume):
    percentage_excess = get_volume_excess(tv, symbol, exchange, interval, now_volume)

    if percentage_excess >= 100: return 10
    elif percentage_excess >= 75: return 9
    elif percentage_excess >= 50: return 8
    elif percentage_excess >= 40: return 7
    elif percentage_excess >= 30: return 6
    elif percentage_excess >= 20: return 5
    elif percentage_excess >= 10: return 4
    elif percentage_excess >= 5: return 3
    elif percentage_excess >= 2: return 2
    else: return 1


def get_volume_excess(tv, symbol, exchange, interval: Interval, now_volume):
    """
    gives the percentage that the given value exceeds the average value
    """
    #print(tf_coefs[interval.value])
    average_volume = average_values_getting.get_average_volume(tv, symbol, exchange, interval, tf_coefs[interval.value])
    excess = now_volume / average_volume - 1
    return excess
