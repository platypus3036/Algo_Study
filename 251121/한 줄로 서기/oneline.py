import sys
sys.stdin = open('input.txt')

"""
N명의 사람 -> 한 줄로 줄 섬. 

같은 키는 없음. 
키가 작은 사람 부터 줄을 세움.
자신 보다 큰 사람은 왼쪽에 몇 명 있어야 함. 
왼쪽에 큰 사람이 몇명인지 기억함.  
=> 그 수 만큼 빈자리를 두고 배치해야함. 


line = 키 1 ~ 4 순서대로, 자기보다 큰 사람이 왼쪽에 몇 명인지. 
       2 1 1 0
       1 왼쪽에 2명
       2 왼쪽에 1명
       3 왼쪽에 1명 
       4 왼쪽에 0명

= 왼쪽에 아무도 없는 4가 첫번재
4 0 0 0 

= 왼쪽에 2명이라는 1이 3번째
4 0 1 0

= 왼쪽에 1명인 2, 3 
= 순서는?
4 2 1 3 또는
4 3 1 2 

하지만 두번째는 
2 자기 왼쪽에 큰 사람이 1명이 아니게 됨. (2명)
그래서 순서는 4 2 1 3
"""

N = int(input())
line = list(map(int, input().split()))

result = [0] * N

# 키가 작은 사람부터 배치 (1 ~ N)
for height in range(1, N+1):
    count = line[height-1]  # 왼쪽에 있어야 하는 키 큰 사람 수
    empty = 0

    # 빈 자리 중 count 번째 빈 자리에 넣는다
    for i in range(N):
        if result[i] == 0:  # 아직 자리 비어있으면
            if empty == count:
                result[i] = height
                break
            empty += 1

print(*result)
