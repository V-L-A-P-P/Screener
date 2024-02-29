from threading import Thread
import telebot


class TelegramBot:
    __token = "5004761639:AAFZEU8rmV3b1Dl_EOw5kcu0tGSgFOjQbXI"
    __chat_ids = "add yours"

    def __init__(self):
        self.__bot = telebot.TeleBot(token=TelegramBot.__token)

    def initialize(self):
        self.__bot.polling(none_stop=True)

    def bot_launch(self):
        # starting it in another thread
        Thread(target=self.initialize, daemon=True).start()
        # simple indicating of successful launch
        print('bot launched!')

    def send_message(self):
        self.__bot.send_message(self.__chat_ids, "test")

    def send_valuation(self, pair, exchange, valuation):
        self.__bot.send_message(self.__chat_ids, exchange + " " + pair + " : " + str(valuation))
