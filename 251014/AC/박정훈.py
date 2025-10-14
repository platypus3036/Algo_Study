'''
1. 문제 해석
R이 나오면, 배열의 맨 앞을 버리는 규칙에서 맨 뒤를 버리는 규칙으로 바뀜
-> deque의 popleft()와 pop()을 사용하면 시간을 단축시키는데 유리
리스트 형태로 입력되는데, 이를 풀어서 입력받는 과정이 필요함
-> 맨 앞의 '['와 맨 뒤의 ']'를 슬라이싱을 이용해 빼고, split을 이용해 숫자만 입력받아야 함
n이 0이 될 때 오류가 발생. n이 0일때와 아닐때를 분류해줘야함

2. 시간계산
n이 최대 100,000이니, 배열을 다시 작성하거나 append()를 사용하면 시간초과가 난다고 판단
-> deque를 사용

3. 풀이
R이 나오면 굳이 배열을 뒤집을 필요 없이, left=True를 두어서 맨앞과 맨뒤 중 어디를 뺄 것인지 방향을 정하면 됨
하지만 left=False인 상태로 배열이 종료되면, 마지막에 배열 전체를 뒤집어서 출력해주어야 함
마지막을 그냥 출력하니 런타임 에러가 발생 -> .join()을 이용해서 풀고 출력
'''

from collections import deque

T = int(input())
for tc in range(1, T+1):
    p = input()
    n = int(input())
    arr = input()
    if n > 0:
        arr_deque = deque(map(int, arr[1:-1].split(',')))
    else:
        arr_deque = deque()

    left = True
    result = []

    for func in p:
        if func == 'R':
            if left:
                left = False
            else:
                left = True
        if func == 'D':
            if len(arr_deque) >= 1:
                if left:
                    arr_deque.popleft()
                else:
                    arr_deque.pop()
            else:
                result = 'error'
                break

    if not left:
        arr_deque.reverse()

    if result != 'error':
        result = "[" + ",".join(map(str, arr_deque)) + "]"

    print(result)