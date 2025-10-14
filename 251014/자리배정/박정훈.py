'''
1. 달팽이 모양으로 돌면서 자리를 배정하는 문제
예전에 풀었을 때는 각 방향별로 4가지 if문을 만들어서 풀어보려 했으나, 런타임 에러로 실패하였음
dx, dy와 visited를 이용해서 풀 수 있을것이라 생각

2. 격자 크기가 최대 1,000 * 1000이고, 대기번호 K의 최댓값도 1억이라 완전탐색은 불가능

3. 고려사항
dx, dy의 방향을 따라 이동하다가, 벽을 만나거나 visited에 있는 좌석을 만나면 방향 전환
공연장 전체를 만들 필요 x, cnt를 1씩 늘리면서 K와 cnt가 같을때까지 이동
좌석을 배정할 수 없다면 0을 출력 -> C * R 범위 안에 K가 있는지 탐색
'''
C, R = map(int, input().split())
K = int(input())

dx = [0, 1, 0, -1]   # 위, 오른쪽, 아래, 왼쪽 순서
dy = [1, 0, -1, 0]
i = 0

visited = [[0] * C for _ in range(R)]

if C * R >= K:
    cnt = 1
    x, y = 0, 0

    while cnt < K:
        visited[y][x] = 1
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < C and 0 <= ny < R and visited[ny][nx] == 0:
            x, y = nx, ny
        else:
            i = (i + 1) % 4     # 원형큐에서 배운 수의 순환
            x += dx[i]
            y += dy[i]
        cnt += 1

    print(x + 1, y + 1)

else:
    print(0)