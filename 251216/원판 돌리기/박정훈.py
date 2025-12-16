'''
1. 문제 분석
반지름이 1, 2, ..., N인 원판이 순서대로 있음
번호는 연속되도록 위치
번호가 xi의 배수인 원판을 di방향으로 ki칸 회전시킴
di가 0이면 시계방향, 1이면 반시계방향
한번 회전할때마다 인접한 수가 같은 수이면 제거
회전 이후 제거할 수가 없다면, 평균보다 큰 수는 -1, 평균보다 작은수는 +1
모든 회전이 끝나고, 원판에 적힌 수의 합을 출력

2. 풀이 방법 고안
N, M, T의 최대치가 50이라서 pop을 사용하면 시간복잡도가 너무 커질 것 같음
굳이 회전을 직접 시켜야하나?
[1, 2, 3, 4, 5]에서 2번 회전을 해서 [3, 4, 5, 1, 2]를 탐색하게끔 하려면
start = 2으로 설정하고, for문을 2번 사용하면 될 것 같음
for i in range(start, M)
for i in range(start)으로 총 2번 사용하면 회전한 효과와 같아진다.

2중 for문을 사용하지 않아도 될 것 같다.
전체를 탐색하면서, 원형큐 부분에서 배운 인덱스 회전을 이용하면 될 것 같음

숫자를 제거할 때, 같은 숫자가 2개씩 붙어있다는 보장이 없음.
바로 지우는 방법보다는 같은 숫자의 범위를 설정하고, 계산 후 한번에 지워야 한다.

숫자를 제거하면 그 숫자는 0으로 설정하고,
평균과 비교해서 +1 혹은 -1을 할 때는 숫자가 0이 아닐 때만 계산하게끔 하자
'''
N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
start = [0] * N     # 각 원판의 start를 저장하는 리스트

for _ in range(T):
    xi, di, ki = map(int, input().split())
    for x in range(xi, N+1, xi):
        # print(arr[x - 1])
        if di == 0:
             start[x - 1] = (start[x - 1] + ki) % M
        else:
            start[x - 1] = (start[x - 1] + (M - ki)) % M

    delete = []

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                continue

            if arr[i][j] == arr[i][(j + 1) % M]:
                delete.append((i, j))
                delete.append((i, (j + 1) % M))

    for j in range(M):
        for i in range(N - 1):
            if arr[i][(j - start[i]) % M] == 0:
                continue

            if arr[i][(j - start[i]) % M] == arr[i + 1][(j - start[i + 1]) % M]:
                delete.append((i, (j - start[i]) % M))
                delete.append((i + 1, (j - start[i + 1]) % M))

    if delete:
        for i, j in delete:
            arr[i][j] = 0
    else:
        total_sum = 0
        cnt = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j] != 0:
                    total_sum += arr[i][j]
                    cnt += 1

        if cnt > 0:
            avg = total_sum / cnt
            for i in range(N):
                for j in range(M):
                    if arr[i][j] != 0:
                        if arr[i][j] > avg:
                            arr[i][j] -= 1
                        elif arr[i][j] < avg:
                            arr[i][j] += 1

result = 0
for lst in arr:
    result += sum(lst)
print(result)