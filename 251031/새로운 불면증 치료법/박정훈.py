'''
1. 문제 분석
본 양의 번호의 숫자들을 저장
본 숫자들이 0~9까지라면 마지막으로 본 양의 번호를 출력

2. 풀이 방법 고안
숫자를 저장하는 set을 만들어서, 0~9까지 총 10개의 숫자가 있으면 break
'''
import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    number_set = set()
    sheep_num = N

    while True:
        for i in str(sheep_num):
            number_set.add(i)

        if len(number_set) == 10:
            break

        sheep_num += N

    print(f'#{tc} {sheep_num}')