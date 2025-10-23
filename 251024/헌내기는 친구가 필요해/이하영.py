import sys
sys.stdin = open('input2.txt')

"""
N * M 캠퍼스 크기 
o 빈 공간 = 길
x 벽
I 도연 (무조건 하나)
P 사람

규칙
벽으로는 다닐 수 없음.
벽이 아닌 상하좌우로만 이동 가능

출력
도연이가 만날 수 있는 사람의 수
P 아무도 못만나면 TT 출력


구현 방법
1. 이중 for문 - 도연 찾기
2. BFS or DFS
= 몇 개 찾을 수 있는지 묻고 있음.
= 연결된 범위를 한 번에 탐색하는 문제. = BFS
- 시작 위치를 큐에 넣기
- 큐에서 하나 꺼내서 popleft
- 주변 상하좌우 탐색
- 방문 안했거나, 벽이 아니라면 큐에 추가
- 큐가 빌때까지 반복.


- 도연 위치 I 찾기
- I에서 탐색 시작 
- 벽X 제외 / O, P를 따라서 상하좌우로 이동 
- 이동하면서 만난 P의 개수 카운트
  방문한 곳 다시 안가도록 방문 체크


""" 
from collections import deque

N, M = map(int, input().split())
campus = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]


# 도연 찾기
for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            start = deque([(i, j)])  # 시작 위치는 도연이 좌표
            visited[i][j] = True     # 방문 체크


# 이동
# dir = [[0, 1],[0, -1],[-1, 0],[1, 0]]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
count = 0

# 도연이 자리에서 탐색 시작.
while start:
    x, y = start.popleft() # start(큐)가 빌 때까지 반복.
    
    for k in range(4): # 4방향 각각 좌표 계산
        nx, ny = x + dx[k], y + dy[k]  
        # k : 한 번에 한 칸만 이동 // 파리퇴치 처럼 이동 칸 수 아님
        # k : 방향 선택용 인덱스 // 리스트에서 인덱스로 선택만 하면 됨.

        # 범위 확인 (범위 안에있고, 아직 방문하지 않았을 것.)
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:

            if campus[nx][ny] != 'X':   # x벽이 아닐때 = O길, P사람 
                visited[nx][ny] = True
                start.append((nx, ny))
                if campus[nx][ny] == 'P':
                    count += 1


if count > 0:
    print(count)
else:
    print("TT")  # 아무도 못 만나면 TT출력
