import sys
sys.stdin = open('input.txt')

"""
N = 5 / 숫자 총 개수
5 1 1 2 1  /  숫자 5만 빼면 숫자 두 종류만 남음. = 남은 숫자 개수 4개

앞쪽 또는 뒤쪽에서 숫자를 몇 개만 빼서 
남은 숫자의 종류를 2개 이하만 남기기. 
stack, queue 말고 양쪽을 다 뺄 수 있는 deque사용

save = set(fruits)
if save == 2
2종류 이하로 남았을 때, 숫자가 총 몇개인지 구하기. 
print len(fruits)


"""
# from collections import deque



# def two_numbers(fruits):
#     seq = deque(fruits)
    
    
#     # 현재 숫자 종류가 2개 보다 많으면 계속 반복.
#     while len(set(seq)) > 2: 

#         # 현재 구간이 조건을 만족하면 길이를 기록하고 멈춤.
#         if len(set(seq)) <= 2:
#             max_len = max(max_len, len(seq))
#             break


#         # 양쪽 중 하나를 뺌.
#         left_remove = deque(seq)
#         left_remove.popleft()
#         right_remove = deque(seq)
#         right_remove.pop()

#         # 과일 종류가 2개 이하면 seq 갱신                             
#         if len(set(left_remove)) <= 2 :
#             seq = left_remove

#         elif len(set(right_remove)) <= 2:
#             seq = right_remove

#         else: 
#             seq.popleft()
#             seq.pop()

# # 숫자 개수 출력.



from collections import deque

def two_numbers(fruits):
    seq = deque(fruits)
    max_len = 0

    # queue를 줄여가며 조건을 만족할 때의 최대 길이 계산
    # 현재 구간이 조건을 만족하면 길이 기록하고 멈춤
    while seq:

        # 현재 구간에 들어있는 과일 종류의 개수를 셈.
        if len(set(seq)) <= 2:
            max_len = max(max_len, len(seq)) # 최대 수 갱신
            break  # 조건 만족 시 종료

        # 양쪽 중 하나를 잘라서 더 오래 살아남을 수 있는 쪽 선택
        left_remove = deque(seq)
        left_remove.popleft()
        right_remove = deque(seq)
        right_remove.pop()

        # 왼쪽을 자른 버전, 오른쪽을 자른 버전 둘 다 2종류인지 확인.
        # 둘 다 만족 할 수도 있음.
        if len(set(left_remove)) <= 2 and len(set(right_remove)) <= 2:
            # 이때 둘 다 2종류면 남은 길이가 더 긴 쪽 선택
            if len(left_remove) >= len(right_remove):
                seq = left_remove
            else:
                seq = right_remove

        
        # 왼쪽 자른 버전이 2종류 이하면 갱신
        elif len(set(left_remove)) <= 2:
            seq = left_remove
        
        # 오른쪽 자른 버전이 2종류 이하면 갱신
        elif len(set(right_remove)) <= 2:
            seq = right_remove
        
        # 양쪽 다 3종류 이상이면 양쪽에서 하나씩 제거
        else:   
            seq.popleft()
            seq.pop()

    return max_len


N = int(input())
fruits = list(map(int, input().split()))
result=two_numbers(fruits)
print(result)

"""
짜잔 시간초과 

기존 코드 : 양쪽에서 잘라가기.  O(n^2)
윈도우 슬라이딩 : 두 종류 이하를 유지하면서 범위를 확장시켜서 확인. O(n)

"""
# 윈도우 슬라이딩 풀이법 

def two_numbers(fruits):
    left = 0 # 윈도우 시작점
    fruit_count = {} # 윈도우 안에 과일이 몇개인지 기록할 딕셔너리
    max_len = 0 # 가장 긴 길이 저장.

    for right in range(len(fruits)): # 오른쪽 포인터를 0부터 끝까지 늘려가면서 확인. -> 과일을 하나씩 추가해보는 과정.
        fruit = fruits[right] # 늘려서 과일을 추가.
        fruit_count[fruit] = fruit_count.get(fruit, 0) + 1
        # 추가한 과일의 개수를 딕셔너리에 추가. 


        # 과일 종류가 2개 초과면 왼쪽 부터 과일을 하나 씩 제거.
        # 왼쪽 포인터를 한칸 오른쪽으로 옮기면서 범위를 좁힘. 
        # 2개 이하로 줄면 종료.
        while len(fruit_count) > 2:
            fruit_left = fruits[left] # 맨 왼쪽 제거할 과일을 가져옴.
            fruit_count[fruit_left] -= 1 # 제거

            # 만약 왼쪽 과일이 하나도 안남으면, 윈도우에서 완전히 사라졌다는 뜻.
            if fruit_count[fruit_left] == 0: 
                del fruit_count[fruit_left] # 과일 종류를 딕셔너리에서 삭제.
            left += 1 # 왼쪽 포인터를 한 칸 오른쪽으로 옮김.

        # 현재 윈도우 길이 갱신
        # right - left + 1 = 현재 구간의 길이 // 0번부터라서 그냥 빼면 칸의 간격만 나옴. 
        max_len = max(max_len, right - left + 1)


    return max_len


N = int(input())
fruits = list(map(int, input().split()))
print(two_numbers(fruits))

"""
# get : 딕셔너리 안에 key가 있으면 key값을. 없으면 0을 돌려달라.

fruit_count = {'apple': 3, 'banana': 2}
print(fruit_count.get('apple', 0))   # 3  (이미 있으니까 그 값을 돌려줌)
print(fruit_count.get('orange', 0))  # 0  (없으니까 기본값 0을 돌려줌)
"""