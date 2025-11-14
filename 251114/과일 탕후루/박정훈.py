'''
1. 문제 분석
수열의 맨 앞과 맨 뒤를 제거해서, 총 숫자의 종류가 2개만 남도록 빼야함
과일을 최소한으로 빼서, 남은 수열의 길이를 출력

2. 풀이 방법 고안
일단 맨 앞과 맨 뒤를 제거해야 하기때문에 deque를 사용해야 할 것 같음

슬라이싱으로도 가능할까?
set()의 길이가 1 or 2이면, 탐색을 종료
탕후루의 길이가 가장 많아야 하기때문에, 탐색의 범위를 전체에서 점점 좁혀가는 식으로 해야함
cut = 0부터 해서 lst[cut:len(lst)] ~ lst[0:len(lst)-cut]을 탐색, cut += 1
-> 시간초과

탕후루에 꽃힌 과일은 0~9 사이의 수로 고정됨
그렇다면 0~9까지의 리스트를 만들어서, 그곳에 처음 각 수의 개수를 저장해두자
cut을 +=1하는 것은 같이 하되, 컷을 하는 범위에 따라서 수의 개수를 +1, -1해보자
'''
# N = int(input())
# num_lst = list(map(int, input().split()))
#
# if len(set(num_lst)) <= 2:
#     print(len(num_lst))
#     exit()
#
# cut = 1
# while True:     # cut = 3
#     for i in range(cut+1):      # num_lst = [1 2 3 4 5 6 7 8 9]    i = 0, 1, 2, 3
#         if len(set(num_lst[cut-i:len(num_lst)-i])) <= 2:
#             print(len(num_lst[cut-i:len(num_lst)-i]))
#             exit()
#     else:
#         cut += 1
def my_cnt():
    cnt = 0
    for i in idx:
        if i != 0:
            cnt += 1
    return cnt

N = int(input())
num_lst = list(map(int, input().split()))
idx = [0] * 10

for i in num_lst:
    idx[i] += 1

if my_cnt() <= 2:
    print(N)
    exit()

cut = 1
while my_cnt() > 2:     # cut = 3
    for i in range(cut):    # i = 0, 1, 2
        idx[num_lst[i]] -= 1
    if my_cnt() <= 2:
        print(N-cut)
        break

    for i in range(cut):
        idx[num_lst[cut-i-1]] += 1
        idx[num_lst[-1-i]] -= 1
        if my_cnt() <= 2:
            print(N-cut)
            exit()

    for i in range(cut):
        idx[num_lst[-1-i]] += 1

    cut += 1