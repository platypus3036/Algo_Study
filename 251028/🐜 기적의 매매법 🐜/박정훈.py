'''
1. 문제 분석
단순구현 문제
준현이는 첫날에 전량매수 이후, 남은 돈으로 주식을 살 수 있는 날마다 계속 전량매수
성민이는 3일연속 하락하면 전량매수, 3일연속 상승하면 전량매도
'''
money = int(input())
MachineDuck = list(map(int, input().split()))

JH_stock = 0
JH_money = money

for i in range(len(MachineDuck)):
    if JH_money // MachineDuck[i] != 0:
        JH_stock += JH_money // MachineDuck[i]
        JH_money -= (JH_money // MachineDuck[i]) * MachineDuck[i]

JH_money += JH_stock * MachineDuck[-1]

SM_stock = 0
SM_money = money

for i in range(3, len(MachineDuck)):
    if MachineDuck[i-3] > MachineDuck[i-2] > MachineDuck[i-1] > MachineDuck[i]:
        SM_stock += SM_money//MachineDuck[i]
        SM_money -=  (SM_money//MachineDuck[i]) * MachineDuck[i]

    if MachineDuck[i-3] < MachineDuck[i-2] < MachineDuck[i-1] < MachineDuck[i]:
        if SM_stock > 0:
            SM_money += SM_stock * MachineDuck[i]
            SM_stock = 0

SM_money += SM_stock * MachineDuck[-1]

if JH_money > SM_money:
    print('BNP')
elif JH_money < SM_money:
    print('TIMING')
else:
    print('SAMESAME')