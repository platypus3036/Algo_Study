'''
1. 문제 분석
벽은 이동할 수 없음. 만날 수 있는 P의 개수를 찾는 문제

2. 풀이 방법 고안
BFS를 사용하면 풀 수 있을 것 같다.
예전에 수업시간에 풀었던 사다리문제나 미로찾기와 유사한 느낌
'''
from collections import deque

N, M = map(int, input().split())
arr = list(input() for _ in range(N))

delta_x = [0, 1, 0, -1]
delta_y = [1, 0, -1, 0]

people = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'I':
            doyuon = (i, j)

q = deque([doyuon])
visited = [[0] * M for _ in range(N)]
x, y = doyuon
visited[x][y] = 1

cnt = 0
while q:
    x, y = q.popleft()
    for dx, dy in zip(delta_x, delta_y):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != 'X' and visited[nx][ny] == 0:
            q.append((nx, ny))
            visited[nx][ny] = 1
            if arr[nx][ny] == 'P':
                cnt += 1

if cnt:
    print(cnt)
else:
    print('TT')
