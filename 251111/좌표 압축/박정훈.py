'''
1. 문제 분석
수직선 위의 N개의 좌표들이 입력으로 주어짐
최솟값을 0으로 바꾸고, 그 다음으로 큰 수는 1, 2, ...으로 바꿈

2. 풀이 방법 고안
index를 활용하려 했는데 수의 범위가 너무크다
문제에 나온 그대로 한번 풀어보자
-> 시간초과

서로 다른 좌표의 개수를 구해야함 -> 중복을 제거하고 탐색
sort를 통해 오름차순 정렬을 하고, enumerate로 index를 추출해서 넣어보자
-> 시간초과
2중 for문을 하기에는 시간복잡도가 너무 커짐

enumerate를 사용해서 idx와 num을 가져오되, 딕셔너리에 보관해보자
'''
# N = int(input())
# nums_list = list(map(int, input().split()))
# nums_set = set(nums_list)
# for num in nums_list:
#     cnt = 0
#     for set_num in nums_set:
#         if num > set_num:
#             cnt += 1
#     print(cnt, end=' ')

# N = int(input())
# nums_list = list(map(int, input().split()))
# sort_nums_set = sorted(set((nums_list)))
#
# for idx, num in enumerate(sort_nums_set):
#     for i in range(N):
#         if nums_list[i] == num:
#             nums_list[i] = idx
# print(*nums_list)

N = int(input())
nums_list = list(map(int, input().split()))
sort_nums_set = sorted(set((nums_list)))

idx_dict = {num: idx for idx, num in enumerate(sort_nums_set)}

result_list = [idx_dict[i] for i in nums_list]
print(*result_list)