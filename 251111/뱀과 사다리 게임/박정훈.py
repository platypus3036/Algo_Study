'''
1. 문제 분석
월말평가로 나왔던 문제다. 항상 100번칸에 도착할 수 있으며, 사다리와 뱀은 각 칸에 최대 1개만 존재
사다리는 보드판의 앞으로 이동하는 기믹, 뱀은 뒤로 이동하는 기믹
100번칸에 도착하기 위해 몇번 주사위를 굴려야 하는가?

2. 풀이 방법 고안
칸이 100번까지밖에 없기 때문에, 여러번 탐색을 반복해도 됨
BFS를 사용해서 최소한의 이동으로 100번 칸에 갈 수 있는 방법을 찾아보자
now에 1~6까지를 계속 더해주면서 사다리나 뱀을 타고 이동시킨다
now가 100보다 커지면, continue
몇번 이동했는지 count해야 하므로, q에 튜플 형태로 현재 위치와 이동횟수를 같이 넣는다
'''
from collections import deque

N, M = map(int, input().split())
move_list = [tuple(map(int, input().split())) for _ in range(N + M)]

q = deque([(1, 0)])
visited = [False] * 101

while q:
    now, cnt = q.popleft()
    if now == 100:
        result = cnt
        break
    for i in range(1, 7):
        move = now + i
        if move > 100:
            continue
        for ladder in move_list:
            if move == ladder[0]:
                move = ladder[1]
        if not visited[move]:
            visited[move] = True
            q.append((move, cnt+1))

print(result)