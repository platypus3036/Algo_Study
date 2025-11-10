import sys
sys.stdin = open('input2.txt')

"""
맨 왼쪽위 좌표 0, 0

땅고르기 
1. 튀어나온 곳 없애기, B가 없을 경우 무조건   빼기 = 2초
    (없애서 B에 넣으라는데, 꼭 필요할까)
2. 인벤토리에서 B 꺼내서 빈 곳에 깔기        넣기 = 1초


모든 칸을 같은 높이로 만들어야함. 
땅의 높이는 256블록을 초과할 수 없다. -> h 257개까지 range로 돌리기.
h = 시도해보는 높이

걸리는 최소 시간, 땅의 최대 높이
만약 h별로 비교했을 때 시간이 같다면? = 더 높은 높이 출력


cut_pick 깎아서 없앤 블록 (B 인벤토리에 다시 넣음.)
must_use 높이를 맞추려면 써야할 블록 개수 (B 인벤토리에서 줄일거임.)

"""
def time_hieght(N, M, B, arr):
    # 최소 시간, 최대 높이 초기화 
    min_time = float('inf') 
    max_height = 0

    for h in range(257):  # 가능한 높이 0~256
        cut_pick, must_use = 0, 0

        for i in range(N):
            for j in range(M):
                height = arr[i][j]  # 좌표의 값은 블록의 높이.

                # height가 h보다 높으면 블록을 깎음.
                if height > h:
                    cut_pick += height - h
                # height가 h보다 낮으면 블록을 쌓음.
                elif height < h:
                    must_use += h - height

        # 인벤토리 + 깎은 블록 < 반드시 사용해야하는 블록 개수
        # 가진 블록보다 올려야하는 블록이 더 많으면 2번 조건은 불가능.
        if B + cut_pick < must_use:
            continue  


        # 시간 = h 높이로 땅을 고를 때 걸리는 총 시간
        # 1, 2번을 한 번에 할 수 도 있다는 전제
        time = (cut_pick * 2) + (must_use * 1)

        # 최소 시간이면 갱신, 또는 여러 h에서 시간이 같다면 더 높은 높이를 선택.
        if time < min_time or (time == min_time and h > max_height):
            min_time = time
            max_height = h

    return min_time, max_height


N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = time_hieght(N, M, B, arr)
print(*result)

"""
시간 초과

1. arr을 1차원으로 풀어서 보기
2. 입력을 input말고 sys.stdin.readline() 사용하기
3. min_time = float('inf')를 10 ** 9로 바꿔보기

"""

def time_height(N, M, B, arr):
    flat = [h for row in arr for h in row] # 1차원으로 풀기
    min_h = min(flat)
    max_h = max(flat)
    
    min_time = 10**9 # 최대값 작게 받기
    max_height = 0

    for h in range(min_h, max_h + 1): # for 문 줄임. N, M
        cut_pick, must_use = 0, 0

        for height in flat:
            if height > h:
                cut_pick += height - h
            elif height < h:
                must_use += h - height

        if B + cut_pick < must_use:
            continue

        time = (cut_pick * 2) + must_use

        if time < min_time or (time == min_time and h > max_height):
            min_time = time
            max_height = h

    return min_time, max_height


N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = time_height(N, M, B, arr)
print(*result)

"""
그래도 시간초과 남^^
"""