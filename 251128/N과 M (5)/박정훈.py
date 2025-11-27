'''
1. 문제 분석
길이가 N인 수열에서, 부분집합의 길이가 M인 수열을 모두나열하시오

2. 풀이 방법 고안
수열은 오름차순으로 정렬되야 하므로, 수열을 먼저 정렬해줘야 함
subset 안에 추가하려는 숫자가 없으면, 추가해서 함수를 재귀
'''
def my_subset(cnt, subset):
    if cnt == M:
        print(" ".join(map(str, subset)))
        return

    for num in num_list:
        if num not in subset:
            my_subset(cnt+1, subset + [num])


N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

my_subset(0, [])