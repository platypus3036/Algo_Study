'''
1. 문제 분석
중복조합을 모두 구하는 문제
nHm를 구하라

2. 풀이 방법 고안
itertools에 기본적으로 순열, 조합, 중복순열, 중복조합이 있다고 알고는 있으나,
연습 겸 직접 구현해보자
-> itertools.combinations_with_replacement([i for i in range(1, N)], M)으로 간단히 풀기 가능

수업시간에 순열과 조합을 구현하는 것을 배운 기억이 있음
함수를 재귀로 돌면서, cnt=M일때 return하는 방식
'''
def my_combination(start, now_lst, cnt):
    if cnt == M:
        print(' '.join(now_lst))
        return

    for i in range(start, N+1):
        my_combination(i, now_lst + [str(i)], cnt+1)

N, M = map(int, input().split())
my_combination(1, [], 0)