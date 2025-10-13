import sys
sys.stdin = open('input.txt')

"""
0. 인덱스 번호 +1 = 스위치, 자연수 번호
   자연수 번호 -1 = 인덱스 번호


1. 자연수 번호의 배수 찾기
range(start 자연수 번호, stop 스위치 개수 까지 , step 자연수 번호 만큼 뛰기.)
-> 스위치 개수는 +1 안해줘도 됨 : 인덱스 번호로 보고있어서!
3 6 9
2 4 6 8


2. 양 옆으로 확장하면서 대칭 확인하기
기준 : girl_num 자연수
(1) 좌우 대칭인지 확인
(2) 범위 넓여가면서 확인
(3) 대칭 깨지거나, 스위치 끝에 도달하면 스탑
(4) 해당하는 대칭 구간 모두 스위치 바꾸기

기준 인덱스 정하기 = girl_num -1 인덱스니까
왼쪽, 오른쪽 정하기
left  = idx - 1
right = idx + 1

양 옆으로 확장 = 조건에 맞으면 left, right 방향으로 한칸씩 가주기
조건 : 왼쪽은 0보다 같거나 클 것.
      오른쪽은 스위치개수 보다 작을 것. 
      왼쪽과 오른쪽이 같을 것. 

if문    => 기준점에서 양쪽 한 번 밖에 확인 못함. ㅜㅜ
while문 => 최대한 확장, 언제까지 확장할지 모르니까 while 써줘야 함.

"""

def switches_onoff(number_switch, switches, boy_num, girl_num):

    # 남학생 : 번호의 배수면 스위치 바꾸기
    for i in range(boy_num - 1, number_switch, boy_num):
        switches[i] = 1 - switches[i]



    # 여학생
    idx = girl_num - 1  # 기준 인덱스 = 자연수 -1 // 인덱스 번호로 보기 위함.
    left, right = idx - 1, idx + 1   # 기준 인덱스 -1 하면 왼쪽, +1 하면 오른쪽

    # 여학생 대칭 구간 넓히면서 확인. (언제까지 넓힐지 모르니까 while)
    # 왼쪽은 0번과 같거나 크고, 오른쪽이 마지막 보다 작을때,
    # 그리고 양쪽 값이 같을 때. 반복
    while left >= 0 and right < number_switch and switches[left] == switches[right]:
        left -= 1   # 한칸 왼쪽 확인
        right += 1  # 한칸 오른쪽 확인

    # 위 반복에서 대칭이 되면 -> 구간을 확장함. -> 다 보면 -1, 5 넘어감.
    # 다시 한칸씩 줄여줘야 실제 대칭 구간.
    left += 1
    right -= 1

    # 대칭 구간에서 스위치 바꾸기. / right 끝값 포함.
    for i in range(left, right + 1):
        switches[i] = 1 - switches[i]



    # 바뀐 스위치 반환.
    return switches



# 실행부 ##########################
number_switch = int(input())  # 스위치 개수
switches = list(map(int, input().split()))
students = int(input()) 
boy, boy_num = map(int, input().split())
girl, girl_num = map(int, input().split())
result = switches_onoff(number_switch, switches, boy_num, girl_num)


# 출력 
for i in range(0, len(result), 20):
    print(*result[i:i+20])  # 한 줄에 20개만 출력.


###################### 실패! 
# 학생 수가 꼭 2명 = 남학생, 여학생이 한명씩 있는게 아닐 수도 있다는 조건

def switches_onoff(number_switch, switches, gender, num):

    # 1 == 남학생, 2 == 여학생
    # 남학생일 때
    if gender == 1:  
        for i in range(num - 1, number_switch, num): # 자연수 배수
            switches[i] = 1 - switches[i]

    # 여학생일 때
    else:  
        idx = num - 1   # 기준점 
        left, right = idx - 1, idx + 1 # 왼쪽 -1, 오른쪽 +1 방향
        # 반복 조건 맞추고
        while left >= 0 and right < number_switch and switches[left] == switches[right]:
            left -= 1
            right += 1
        # 반복 조건에 맞을때, 대칭 범위를 확장함.
        # 근데 마지막 확장이 조건에 안맞을 수도 있으니까, 
        # 실제 대칭범위와는 다르니까 다시 줄여주기.
        left += 1
        right -= 1

        # 대칭에 들어가면 다 스위치 바꾸기.
        for i in range(left, right + 1):
            switches[i] = 1 - switches[i]

    # 바꾼 스위치 반환
    return switches


# 실행부 ##########################
number_switch = int(input())
switches = list(map(int, input().split()))
students = int(input())  # 학생 수
for _ in range(students): # 학생 수만큼 
    gender, num = map(int, input().split()) # 성별, 자연수
    switches = switches_onoff(number_switch, switches, gender, num)

for i in range(0, len(switches), 20):
    print(*switches[i:i+20])

