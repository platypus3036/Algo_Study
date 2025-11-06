import sys
sys.stdin = open('input.txt')
import heapq


"""
해야하는 것. 
1. 배열에 자연수 x를 넣는다.
2. 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.

조건
1. x = 자연수. -> 배열에 x라는 값을 추가하는 연산
   x > 0      -> heapq.heappush(heap, x) 힙에 추가

2. x == 0     -> 배열에서 가장 작은 값을 출력 & 그 값을 배열에서 제거 
              -> heapq.heappop(heap)

음의 정수는 주어지지 않음. 

"""
def min_heap(math):
    heap = [] # 0이 아닐때 넣음. 
    save = [] # 결과를 저장해서 반환.

    for x in math:
        if x == 0:   # 0일 때 가장 작은값 출력. 제거.
            if heap: # 힙이 비어있지 않으면
                save.append(heapq.heappop(heap))
            else:    # 비어있으면 꺼낼 수가 없으니까 0
                save.append(0)
        else:
            heapq.heappush(heap, x) # 0이 아니면 걔를 힙에 넣음. 

    return save

N = int(input())
math = [int(input()) for _ in range(N)]
result = min_heap(math)

for rst in result: # 한 줄씩 줄바꿈
    print(rst)