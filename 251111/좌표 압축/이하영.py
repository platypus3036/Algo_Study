import sys
sys.stdin = open('input.txt')

"""
?
각 좌표가 전체 좌표 중 몇번째로 작은 값인지 구하기.

숫자를 작은 순서대로 정렬. (중복 제거)
정렬된 순서에 0번부터 부여.

원래
[2, 4, -10, 4, -9]

중복 제거 후 정렬
[-10, -9, 2, 4]


압축값 = 작은 순으로 번호 부여 0~9
-10은 가장 작으니까 압축값 0
-9는 그 다음이니까 압축값 1
2는 세 번째로 작으니까 압축값 2
4는 네 번째로 작으니까 압축값 3

얘를 다시 원래 값에 대입해서 
[2, 4, -10, 4, -9]
[2  3   0   3   1]

"""

N = int(input())
arr = list(map(int, input().split()))
# [2, 4, -10, 4, -9]

# 중복 제거 + 정렬 [-10, -9, 2, 4]
set_sort = sorted(list(set(arr)))

# 원래 배열 순서에 맞게 번호 넣어서 출력
result = []
for x in arr: # 원래 배열 [2, 4, -10, 4, -9]
    # x가 set_sort에서 몇 번째인지 찾기
    for i in range(len(set_sort)): # [-10, -9, 2, 4] = 0 1 2 3 
        if set_sort[i] == x: # [-10, -9, 2, 4] 정렬된 거에 i번째가 x랑 같은지 확인
            result.append(i) # 원래 배열의 x값을 정렬된 i인덱스 번호로 넣기. 
                             # => x 순서대로 i를 결과에 저장.
            break

print(*result)


"""
왜 또 시간초과..

1. 이중 for문 
2. 문제 범위가 너무 큼
1 ≤ N ≤ 1,000,000
-109 ≤ Xi ≤ 109

- 딕셔너리 또는 이진탐색.. 

""" 
# 딕셔너리

N = int(input())
arr = list(map(int, input().split()))

# 중복 제거 + 정렬
set_sort = sorted(set(arr))

# 값 → 좌표압축값 딕셔너리
# 각 고유 값이 압축값이 무엇인지 미리 만들어놓고, O(1)로 조회
result = {}
for i in range(len(set_sort)):
    result[set_sort[i]] = i # 바로 매핑. 정렬된 리스트 i번째 = 압축값은 i임.
"""
i  set_sort   result
0   -10       result[-10] = 0
1   -9        result[-9] = 1
2    2        result[2] = 2
3    4        result[1] = 3

"""
result = [result[x] for x in arr]
print(*result)
