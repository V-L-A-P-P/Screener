import evaluation_algorithms
import TelegramBot
from tvDatafeed import Interval

import with_json_working


class OnlineHandler:
    def __init__(self, bot: TelegramBot, tv, tv_live):
        self.__bot = bot
        self.__tv = tv
        self.__tv_live = tv_live

        valid_pairs = with_json_working.load_valid_pairs("Binance")

        # load all pairs to handlers
        for pair in valid_pairs:
            print(pair)
            while True:
                try:
                    seis = tv_live.new_seis(pair, 'BINANCE', Interval.in_5_minute)
                    break
                except Exception as exception:
                    print(exception)
            tv_live.new_consumer(seis, self.get_actual_info)
        print('all pairs have been added')

    def get_actual_info(self, seis, data):
        """
        callback function
        here comes new information about one pair at a certain interval( price, volume )
        """

        symbol = seis.symbol
        exchange = seis.exchange
        interval = seis.interval
        now_price = data.close[0]
        now_volume = data.volume[0]

        valuation = evaluation_algorithms.estimate_the_volume_surge(self.__tv, symbol, exchange, interval, now_volume)
        print(symbol, valuation)
        if valuation > 5:
            self.__bot.send_valuation(symbol, exchange, valuation)
