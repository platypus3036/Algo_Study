"""
w = 상자 가로 개수
n = 상자 총 개수
num = 찾으려는 상자 번호

2 ≤ n ≤ 100
1 ≤ w ≤ 10
1 ≤ num ≤ n
=> 완탐 가능, 스택 탑 꺼내기 가능
O(n)이나 O(n^2) 정도는 충분히 처리



예시) w = 6, n = 22

      22 21 20 19
13 14 15 16 17 18
12 11 10  9  8  7
 1  2  3  4  5  6 

위로 꺾어서 오른쪽부터 왼쪽까지 또 한층 쌓고, 반복
제일 왼쪽 밑 0,0 ~ 0,w 까지 쌓고 위로 ^


문제 ) 자신의 택배 번호 num을 찾으려면 
    그 위에 있는 모든 상자를 꺼내야 함.
    8번 상자를 꺼내기 위해서는 20번, 17번 상자를 꺼내야함. 
    이때 꺼내야하는 상자의 총 개수? 3회
    (20, 17, 8) -> 꺼내야하는 상자에 내가 찾는 상자도 포함.

    

로직 아이디어

1. 상자 쌓기 (왼쪽 아래 부터)
- 왼쪽 위부터 늘여놓으면 한 열씩 볼때, 스택으로 꺼내기 어려울 것 같음.

    1-1. w 길이 만큼 범위를 설정. 안넘어가게. -> 범위 체크 필요
         배열의 x또는 y가 w만큼 이동하면 꺾어야함.

    1-2. w 길이 만큼 num을 행 으로 채우기
        
    1-3. 반대로 꺾어서 reverse로 한 줄 채우기
         수평으로 w만큼 한줄 채움,
         다음 줄 y+1 위로 올라가서 reverse로 한줄 채움,
         while로 num을 다 배치할 때 까지. 

 

2. 좌표 배열이 만들어지면, num의 좌표를 찾기

3. num좌표가 있는 열을 탐색

4. num까지 스택으로 top에서 다 뽑아내기

5. 스택으로 top을 꺼낼 때 마다 카운트
 
   5-1. 항상 top이 모두 채워져 있지 않음.



x 증가 -> 오른쪽으로 이동 + 1
x 감소 -> 왼쪽으로 이동 - 1
y 증가 -> 위로 이동 + 1
y 감소 -> 아래로 이동 -1
= dir 오른쪽으로 이동하려면 +1
= dir 왼쪽으로 이동하려면 -1 

x축은 좌↔우 방향 : 열로 보기
y축은 상↔하 방향 : 행으로 보기
arr[행y][열x]



""" 
import math

def solution(n, w, num):
    x = 0
    y = 0
    h = math.ceil(n/w)   # 높이. 배열 몇줄인지 / 올림 어케함.
    # 딱 나누어 떨어지는데도 +1을 하면 안됨. 
    arr = [[0] * w for _ in range(h)] # 가로로 w만큼 * h줄
    dir = 1 # 오른쪽으로 시작. 
    box_number = 1 # 박스 채울 숫자

    while box_number <= n :  # num이 n 이하일때만 반복. 이하일때만 계속 채우기. 

        # 1. 가로로 w칸 이동        
        for _ in range(w):
            arr[y][x] = box_number  # 현재 좌표에 숫자 넣고 증가시키기 
            box_number +=1 
            if box_number > n:     # 남은 박스가 없으면 break
                break

            # 다음 x 계산, 오른쪽 방향으로 이동
            new_x = x + dir 
            
            if not (0 <= new_x < w) : # 오른쪽 끝, 왼쪽 끝에 닿으면 break
                break
            x = new_x  # 이동마다 갱신

        # 2. 한 줄 다 채우면 위로 한 칸 이동
        y += 1     # 위로 올라가기
        if y >= h:
            break


        # 3. 방향 반전 = 부호뒤집기
        dir *= -1  
             
        # 4. 다음줄 시작하기 
        new_x = x + dir
        if 0 <= new_x < w:
            x = new_x 
        else:
            x = 0 if new_x < 0 else w -1

    # num 찾기
    look_y = look_x = -1  # 찾을 좌표 초기화

    for yy in range(h):
        for xx in range(w):
            if arr[yy][xx] == num:          # 배열에서 num을 찾으면 
                look_y, look_x = yy, xx     # 저장하고 반복 종료 looky,x = num 좌표
                break

        if look_x != -1:  # 초기값이 아니면 num 찾은거니까 종료
            break
    if look_x == -1:
        return 0

    # num있는 열에서 top 찾기 // 기존 배열 값인 0이 아니어야함.
    top_y = None  # 제일 위 top_y 찾기

    for yy in range(h):          # 위에서 아래로 탐색 -> 제일 위 top 찾기
        if arr[yy][look_x] != 0: # 해당 column의 y=yy 위치에 값이 존재하면 / 0이 아니면
            top_y = yy           # 값이 있으면 갱신
            break

    # pop 횟수 계산.
    # 제일 위에있는 top_y - num의 y좌표 + 1
    # num도 포함하기 위해 + 1
    pop_count = look_y - top_y + 1
    


    return pop_count


"""
시간초과 런타임에러

해결

가로 이동 루프가 w칸을 보장 못함.
x이동할때 방향 반전하면서 과정이 잘못됨.
    예시와 다르게 숫자가 채워짐.
pop_count 계산식 잘못됨
3 => 0
4 => -1 나옴
pop_count = top_y - look_y + 1
    이렇게 하면 음수 될 수 있음. 

"""
####################### 고친 코드

import math
def solution(n, w, num):
    h = math.ceil(n/w)   # 높이. 층 개수 (올림)
    arr = [[0] * w for _ in range(h)]  # y=0 = 바닥층
    box = 1  # 배열에 채울 숫자 

    # 지그재그로 배열 채우기 (바닥→위)
    for y in range(h):   # 0번 층 ~ h -1 층까지
        if y % 2 == 0:   # 짝수 : 왼→오
            x = 0
            dir = 1
        else:            # 홀수 : 오→왼
            x = w - 1
            dir = -1

        for _ in range(w):    # w만큼 반복해서 한 층에 숫자를 또 넣음. 
            if box > n: 
                break         # 더 이상 배치할 숫자가 없으면 종료.
            arr[y][x] = box   # 좌표에 숫자를 채우고 box값을 +1 함. 
            box += 1
            x += dir # x = 숫자 배치될 위치. dir 위치 이동(왼, 오)

    # num 좌표 찾기 / 완탐. 
    look_y = look_x = -1  # 초기값
    for yy in range(h):
        for xx in range(w):
            if arr[yy][xx] == num:       # 좌표에서 num을 찾으면 
                look_y, look_x = yy, xx  # 해당 위치를 저장, 반복문 종료 
                break
        if look_x != -1:
            break

    # 만약 num이 없다면
    if look_x == -1:
        return 0

    # 위층(top_y) 찾기: y=h-1에서 y=0까지 내려오면서 탐색
    top_y = None
    for yy in range(h - 1, -1, -1):
        if arr[yy][look_x] != 0:  # h-1부터 0까지 내려오면서 lool_x열에서 0이 아닌 첫번째 층을 찾음. 
            top_y = yy            # 이 층을 top으로 저장함. 
            break

    # pop 개수 = 위의 층 수 + 자기 자신
    # num이 있는 층부터 위로 몇층이 존재하는지 계산.
    pop_count = top_y - look_y + 1  

    return pop_count



#######################################지피티 코드
def solution(n, w, num):
    # 목표 상자의 행/열 계산
    row = (num - 1) // w
    pos = (num - 1) % w
    if row % 2 == 0:
        col = pos
    else:
        col = w - 1 - pos

    removed_above = 0
    max_row = (n - 1) // w
    for r in range(row + 1, max_row + 1):
        if r % 2 == 0:
            other_num = r * w + col + 1
        else:
            other_num = r * w + (w - col)
        if other_num <= n:
            removed_above += 1

    return removed_above + 1  # 위의 상자들 + 목표 상자

###################### 프로그래머스 다른사람 코드

# 수학적 규칙으로 풀어낸 버전. 
"""
지그재그로 숫자를 채우면, 특정 열(x)으로 숫자가 도착하는 숫자들은 일정한 패턴을 가짐.
w = 4라면
y=0 :  1  2  3  4
y=1 :  8  7  6  5
y=2 :  9 10 11 12
y=3 : 16 15 14 13

이때 x=1(두 번째 칸)에 오는 숫자는
2, 7, 10, 15, 18, 23, ...
이렇게 일정하게 증가함. 
= 2*w
한 번의 오르락 내리락 하는 사이클이 2 * w 칸이기 때문. 

"""
def solution(n, w, num):
    m1 = num%(w*2)  # num이 사이클 길이 2*w안에서 몇번째 위치인지 계산한 값. -> num이 주기의 어느 위치에 있는지 확인.
    m2 = ((w*2+1) - m1)%(w*2) # 지그재그 채우기 -> 짝수층, 홀수층 
    # num 이상 n 이하의 수들 중 2*w로 나눈 나머지가 m1,m2인 것들의 수를 세면 된다.
    return len(range(num,n+1,w*2)) + len(range(num + (m2-m1)%(w*2), n+1, w*2))
        # num과 같은 열에 쌓인 숫자들 중 아래부분 + num 위쪽의 지그재그 반대방향 홀수층으로 올라간 숫자들 셈. 
        # 같은 x열에 올라와있는 숫자 개수 = 꺼내야하는 박스의 수.


"""
num이 있는 열 x 위치에서 그 다음으로 같은 열에 나타나는 숫자를
직접 다음 숫자로 점프하면서 세는 방식. 

2 → 7 → 10 → 15 → 18 → 23 ...
점프 크기 규칙적. 
"""
def solution(n, w, num):

    answer = 0
    while True:
        num += 2 * (w - num % w) + 1 if num % w != 0 else 1  
        # 현재 숫자가 오른쪽으로 몇번째 칸인지 알아내기 / if문 : 오른쪽 끝까지 이동, 다시 왼쪽으로 갈아탐. / else 오른쪽 끝에이씅면 바로 +1 이동 
        answer += 1  # 한번 점프를 했으므로 num위에 박스가 있다는 뜻 = 제거할 박스 수 카운트 
        if (num > n): return answer  # n보다 큰 수가 나오면 더 이상 위에 박스 없음. = 점프 횟수 반환. 



def solution(n, w, num):
    top = (n-1)//w+1
    row = (num-1)//w+1
    col = (num-1)%w
    top_col = (n-1)%w
    if top%2==row%2:
        return top-row + (0 if top_col<col else 1)
    else:
        return top-row + (0 if top_col+col<w-1 else 1)