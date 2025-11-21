'''
1. 문제 분석
제공되는 수들은, 키가 1인 사람부터 자신 왼쪽에 자신의 키보다 큰 사람이 몇명인지를 나타내는 수이다.
줄을 선 순서대로 출력

2. 풀이 방법 고안
N이 최대 10이기 때문에, 어떤식으로든 풀 수 있음
idx_list = [False] * 10을 설정해두고,
키가 작은순으로 True로 바꾸는 식으로 풀어보자

먼저, 키가 1인 사람은 본인의 위치를 바로 알 수 있음. result[num_list[0]] = 1, idx_list[num_list[0]] = True
키가 2인 사람의 경우에는, idx_list를 순회하다가 False가 num_list[1]번째인 곳을 True로 바꾸고, 그때의 index를 result에 넣어서 탐색
'''
N = int(input())
num_list = list(map(int, input().split()))

idx_list = [False] * N
result = [0] * N

for i in range(N):
    cnt = 0
    for j in range(N):
        if cnt == num_list[i] and idx_list[j] is False:
            idx_list[j] = True
            result[j] = i+1
            break

        if idx_list[j] is False:
            cnt += 1

print(" ".join(map(str, result)))