import matplotlib.pyplot as plt
import yfinance as yf
from ta.volatility import BollingerBands, AverageTrueRange
from ta.trend import MACD, EMAIndicator, SMAIndicator
from ta.momentum import RSIIndicator, StochasticOscillator
import datetime

hisse = "BIMAS.IS"

def veri_indir(his, baslangic_tarihi, bitis_tarihi):
    df = yf.download(his, start=baslangic_tarihi, end=bitis_tarihi, progress=False)
    return df

bugun = datetime.date.today()
sure = 300

once = bugun - datetime.timedelta(days=sure)
baslangic_tarihi = once
bitis_tarihi = bugun

veri = veri_indir(hisse, baslangic_tarihi, bitis_tarihi)

def teknik_gostergeler():
    macd = MACD(veri['Close'], window_slow=26, window_fast=12, window_sign=9).macd()
    rsi = RSIIndicator(veri['Close'], window=14).rsi()
    sma = SMAIndicator(veri['Close'], window=7).sma_indicator()
    ema_9 = EMAIndicator(veri['Close'], window=9).ema_indicator()
    ema_26 = EMAIndicator(veri['Close'], window=26).ema_indicator()
    atr = AverageTrueRange(veri['High'], veri['Low'], veri['Close'], window=14).average_true_range()
    stochastic = StochasticOscillator(veri['High'], veri['Low'], veri['Close'], window=14, smooth_window=3).stoch()
    
    plt.figure(figsize=(14, 20))
    
    plt.subplot(6, 1, 1)
    plt.plot(veri.index, veri['Close'], label='Kapanış Fiyatı')
    plt.legend()
    plt.title('Hisse Fiyatı')
    plt.xlabel('')
    plt.xticks(rotation=45)
    
    plt.subplot(6, 1, 2)
    plt.plot(veri.index, sma, label='SMA (7)')
    plt.legend()
    plt.title('SMA (7)')
    plt.xlabel('')
    plt.xticks(rotation=45)
    
    plt.subplot(6, 1, 3)
    plt.plot(veri.index, ema_9, label='EMA (9)')
    plt.plot(veri.index, ema_26, label='EMA (26)')
    plt.legend()
    plt.title('EMA (9) ve EMA (26)')
    plt.xlabel('')
    plt.xticks(rotation=45)
    
    plt.subplot(6, 1, 4)
    plt.plot(veri.index, macd, label='MACD (12, 26, 9)')
    plt.legend()
    plt.title('MACD (12, 26, 9)')
    plt.xlabel('')
    plt.xticks(rotation=45)
    
    plt.subplot(6, 1, 5)
    plt.plot(veri.index, rsi, label='RSI (14)')
    plt.legend()
    plt.title('RSI (14)')
    plt.xlabel('')
    plt.xticks(rotation=45)
    
    plt.subplot(6, 1, 6)
    plt.plot(veri.index, atr, label='ATR (14)')
    plt.plot(veri.index, stochastic, label='Stokastik Osilatör (14, 3)')
    plt.legend()
    plt.title('ATR (14) ve Stokastik Osilatör (14, 3)')
    plt.xlabel('')
    plt.xticks(rotation=45)
    
    plt.tight_layout(pad=3.0)
    plt.subplots_adjust(top=0.95)
    plt.show()

teknik_gostergeler()
