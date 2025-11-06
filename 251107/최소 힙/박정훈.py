'''
1. 문제 분석
입력으로 0이 주어지면, 배열의 최솟값을 출력하고 그 값을 배열에서 제거
입력으로 0이 아닌 수가 주어지면, 배열에 그 수를 추가
배열이 비어있는 상태에서 0이 주어지면 0을 출력

2. 풀이 방법 고안
일단 min과 sort을 사용해서 풀어보자  -> 시간초과

빈 리스트에 숫자를 넣으면서, 최솟값을 리스트의 맨 뒤로 옮기면
0이 나왔을 때 pop()만 하면 될 것 같음  -> 시간초과

heapq라는 모듈이 있었구나
'''
import sys
from heapq import heappop, heappush

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if heap:
            print(heappop(heap))
        else:
            print(0)
    else:
        heappush(heap, num)
'''
def my_sort():
    global num_list

    num_idx = len(num_list) - 1
    while num_list[num_idx] > num_list[num_idx - 1]:
        num_list[num_idx], num_list[num_idx - 1] = num_list[num_idx - 1], num_list[num_idx]
        num_idx -= 1
        if num_idx == 0:
            break

N = int(input())
num_list = []
for _ in range(N):
    num = int(input())
    if num == 0:
        if num_list:
            print(num_list.pop())
        else:
            print(0)
    else:
        num_list.append(num)
        if len(num_list) >= 2:
            my_sort()
'''