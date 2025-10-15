'''
1. 문제 분석
K년동안 봄, 여름, 가을, 겨울을 돌면서 각 계절에 맞는 규칙에 따라 나무와 양분이 변화
나무의 나이를 저장하는 list, 땅의 양분 상태를 저장할 list가 필요

2. 시간복잡도
K의 최댓값이 1000이지만 N의 최댓값이 10, M의 최댓값은 100이라서 잘하면 단순구현으로 풀릴 수 있을것이라 생각

3. 풀이 방법
봄에 여러개의 나무가 있을 때, 어린 나무부터 양분을 먹기 때문에 sort()을 이용해서 어린 나무부터 반복문을 돌게끔 구현
나무 나이의 list가 봄을 지날때 나이를 먹는 나무와 죽는 나무가 많아서 pop()을 이용하기에는 시간이 너무 오래 걸릴것이라 생각
-> 새 리스트에 바뀐 나무 나이들을 저장하고, 그걸로 기존의 나이 리스트를 대체하자
봄과 여름을, 가을과 겨울을 묶어서 2중 for문을 2번만 사용하게끔 하면 시간을 줄일 수 있음 
'''
N, M, K = map(int, input().split())
A_list = [list(map(int, input().split())) for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

solid = [[5] * N for _ in range(N)]

delta_x = [0, 1, 0, -1, 1, 1, -1, -1]
delta_y = [1, 0, -1, 0, 1, -1, 1, -1]

for _ in range(K):      # K년동안 반복
    cnt = 0
    for i in range(N):      # 봄, 여름
        for j in range(N):
            if trees[i][j]:
                if len(trees[i][j]) >= 2:
                    trees[i][j].sort()      # 나무들의 나이를 오름차순으로 정렬
                dead_trees = 0      # 봄이 끝난 뒤 추가될 양분의 양
                new_trees = []
                for age in trees[i][j]:
                    if age <= solid[i][j]:
                        new_trees.append(age+1)
                        solid[i][j] -= age
                    else:
                        dead_trees += age // 2      # 봄이 끝난 뒤, 나무의 나이 // 2 만큼 양분으로 추가
                trees[i][j] = new_trees     # 나무의 나이를 재정립(살아남은 나무의 나이 + 1, 죽은 나무 제거)
                cnt += len(new_trees)
                solid[i][j] += dead_trees   # 양분 추가

    for i in range(N):      # 가을, 겨울
        for j in range(N):
            if trees[i][j]:
                for age in trees[i][j]:
                    if age % 5 == 0:      # 나무의 나이가 5의 배수라면
                        for dx, dy in zip(delta_x, delta_y):
                            nx = dx + i
                            ny = dy + j
                            if 0 <= nx < N and 0 <= ny < N:     # 땅을 벗어나지 않는 이내
                                trees[nx][ny].append(1)     # 주변 8칸에 나이가 1인 나무를 추가
                                cnt += 1

            solid[i][j] += A_list[i][j]

print(cnt)