"""
1. 문제 분석
R, G, B로 구역이 나누어져 있는데, 적록색약인 사람이 봤을때와 적록색약이 아닌 사람이 봤을 때 각각 몇개의 구역으로 나뉘어져 있는가?

2. 풀이 방법 고안
BFS를 통해 가능한 지점을 모두 탐색
-> 더이상 가능한 지점이 없으면, cnt += 1을 하고 다음 지점으로 넘어감

적록색약의 경우에는 visited[x][y]와 visited[nx][ny]가 모두 'RG'에 in 관계인지를 판단하면 됨
"""

from collections import deque

N = int(input())
arr = list(input() for _ in range(N))

delta_x = [0, 1, 0, -1]
delta_y = [1, 0, -1, 0]

q = deque([])
visited = [[False] * N for _ in range(N)]
cnt = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            q.append((i, j))
            visited[i][j] = True

            while q:  # BFS
                x, y = q.popleft()
                for dx, dy in zip(delta_x, delta_y):
                    nx = dx + x
                    ny = dy + y
                    if (
                        0 <= nx < N
                        and 0 <= ny < N
                        and arr[x][y] == arr[nx][ny]
                        and not visited[nx][ny]
                    ):
                        visited[nx][ny] = True
                        q.append((nx, ny))

            cnt += 1

blind_q = deque([])
blind_visited = [[False] * N for _ in range(N)]
blind_cnt = 0

for i in range(N):
    for j in range(N):
        if not blind_visited[i][j]:
            blind_q.append((i, j))
            blind_visited[i][j] = True

            while blind_q:
                x, y = blind_q.popleft()
                for dx, dy in zip(delta_x, delta_y):
                    nx = dx + x
                    ny = dy + y
                    if 0 <= nx < N and 0 <= ny < N and not blind_visited[nx][ny]:
                        if arr[x][y] == "B" and arr[x][y] == arr[nx][ny]:
                            blind_visited[nx][ny] = True
                            blind_q.append((nx, ny))
                        elif arr[x][y] in "RG" and arr[nx][ny] in "RG":
                            blind_visited[nx][ny] = True
                            blind_q.append((nx, ny))

            blind_cnt += 1

print(cnt, blind_cnt)
