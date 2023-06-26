import pyupbit
import numpy as np

#open high low close volume에 대한 정보를 불러옴 count=7 은 7일치
df = pyupbit.get_ohlcv("KRW-BTC", count=7)   #count=7 은 7일 치  / ohlcv open higl low close volume
#변동폭 *k 계산, (고가-저가) * k 값
df['range'] = (df['high'] - df['low']) * 0.5  #0.5를 k값으로 가정 
# target(매수가), range(1일치) 컬럼을 한칸씩 밑으로 내림(.shift(1))
df['target'] = df['open'] + df['range'].shift(1)
print(df)

fee = 0.005
#ror(수익률), np.where(조건문, 참일때 값, 거짓일때 값)
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'] - fee,
                     1)
#누적 곱 계산(cumprod) -> 누적수익률
df['hpr'] = df['ror'].cumprod()
# Draw Down 계산 (누적 최대 값과 현재 hpr 차이 / 누적 최대값 *100)
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
#MDD 계산
print("MDD(%): ", df['dd'].max())
#MDD 값 저장 
df.to_excel("dd.xlsx")