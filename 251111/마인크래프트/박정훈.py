'''
1. 문제 분석
인벤토리에 블럭이 B개 들어있음
땅을 평탄화시키는것이 목표
땅을 같은 높이로 만들기위해, 블럭을 설치하거나 부술 수 있음
블럭을 설치하는데는 1초가, 블럭을 부수는데는 2초가 걸림
인벤토리에 블럭이 없으면 설치 불가

2. 풀이 방법 고안
N * M * 땅의 높이의 최대는 500 * 500 * 256이므로 완전탐색 가능

현재 존재하는 모든 블럭의 수 // 전체 칸 수 =  가능한 최대 높이
 - 현재 존재하는 모든 블럭의 수 = 설치되어있는 블록들 + 인벤토리의 블록

소요시간이 동일하다면 더 높은 높이를 찾아야함
-> 높이가 높은 순으로 위에서부터 탐색

인벤토리의 블록이 0 또는 양수라면, 최소시간을 비교
'''
N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

sum_arr = 0
max_height = 0

for i in range(N):
    for j in range(M):
        sum_arr += arr[i][j]
        if max_height < arr[i][j]:
            max_height = arr[i][j]

# 최대높이와, arr의 숫자의 총합 + B의 가능 평균 높이 비교(가지치기)
target_search = min(max_height, (sum_arr + B) // (N * M))

cnt_result = float('inf')
height_result = 0

for target_height in range(target_search, -1, -1):
    cnt = 0
    inv = B
    for i in range(N):
        for j in range(M):
            gap_block = arr[i][j] - target_height
            if gap_block > 0:   # 좌표 블록의 높이 > 목표 높이
                cnt += gap_block * 2
                inv += gap_block
            if gap_block < 0:   # 좌표 블록의 높이 < 목표 높이
                cnt += abs(gap_block)
                inv -= abs(gap_block)

    if inv >= 0:
        if cnt < cnt_result:     # 같은 경우일 때, 더 높은 높이를 찾아야 하므로 등호 X
            cnt_result = cnt
            height_result = target_height

print(cnt_result, height_result)