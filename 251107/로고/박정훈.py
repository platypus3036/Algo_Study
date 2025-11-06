'''
1. 문제 분석
연필을 내리면 선을 그리는 모드, 연필을 올리면 모드 해제
거북이는 (0, 0)에서 시작해서 위쪽을 보고있고, 연필을 내리고있음
x1, y1, x2, y2로 이루어진 직사각형을 그리는데 필요한 연필을 올리는 명령의 출력

2. 풀이 방법 고안
사각형이 붙어있는지 떨어져있는지를 판단해야 함
한점이라도 연결되어있으면, pu를 할 필요가 x
한 사각형 안에 다른 사각형이 완전히 들어가있으면 연결되지 않은것으로 처리

범위로 하면 포함관계를 판단하기 어려움
사각형의 변만을 저장할 수 있을까?

처음 두 개의 사각형이 완전히 떨어져있더라도,
다른 사각형이 두 개의 사각형과 각각 붙어버리면
세 사각형은 하나의 도형으로 처리해야 함

각각의 사각형에 대해, 그 사각형과 범위가 겹치는 사각형을 탐색
union-find처럼 연결시켜보자
마지막으로, 사각형의 변이 (0, 0)을 지나는 사각형이 하나도 없으면 cnt += 1
'''
def make_set(n):
    return [i for i in range(n)]


def find_set(x):
    if parent[x] == x:
        return x

    parent[x] = find_set(parent[x])
    return parent[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x < y:
        parent[y] = parent[x]
    else:
        parent[x] = parent[y]

def is_separate(tuple_1, tuple_2):  # 겹치지 않고 완전히 분리되어있는지
    x1, y1, x2, y2 = tuple_1
    new_x1, new_y1, new_x2, new_y2 = tuple_2

    return x2 < new_x1 or x1 > new_x2 or y2 < new_y1 or y1 > new_y2

def is_donut(tuple_1, tuple_2):     # 한 사각형이 다른 사각형을 겹치지 않고 완전히 포함하는지
    x1, y1, x2, y2 = tuple_1
    new_x1, new_y1, new_x2, new_y2 = tuple_2
    # tuple1가 밖, tuple2이 밖
    return (x2 > new_x2 and x1 < new_x1 and y2 > new_y2 and y1 < new_y1) or (x1 > new_x1 and x2 < new_x2 and y1 > new_y1 and y2 < new_y2)


N = int(input())
parent = make_set(N+1)      # N번은 (0, 0)
square_list = []
include_zero = False

for square_idx in range(N):
    square = tuple(map(int, input().split()))
    square_list.append(square)

    x1, y1, x2, y2 = square
    if (x1 == 0 or x2 == 0) and y1 <= 0 <= y2 or (y1 == 0 or y2 == 0) and x1 <= 0 <= x2:
        include_zero = True

    if not include_zero:
        x1, y1, x2, y2 = square_list[square_idx]
        if (x1 == 0 or x2 == 0) and y1 <= 0 <= y2 or (y1 == 0 or y2 == 0) and x1 <= 0 <= x2:
            include_zero = True

    for i in range(len(square_list) - 1):    # 연결된 사각형이 있으면
        if not is_separate(square_list[i], square_list[square_idx]) and not is_donut(square_list[i], square_list[square_idx]):
            union(i, square_idx)

roots = {find_set(i) for i in range(N)}
result = len(roots)
if include_zero:
    result -= 1

print(result)