"""
1. 문제 분석
NXN의 표에 수가 있는데, 각 열의 숫자들은 오름차순 정렬되어있음
N번째로 큰 수를 구하여라.

2. 풀이방법 고안
마지막 행에는 각 열에서 가장 큰 숫자들이 나열되지만, 그 행에 있는 수가 다른 행, 다른 열의 수보다 작을 수도 있다.
전체에서 가장 큰 수는 마지막 행에서 가장 큰 수를 찾으면 됨
가장 큰 수를 찾은 열에서는 뒤에서 두번째 행의 수를, 나머지 열에서는 마지막 행의 수를 비교

생각보다 안풀린다.
세로로 만든 각 수들의 배열들의 [-1]들을 비교하고, 그 열에 대해 pop()을 해주어야 하는데 어느열인지에 대한 정보를 찾기가 힘듦
튜플로 열의 idx를 같이 넣어주자.

2중 for문을 사용하긴 하지만, N의 최대는 1500이므로 시간은 여유롭다.
"""

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
new_arr = [
    list(nums) for nums in zip(*arr)
]  # 가로세로 뒤집은 새로운 배열, pop()을 할 것이므로 list로 형태 변환

for cnt in range(1, N + 1):
    check_max = []
    for i in range(N):
        check_max.append(new_arr[i][-1])
    if cnt != N:
        new_arr[check_max.index(max(check_max))].pop()
    else:
        print(new_arr[check_max.index(max(check_max))].pop())
