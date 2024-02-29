import time
from datetime import datetime
from tradingview_ta import TA_Handler, Interval, Exchange


          
INTERVAL = Interval.INTERVAL_15_MINUTES
handler = TA_Handler(exchange='Binance')

'''
while True:
    
    print('btc', TA_Handler(symbol="BTCUSDT",
                            screener='crypto',
                            exchange='BYBIT',
                            interval=INTERVAL).get_analysis().indicators['volume'])
    
    print('xrp', TA_Handler(symbol="XRPUSDT",
                            screener='crypto',
                            exchange='Bybit',
                            interval=INTERVAL).get_analysis().indicators['volume'], end = " (")
        
    print(datetime.now(), ')')
    time.sleep(1)
'''
