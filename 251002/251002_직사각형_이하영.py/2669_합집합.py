import sys
sys.stdin = open('input.txt')


def calc_area(rec):

    cells = set()                       # 빈 집합 set. -> 중복 칸 거르기.
    for x1, y1, x2, y2 in rec:          # x1, y1 = 왼 아래 / x2, y2 = 오른 위

        # 면적 구하기.
        for x in range(x1, x2):         # x1 = 2, x2 = 5 / x = 2, 3, 4    → 가로줄 3칸
            for y in range(y1, y2):     # y1 = 3, y2 = 7 / y = 3, 4, 5, 6 → 세로줄 4칸
                cells.add((x, y)) # cell에 넣기. 가로3번, 세로 4번 / 겹치는거 제외
                # cell = (2, 3), (2, 4) ... 12 묶음.
    return len(cells) # cell의 개수 = 총 면적과 같음.



rec = [list(map(int, input().split())) for _ in range(4)] # 4개 사각형
result = calc_area(rec)
print(result)