'''
1. 문제 분석
연속된 칸 4개의 합이 가장 크게 되는 값을 출력

2. 풀이 방법 고안
BFS로 깊이가 4인 지점에서 max_sum을 비교 후 갱신
시간 단축을 위해, 시작점 기준 위쪽은 탐색 x

BFS로 안풀려서 다른 방법을 생각하는 중,
테트로미노들의 대칭과 회전을 모두 포함한 가능한 경우의 수는 총 19가지
N * M의 최악의 경우는 25000
한개의 테트로미노에서 탐색하는 칸은 총 4칸이므로
전체를 완전탐색할 때, 최악의 경우의 수는 19,000,000가지
-> 가능한 테트로미노 모양의 모든 경우를 찾아서 해보자

DFS를 이용하면 테트로미노 모양들을 대부분 찾을 수 있는데, 십자모양(ㅗ)은 찾을수가 없음
십자모양은 직접 4가지 모양을 찾아서 따로 찾아주자
'''
from collections import deque

def find_tet(x, y, cnt, sum_num):
    global max_cnt, visited
    if cnt == 3:
        max_cnt = max(max_cnt, sum_num)
        return

    for dx, dy in zip(delta_x, delta_y):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            find_tet(nx, ny, cnt + 1, sum_num + arr[nx][ny])
            visited[nx][ny] = False

def find_cross(x, y):
    global max_cnt
    if 0 <= x - 1 and x < N and 0 <= y - 1 and y + 1 < M:
        sum_num = arr[x][y] + arr[x-1][y] + arr[x][y-1] + arr[x][y+1]
        max_cnt = max(max_cnt, sum_num)

    if 0 <= x - 1 and x + 1 < N and 0 <= y - 1 and y < M:
        sum_num = arr[x][y] + arr[x][y-1] + arr[x-1][y] + arr[x+1][y]
        max_cnt = max(max_cnt, sum_num)

    if 0 <= x and x + 1 < N and 0 <= y - 1 and y + 1 < M:
        sum_num = arr[x][y] + arr[x+1][y] + arr[x][y-1] + arr[x][y+1]
        max_cnt = max(max_cnt, sum_num)

    if 0 <= x - 1 and x + 1 < N and 0 <= y and y + 1 < M:
        sum_num = arr[x][y] + arr[x][y+1] + arr[x-1][y] + arr[x+1][y]
        max_cnt = max(max_cnt, sum_num)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 첫 블럭을 기준으로, 블럭들의 delta_idx를 저장
delta_x = [0, 1, 0, -1]
delta_y = [1, 0, -1, 0]

visited = [[False] * M for _ in range(N)]
max_cnt = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        find_tet(i, j, 0, arr[i][j])
        find_cross(i, j)
        visited[i][j] = False

print(max_cnt)