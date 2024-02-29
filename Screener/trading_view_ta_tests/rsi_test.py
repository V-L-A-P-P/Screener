import time
from datetime import datetime
from tradingview_ta import TA_Handler, Interval, Exchange


          
INTERVAL = Interval.INTERVAL_1_HOUR


while True:
    
    print(TA_Handler(symbol="BTCUSDT",
                            screener='crypto',
                            exchange='Binance',
                            interval=INTERVAL).get_analysis().indicators['RSI'], end = " (")
    print(datetime.now(), ')')
    time.sleep(5)
