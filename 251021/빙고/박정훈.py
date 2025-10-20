'''
1. 문제 분석
빙고가 총 3줄이 되면 종료
그때, 몇번째 수를 불렀는지를 출력

2. 풀이 방법 구상
숫자 하나를 부를 때 마다 빙고판을 탐색해서 빙고의 개수를 세는 방법
-> 숫자판이 5*5로 고정이기 때문에 시간은 충분

이미 부른 숫자와 그 위치를 기억해서, 빙고를 판별해야 함
부른 숫자의 위치를 기억할 0과 1로 구성된 2차원 리스트를 하나 더 만들자
'''

stage = [list(map(int, input().split())) for _ in range(5)]
bingo_numbers_lst = []
for _ in range(5):
    bingo_numbers_lst.extend(map(int, input().split()))
bingo_stage = [[0] * 5 for _ in range(5)]

result = 1
for num in bingo_numbers_lst:
    cnt = 0
    for i in range(5):
        bingo_check = True
        for j in range(5):
            if stage[i][j] == num:      # bingo_stage에 부른 숫자 위치를 기억
                bingo_stage[i][j] = 1

            if bingo_stage[i][j] == 0:      # 가로줄 빙고 검사
                bingo_check = False

        if bingo_check:
            cnt += 1

    for i in range(5):
        bingo_check = True
        for j in range(5):
            if bingo_stage[j][i] == 0:      # 세로줄 빙고 검사
                bingo_check = False

        if bingo_check:
            cnt += 1

    # 두 대각선 빙고 검사
    if bingo_stage[0][0] and bingo_stage[1][1] and bingo_stage[2][2] and bingo_stage[3][3] and bingo_stage[4][4]:
        cnt += 1

    if bingo_stage[0][4] and bingo_stage[1][3] and bingo_stage[2][2] and bingo_stage[3][1] and bingo_stage[4][0]:
        cnt += 1

    if cnt >= 3:    # 빙고가 3개 이상이라면, 검증 종료
        print(result)
        break

    result += 1
