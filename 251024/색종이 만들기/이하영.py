import sys
sys.stdin = open('input.txt')

"""
종이 크기 N * N
   예시 ) 8 * 8
        2, 4, 8, 16, 32, 64, 128 중 하나.

흰색 0
파란색 1

1. 전체가 같은 색이 아니면  N/2 * N/2 로 나눔.
    = 한 변이 N/2 인 정사각형 네게로 나누자. 
    = 즉, 크기가 N/2 * N/2 인 것.
    = 한 변의 길이 size / 2 해주면 됨. (size는 N부터 계속 줄어드는 길이)
    = 넓이를 4등분 == 한 변을 절반으로 나누자.


   전체를 계속 나눠야 함.
   전체가 같은색이 아니면 계속 반복. 조건이 만족할 때 까지 반복.  
   while 또는 재귀호출??
   while 사용하려면, stack으로 구현. = 재귀
   => 재귀가 깊어지거나, 메모리 제한 때문에 직접 관리해야할 때 while+stack 사용.
   
2. 종료 조건
   (1) 잘라진 종이 전체가 하얀색 또는 파란색일 때.
   (2) 하나의 정사각형이 되어 더 이상 나눌 수 없을때.


2. 하얀색, 파란색 색종이 개수 각각 출력.

"""

###################################################
# 재귀

N = int(input())
color_paper = [list(map(int, input().split())) for _ in range(N)]

# size : 정사각형 한 변의 길이 / 계속 달라지는 정사각형의 크기가 될 것임.
def divide(x, y, size):
    global white, blue

    # 첫번째 색 = 맨 왼쪽 위칸 색.
    first_color = color_paper[x][y]
    same = True # 영역이 전부 같은 색인지 판별 -> 다른 색 있으면 False.

    # 현재 정사각형 영역이 모두 같은 색인지 확인
    # x : 시작 행 인덱스
    # y : 시작 열 인덱스
    # size : 한 변의 길이 (현재 영역의 크기)
    for i in range(x, x + size): # 행 0~7
        for j in range(y, y + size): # 열 0~7
            
            # 현재 색이 -> 첫번째 색과 다르면
            if color_paper[i][j] != first_color: 
                same = False # 다르면 Flase로 바꿈.
                break   # 다른 색 발견하면 반복 종료.
                # 나머지 칸 까지 검사할 필요 없음. 어짜피 다른색 발견한 이상 무조건 나눠야 하기 때문.
                # 맨 처음 두칸이 이미 다르면, 나머지 모든 칸을 검사할 필요가 없음.
        
        # 위에 break는 안쪽 for문만 종료됨. 바깥 for문도 나와주기.
        # 이미 색 다르니까, 더 이상 돌지 않게.
        if not same:
            break

    # 종료 조건
    if same:  # 전부 같은 색이면 (size == 1 포함.)
        if first_color == 0: # 첫번째 색이 흰색이면 
            white += 1       # 흰색 +1 
        else:                # 파란색이면 
            blue += 1        # 파란색 +1
        return  # 함수 종료

    # 재귀 호출 : 색이 섞여있다면 4칸으로 나누기.
    # 지금 영역을 4등분 = 한 변의 절반 크기를 구함.
    # size = 한 변의 길이.
    # half = 한 변을 줄인 절반 길이. x축 줄이고, y축 줄이고.
    half = size // 2
    divide(x, y, half)               # 왼쪽 위 / 그대로 시작
    divide(x, y + half, half)        # 오른쪽 위 / y축 방향으로 half만큼 이동
    divide(x + half, y, half)        # 왼쪽 아래 / x축 방향으로 half만큼 이동
    divide(x + half, y + half, half) # 오른쪽 아래 / 두 방향 다 half만큼 이동
    # x,y = 각 정사각형의 시작 좌표.
    # 위치 옮겨가면서 4개의 half * half 영역을 검사하는 것. 

    """
    divide(0, 0, 8) = 좌표 0,0 / 크기 8*8
    검사 -> 색 섞임 -> 4등분
    divide(0, 0, 4)
    divide(0, 0, 2)
    divide(0, 0, 1)
    """


# 초기값
white = 0
blue = 0

# 호출 
divide(0, 0, N)  # size = N 으로 시작.
"""
N
N/2
N/4
N/8 
...
"""

print(white)
print(blue)

#########################################################
# while+stack


N = int(input())
color_paper = [list(map(int, input().split())) for _ in range(N)]

white, blue = 0, 0
stack = [(0, 0, N)]  # 시작점 (x, y, size)

while stack:
    x, y, size = stack.pop()
    first = color_paper[x][y]
    same = True

    # 현재 영역이 모두 같은 색인지 확인
    for i in range(x, x + size):
        for j in range(y, y + size):
            if color_paper[i][j] != first:
                same = False
                break
        if not same:
            break

    if same:  # 모두 같은 색이면 색 카운트
        if first == 0:
            white += 1
        else:
            blue += 1
    else:     # 섞여 있으면 4등분해서 stack에 추가
        half = size // 2
        stack.append((x, y, half))               # 왼쪽 위
        stack.append((x, y + half, half))        # 오른쪽 위
        stack.append((x + half, y, half))        # 왼쪽 아래
        stack.append((x + half, y + half, half)) # 오른쪽 아래

print(white)
print(blue)