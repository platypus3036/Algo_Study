import sys
sys.stdin = open('input.txt')

"""
2차원 배열

무조건 첫째줄 숫자들 보다 한 칸 밑 숫자들이 큼. 
양옆은 비교 안함. 

N개 행 * 열
N번째로 큰 숫자 찾기

1. 2차원 배열을 1차원으로 받기
2. reverse 정렬
3. N번째 -1 index 꺼내기
-> for문 돌기
-> 안돌아도 됨!! arr[N-1]

= 시간초과 날까??
1 ≤ N ≤ 1,500
표에 적힌 수는 -10억보다 크거나 같고, 10억보다 작거나 같은 정수

1. extend 누적 O(N) 제일 빠름
2. 리스트 정렬 O(N log N) 오래 걸림.
3. 리스트 for문 돌기 O(N) 생각보다 빠름.

"""

def find_N_index(N, arr):
    arr.sort(reverse = True)
    answer = arr[N-1]
    return answer

N = int(input())
arr = []
for _ in range(N):
    arr.extend(map(int, input().split()))
    result = find_N_index(N, arr)
print(result)

"""
시간이 아니라
메모리 초과가 남.

1. 입력 받을때 마다 정렬을 해서. O(M log M)
2. arr 크기가 커서. 최대 1500 * 1500 = 2,250,000


해결 방법
1. 전체 arr을 저장하지 말고 N번째 큰 값만 찾기.

"""

N = int(input())
arr = []
for _ in range(N):
    arr.extend(map(int, input().split()))
arr.sort(reverse=True)
print(arr[N-1])

# 여전히 arr이 너무 큼. 

#######################
"""
arr저장 안하고
N번째 큰 수만 찾기
=> heapq

항상 크기 N짜리 heap만 유지하지 때문. O(N)
N ≤ 1500 → heap 메모리 거의 안 듦

"""

import heapq

N = int(input())
heap = []

for _ in range(N):
    for num in map(int, input().split()): 
    # 입력 받으면서 바로 num에 돌림.

        # 정렬 대신 N에 비교하는 조건문.
        # 힙이 N보다 작으면, N까지만 채워짐. 
        if len(heap) < N:
            heapq.heappush(heap, num)
        else: # 힙이 N개 이상이면(다 채워졌으면)
            # N개 보다 큰 숫자만 받아야함. 
            # num이 힙 최소보다 클 때
            if num > heap[0]:
                heapq.heapreplace(heap, num)
                # 제일 작은 값이랑 num이랑 교체함. 
                # N개의 가장 큰 숫자만 유지함. 

print(heap[0])  # N개의 큰 숫자들 중에 N번재 숫자는 제일 작은 수임. 
