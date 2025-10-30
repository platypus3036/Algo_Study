'''
1. 문제 분석
bit을 다른 숫자로 설정하면, 그 뒤의 숫자들은 전부 지정한 숫자로 바뀜

2. 풀이 방법 고안
0으로 시작, 앞에서부터 1이 있는지 탐색
1이 있으면 그 뒤로는 0이 있는지 탐색
'''
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    bit = input()
    cnt = 0
    zero = True
    for num in bit:
        if zero is True and num == '1':
            cnt += 1
            zero = False
        elif zero is False and num == '0':
            cnt += 1
            zero = True

    print(f'#{tc} {cnt}')
