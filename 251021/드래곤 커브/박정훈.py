'''
1. 문제 분석
세대가 올라가면서, 90도 돌면서 기존의 모양을 늘려나가는 모양
정사각형의 네 꼭짓점이 모두 드래곤커브의 일부인 개수를 출력
동시에 여러개의 드래곤커브가 존재 가능. 겹칠 수 있음

2. 풀이 방법 고안
90도 돌아가면서 모양이 커진다
-> 기존의 모양을 저장, 방향은 dx dy의 루프를 통해 설정 가능
-> 세대가 올라가면 오른쪽, 위쪽, 왼쪽, 아래 순서대로 추가할 점의 방향이 변경

세대가 올라가면, 기존의 방향들에서 한칸 다음의 방향들을 역순으로 구현
시작점은 기존 드래곤커브믜 마지막점
'''
N = int(input())
visited = [[0] * 101 for _ in range(101)]

delta_x = [1, 0, -1, 0]
delta_y = [0, -1, 0, 1]

for _ in range(N):
    x, y, d, g = map(int, input().split())
    visited[x][y] = 1
    direction = [d]
    x = x + delta_x[d]
    y = y + delta_y[d]
    visited[x][y] = 1     # 0세대

    for age in range(g):     # 1세대부터
        for dir in reversed(direction):   # 방향 설정은 역순으로
            dir = (dir + 1) % 4     # 다음 방향을 추가(0, 1, 2, 3 반복)
            x = x + delta_x[dir]
            y = y + delta_y[dir]        # x, y를 드래곤 커브의 마지막 지점으로 설정
            visited[x][y] = 1
            direction.append(dir)

cnt = 0
for i in range(100):
    for j in range(100):
        if visited[i][j] == 1 and visited[i][j+1] == 1 and visited[i+1][j] == 1 and visited[i+1][j+1] == 1:
            cnt += 1

print(cnt)