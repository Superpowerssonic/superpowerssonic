import pyupbit

# 로그인
access = "8pvdMSe53rAfLEXg6s4k7ycKmLWWai9x2lj51HFn"          # 본인 값으로 변경
secret = "mxXhfJ3B6j3ix68NI0O3nvUbzMxku7SZBPhzuzqS"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

#잔고조회
print(upbit.get_balance("KRW-HPO"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회