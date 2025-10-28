'''
1. 문제 분석
양 손가락의 위치가 주어지고, 주어진 문자열을 출력하는데 걸리는 시간의 최솟값을 출력
자음쪽 자판은 왼손으로, 모음쪽 자판은 오른쪽으로 입력

2. 풀이 방법 고안
자음과 모음의 arr을 각각 설정하고, 좌표에 따른 이동거리를 계산
'''
sl, sr = input().split()
word = input()

left = "qwertasdfgzxcv"
right = "yuiophjklbnm"

left_keyboard = ["qwert", "asdfg", "zxcv "]
right_keyboard = [" yuiop", " hjkl ", "bnm   "]

for i in range(3):
    for j in range(5):
        if left_keyboard[i][j] == sl:
            sl_x = i
            sl_y = j

for i in range(3):
    for j in range(6):
        if right_keyboard[i][j] == sr:
            sr_x = i
            sr_y = j

time = 0

for char in word:
    if char in left:
        check = True
        for i in range(3):
            for j in range(5):
                if left_keyboard[i][j] == char:
                    time += abs(sl_x - i) + abs(sl_y - j) + 1
                    sl_x = i
                    sl_y = j
                    check = False
                    break
            if not check:
                break

    elif char in right:
        check = True
        for i in range(3):
            for j in range(6):
                if right_keyboard[i][j] == char:
                    time += abs(sr_x - i) + abs(sr_y - j) + 1
                    sr_x = i
                    sr_y = j
                    check = False
                    break
            if not check:
                break

print(time)