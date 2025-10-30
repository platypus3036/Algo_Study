'''
1. 문제 분석
배틀싸피와 같은 느낌의 문제이다

2. 풀이 방법 고안
입력을 str형태로 받으면 변경이 어려워서, 이중 리스트로 받는것이 편할것이다
'''
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    arr = [list("".join(input())) for _ in range(H)]
    N = int(input())
    move = input()
    # print(arr)

    for i in range(H):
        for j in range(W):
            if arr[i][j] == '^':
                tank = [i, j, 'up']
            elif arr[i][j] == 'v':
                tank = [i, j, 'down']
            elif arr[i][j] == '<':
                tank = [i, j, 'left']
            elif arr[i][j] == '>':
                tank = [i, j, 'right']

    for char in move:
        tank_x, tank_y = tank[0], tank[1]
        tank_dir = tank[2]

        if char == 'U':
            tank_dir = 'up'
            if 0 <= tank_x - 1 and arr[tank_x - 1][tank_y] == '.':
                arr[tank_x][tank_y] = '.'
                tank_x -= 1
            arr[tank_x][tank_y] = '^'
            tank = [tank_x, tank_y, tank_dir]

        elif char == 'D':
            tank_dir = 'down'
            if tank_x + 1 < H and arr[tank_x + 1][tank_y] == '.':
                arr[tank_x][tank_y] = '.'
                tank_x += 1
            arr[tank_x][tank_y] = 'v'
            tank = [tank_x, tank_y, tank_dir]

        elif char == 'L':
            tank_dir = 'left'
            if 0 <= tank_y - 1 and arr[tank_x][tank_y - 1] == '.':
                arr[tank_x][tank_y] = '.'
                tank_y -= 1
            arr[tank_x][tank_y] = '<'
            tank = [tank_x, tank_y, tank_dir]

        elif char == 'R':
            tank_dir = 'right'
            if tank_y + 1 < W and arr[tank_x][tank_y + 1] == '.':
                arr[tank_x][tank_y] = '.'
                tank_y += 1
            arr[tank_x][tank_y] = '>'
            tank = [tank_x, tank_y, tank_dir]

        elif char == 'S':
            if tank_dir == 'up':
                for idx in range(tank_x, -1, -1):
                    if arr[idx][tank_y] == '#':
                        break
                    elif arr[idx][tank_y] == '*':
                        arr[idx][tank_y] = '.'
                        break

            elif tank_dir == 'down':
                for idx in range(tank_x, H):
                    if arr[idx][tank_y] == '#':
                        break
                    elif arr[idx][tank_y] == '*':
                        arr[idx][tank_y] = '.'
                        break

            elif tank_dir == 'left':
                for idx in range(tank_y, -1, -1):
                    if arr[tank_x][idx] == '#':
                        break
                    elif arr[tank_x][idx] == '*':
                        arr[tank_x][idx] = '.'
                        break

            elif tank_dir == 'right':
                for idx in range(tank_y, W):
                    if arr[tank_x][idx] == '#':
                        break
                    elif arr[tank_x][idx] == '*':
                        arr[tank_x][idx] = '.'
                        break

        tank = [tank_x, tank_y, tank_dir]

    print(f'#{tc} ', end="")
    for i in range(H):
        print("".join(arr[i]))
