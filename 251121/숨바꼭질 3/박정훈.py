'''
1. 문제 분석
수빈이의 위치가 X일때, 걸으면 1초후 좌우로 1칸을, 순간이동을 하면 즉시 2*X로 이동가능
가장 빨리 동생을 찾을 때 몇초가 걸릴까?

2. 풀이 방법 고안
동생이 형을 찾는식으로 거꾸로 생각해보자
동생의 위치가 짝수이면 즉시 2로 나누고, 동생의 위치가 홀수이면 +1 혹은 -1을 진행해야 함
예를 들어, 10 49와 같이 주어지면
49를 줄여서 10까지 가야함
49 48 24 12 11 10으로총 3초
34 45와 같이 주어지면
34 * 2인 68까지 갈것인지, 34까지 갈것인지 선택
37 48과 같이 주어지면 48을 37으로 줄일것인지, 74로 늘릴것인지 선택
만약 37로 줄일것이라면, 24에서 37까지 갈것인지, 48에서 37까지 갈것인지 선택

경우의 수가 너무 많다
예를 들어, 5 19로 수가 나오면
19 20 10 5의 식으로 가면 1초인데,
19 18 9 8 4 5로 가면 3초임

BFS로 해보자
cnt가 1 올라가는 때는 +1 or -1만 해당함
N을 2배로 올리는것은 cnt 변동 x
-> 런타임에러 발생

왜 메모리초과가 나올까?
예를들어, 5 17의 입력값이 있다면
while 한 사이클이 돌면, q에는 (10, 0), (6, 1), (4, 1)이 들어감.
두번째는 (6, 1), (4, 1), (20, 0), (11, 1), (9, 1)이 들어감.
(20, 0)과 같이 cnt가 작은것 부터 먼저 탐색하고싶다

deque에는 pop()와 popleft()처럼 append()와 appendleft()가 있다고 함
이를 이용하면 cnt가 바뀌지 않는 tuple을 먼저 탐색가능
-> 오답

다익스트라와 같은 사용방식에서는, q를 popleft한 직후에 방문처리를 하고, 분석하는것이 맞는 방법이라고 함
가중치가 섞여있는 상황에서는 큐에 넣는 순서와 큐에서 나오는 순서가 달라질 수 있기 때문
'''
# from collections import deque
#
# N, K = map(int, input().split())
# q = deque([(N, 0)])
# visited = [0] * 100001
# visited[N] = 1
# while q:
#     n, cnt = q.popleft()
#     if n == K:
#         result = cnt
#         break
#
#     new_n = n * 2
#     if 0 <= new_n < 100001 and not visited[new_n]:
#         q.append((new_n, cnt))
#         visited[new_n] = 1
#
#     new_n_2 = n + 1
#     if 0 <= new_n_2 < 100001 and not visited[new_n_2]:
#         q.append((new_n_2, cnt+1))
#         visited[new_n_2] = 1
#
#     new_n_3 = n - 1
#     if 0 <= new_n_3 < 100001 and not visited[new_n_3]:
#         q.append((new_n_3, cnt + 1))
#         visited[new_n_3] = 1
#
# print(result)
from collections import deque

N, K = map(int, input().split())
q = deque([(N, 0)])
visited = [0] * 100001
while q:
    n, cnt = q.popleft()

    if visited[n]:
        continue

    visited[n] = 1

    if n == K:
        print(cnt)
        break

    new_n = n * 2
    if 0 <= new_n < 100001 and not visited[new_n]:
        q.appendleft((new_n, cnt))

    new_n_2 = n + 1
    if 0 <= new_n_2 < 100001 and not visited[new_n_2]:
        q.append((new_n_2, cnt+1))

    new_n_3 = n - 1
    if 0 <= new_n_3 < 100001 and not visited[new_n_3]:
        q.append((new_n_3, cnt + 1))
