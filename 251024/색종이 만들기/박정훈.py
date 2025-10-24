'''
1. 문제 분석
한변의 길이 N은 2**7이하의 2의 제곱수
전체가 같은 색이 아니면, 4등분해서 반복(재귀)

2. 풀이 방법 고안
한변의 길이 N
4등분을 했을때, 각 사각형의 시작점은 (0, 0), (0, N//2), (N//2, 0), (N//2, N//2)
시작점과 한변의 길이를 바꾸면서, 재귀함수를 돌리면 될것같다.
'''
def find_paper(start, length):
    global white_cnt, blue_cnt

    x, y = start

    if length == 1:
        if arr[x][y] == 0:
            white_cnt += 1
        else:
            blue_cnt += 1
        return

    check = True
    for i in range(length):
        for j in range(length):
            if arr[x+i][y+j] != arr[x][y]:
                check = False
                break
        if not check:
            break

    if not check:
        find_paper((x, y), length // 2)
        find_paper((x, y + length // 2), length // 2)
        find_paper((x + length // 2, y), length // 2)
        find_paper((x + length // 2, y + length // 2), length // 2)
    else:
        if arr[x][y] == 0:
            white_cnt += 1
        else:
            blue_cnt += 1

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
white_cnt = 0
blue_cnt = 0

find_paper((0, 0), N)

print(white_cnt)
print(blue_cnt)