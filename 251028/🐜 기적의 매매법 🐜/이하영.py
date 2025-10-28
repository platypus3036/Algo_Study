import sys
sys.stdin = open('input_2.txt')

"""
준현 : BNP
성민 : TIMING
똑같으면 : SAMESAME

입력
첫째줄 현금
둘째줄 주가 공백을 두고 차례로 주어짐.

1. 가능한 만큼 즉시 매수
보유 가격 cash = 100원
주가 price = 40원
매수 buy 개수 = 2개
=> 80원에 2개 매수.
=> 잔액 20원

즉, 보유 현금 // 주가 = 매수한 개수
    보유 현금 잔액 = 원래 현금 - 매수개수 * 주가

    
2. 주가가 3일 째 상승 시, 전량 매도
주가가 14일 치 주어지니까 for i 로 돌려서 0~13로 인덱스 번호 출력하고
3일 연속은 인덱스 번호로 2니까,  i >= 2  (0, 1, 2번 날짜의 주가 모두 확인.)
상승하는 주가는 price의 인덱스 번호 기준으로 
price[i] < price[i+1] < price[i+2]


3. 주가가 3일 째 하락 시, 전량 매수
하락하는 주가는 price의 인덱스 번호 기준으로 
price[i] > price[i+1] > price[i+2]



- 그래서 즉시 매수만 했을때
- 상승 시 매도, 하락 시 매수 했을때

누가 더 많은 잔액을 보유하고 있는지?
각자의 잔액 = cash + price[-1] * buy

매수 cash -= 이때 산 개수 buy * price
매도 cash += 누적된 보유량 buy_count * price 

- 인덱스 에러 
for i in range(len(price)):
price[i] < price[i+1] < price[i+2]:
price[i] > price[i+1] > price[i+2]:
=> i가 14번째 이상으로 가니까 인덱스 에러남.
=> 순서를 반대로 price[i-2] > price[i-1] > price[i]:
   i를 기준으로 앞쪽이 작아지게 배치하기.

"""


def whos_winner(cash, price):
    # 준현과 성민의 초기 현금, 초기 보유량은 같지만
    # 계속 갱신하면 서로 값이 달라지므로 따로 저장해야 됨.
    cash_junhyun = cash
    cash_sungmin = cash
    # 누적 주식 보유량 카운트 
    buy_junhyun_count = 0
    buy_sungmin_count = 0
    
    
    for i in range(len(price)):
        
        # 준현 = 가능한 만큼 즉시 매수. 마지막 날 매도 
        buy_junhyun = cash_junhyun // price[i] # 구매 개수
        buy_junhyun_count += buy_junhyun       # 누적시키기
        cash_junhyun -= buy_junhyun * price[i] # 매수, 남은 현금 갱신 = 구매 개수 * 주가 몇원

        # 성민
        if i >= 3:
            # 3일 연속 상승 시 매도
            if price[i-2] < price[i-1] < price[i]:
                cash_sungmin += buy_sungmin_count * price[i] # 누적값에 곱하기
                buy_sungmin_count = 0 # 다 팔았으니까 누적된 보유량 초기화

            # 3일 연속 하락 시 매수
            if price[i-2] > price[i-1] > price[i]:
                buy_sungmin = cash_sungmin // price[i]
                buy_sungmin_count += buy_sungmin
                cash_sungmin -= buy_sungmin * price[i]


    last_junhyun = cash_junhyun + price[-1] * buy_junhyun_count
    last_sungmin = cash_sungmin + price[-1] * buy_sungmin_count


    if last_junhyun > last_sungmin:
        return 'BNP'

    elif last_junhyun < last_sungmin:
        return 'TIMING'
        
    else:
        return 'SAMESAME' 
    

# 입력
cash = int(input())
price = list(map(int, input().split()))
result = whos_winner(cash, price)
print(result)


"""
왜 틀렸을까... 출력은 맞음.
엣지케이스 뭐가 있을지

1. 초기 현금이 주가보다 작은 경우
둘 다 애초에 거래를 못해서 잔액도 같을테니 SAMESAME. 

2. 14일 내내 동일한 주가인 경우.
준현 : 처음에 구매하고, 이후 현금 부족으로 못삼.
      첫 구매한 매도 개수로 잔액 계산

성민 : (1) 첫 날 구매하고, 이후 매수 및 매도 못함.
          첫 날 구매한 매도 개수로 잔액 계산
      (2) 혹은 애초에 구매를 안함.

=> 성민이는 초기 매매를 언제 하는거야??
하락이 없으면 매수도 안하는건가? 그럼 그냥 아무것도 안하고 현금보유로 끝? 

=> 성민이는 매도하고 남은 현금으로 다음 주식을 다시 사긴하는건지?
=> 설마 하락한다고 예측한 다음날에 팔고, 상승한다는 다음날에 사지는 않겠지.. 
  wow 성민이는 ㅄ이었다.


[기존 코드]
# 성민
# 3일 연속 상승 시 매도
if i >= 2 and price[i-2] < price[i-1] < price[i]:
    cash_sungmin += buy_sungmin_count * price[i] # 누적값에 곱하기
    buy_sungmin_count = 0 # 다 팔았으니까 누적된 보유량 초기화

# 3일 연속 하락 시 매수
if i >= 2 and price[i-2] > price[i-1] > price[i]:
    buy_sungmin = cash_sungmin // price[i]
    buy_sungmin_count += buy_sungmin
    cash_sungmin -= buy_sungmin * price[i]

[정답 코드]
# 성민
if i >= 3:
    # 3일 연속 상승 시 매도
    if price[i-2] < price[i-1] < price[i]:
        cash_sungmin += buy_sungmin_count * price[i] # 누적값에 곱하기
        buy_sungmin_count = 0 # 다 팔았으니까 누적된 보유량 초기화

    # 3일 연속 하락 시 매수
    if price[i-2] > price[i-1] > price[i]:
        buy_sungmin = cash_sungmin // price[i]
        buy_sungmin_count += buy_sungmin
        cash_sungmin -= buy_sungmin * price[i]

        

3일 연속 상승 -> 내일 하락할 것이다. -> 오늘 매도하자. 즉, 떨어지기 전에 팔기.
3일 연속 하락 -> 내일 상승할 것이다. -> 오늘 매수하자. 즉, 오르기 전에 사기. 
=> i >= 2, price[i-2] < price[i-1] < price[i]
   이게 맞지.. 왜?????

"""
