'''
1. 문제 분석
M초 뒤 K개의 붕어빵을 만들 수 있음
손님의 도착 시간이 주어지고, 대기시간없이 바로 붕어빵을 제공할 수 있는지를 판별

2. 풀이 방법 고안
손님의 도착시간을 sort()
M의 배수인 시간에, 빵이 만들어져서 += K
손님이 오면 빵을 하나 빼고, 빵이 음수가 되면 impossible 출력

0초에도 손님이 올 수 있음

'''
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arrive_time = list(map(int, input().split()))
    arrive_time.sort()
    bread = 0
    result = 'Possible'

    for i in range(arrive_time[-1] + 1):
        if i % M == 0:
            bread += K

        if i in arrive_time:
            bread -= 1

        if bread < 0:
            result = 'Impossible'
            break

    print(f'#{tc} {result}')