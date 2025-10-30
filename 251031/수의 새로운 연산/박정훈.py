'''
1. 문제 분석
점의 좌표를 보고 할당된 수를 찾는 함수,
수를 보고 점의 좌표를 찾는 함수
새로운 연산을 구현

2. 풀이 방법 고안
함수 2개를 먼저 만들고, 좌표들끼리 덧셈해서 최종 결론 도출 가능
점의 좌표를 보고 수를 찾는 함수는 점의 좌표끼리 더한 값을 기준으로 찾을 수 있음
수르 보고 점의 좌표를 찾는 함수는 n(n+1)//2의 범위 내로 찾을 수 있음
'''
import sys
sys.stdin = open('input.txt')

def find_num(x, y):
    n = (x + y - 2)
    start = n*(n+1) // 2
    return start + x

def find_x_y(num):
    n = 0
    while True:
        if n*(n+1)//2 < num <= (n+1)*(n+2)//2:
            sum_x_y = n+2
            break
        n += 1

    x = num - n*(n+1)//2
    y = sum_x_y - x
    return (x, y)

T = int(input())
for tc in range(1, T+1):
    p, q = map(int, input().split())

    x1, y1 = find_x_y(p)
    x2, y2 = find_x_y(q)

    result = find_num(x1+x2, y1+y2)
    print(f'#{tc} {result}')