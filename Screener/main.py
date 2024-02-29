from tvDatafeed import TvDatafeed, TvDatafeedLive
import TelegramBot
import OnlineHandler
import traceback

# username = ''
# password = ''
# tv = TvDatafeed(username, password)
# tv_live = TvDatafeedLive(username, password)


if __name__ == "__main__":
    try:
        tv = TvDatafeed()
        tv_live = TvDatafeedLive()

        bot = TelegramBot.TelegramBot()
        bot.bot_launch()
        online_handler = OnlineHandler.OnlineHandler(bot, tv, tv_live)
    except Exception as _ex:
        print(traceback.format_exc())
