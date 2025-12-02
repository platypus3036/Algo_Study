'''
1. 문제 분석
파이프를 오른쪽, 대각선아래, 아래 방향으로 이동시키며 파이프의 한쪽 끝을 오른쪽 아래 끝으로 옮기는 방법의 수를 출력
45도만 밀 수 있으므로, 오른쪽 방향에서 아래 방향으로 바로 이동시키는 것은 불가능

2. 풀이 방법 고안
N이 그렇게 크지는 않음.
start는 (0, 1)
경우의 수를 찾고, 전으로 돌아가서 다른 가지의 경우의 수를 찾으면 될 것 같음.
state는 right, diag, down 셋 중 하나
state = right이면, diag와 right 중 하나만 가능
state = down이면, diag와 down 중 하나만 가능
state = diag이면 모두 가능
다음 state로 diag을 두고 싶으면, 원래 좌표의 우, 아래, 대각선아래가 모두 0이어야 가능
기본값을 0으로 두고, 경우의 수를 cnt로 추가해주면 불가능할 때 0이 나옴

89퍼에서 시간초과

DFS로 풀 수 없다
DP를 사용해야 함
'''
# N = int(input())
# arr = [list(map(int, input().split( ))) for _ in range(N)]
# cnt = 0
#
# def dfs(x, y, state):
#     global cnt
#
#     if x == N - 1 and y == N - 1:
#         cnt += 1
#         return
#
#     if state in ['right', 'diag']:
#         if y + 1 < N and arr[x][y+1] == 0:
#             dfs(x, y+1, 'right')
#
#     if state in ['right', 'diag', 'down']:
#         if x + 1 < N and y + 1 < N and arr[x][y+1] == 0 and arr[x+1][y+1] == 0 and arr[x+1][y] == 0:
#             dfs(x+1, y+1, 'diag')
#
#     if state in ['diag', 'down']:
#         if x + 1 < N and arr[x+1][y] == 0:
#             dfs(x+1, y, 'down')
#
# dfs(0, 1, 'right')
#
# print(cnt)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]

dp[0][1][0] = 1

# 가로: 0, 대각선: 1, 세로: 2
for x in range(N):
    for y in range(N):
        # 가로로 이동
        if y - 1 >= 0 and arr[x][y] == 0:
            dp[x][y][0] += dp[x][y-1][0] + dp[x][y-1][1]

        # 대각선 이동
        if x - 1 >= 0 and y - 1 >= 0 and arr[x][y] == 0 and arr[x-1][y] == 0 and arr[x][y-1] == 0:
            dp[x][y][1] += dp[x-1][y-1][0] + dp[x-1][y-1][2] + dp[x-1][y-1][1]

        # 세로로 이동
        if x - 1 >= 0 and arr[x][y] == 0:
            dp[x][y][2] += dp[x-1][y][2] + dp[x-1][y][1]

print(sum(dp[N-1][N-1]))