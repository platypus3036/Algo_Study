bg = [[0] * 100 for _ in range(100)]

for _ in range(4):
    left_x, left_y, right_x, right_y = map(int, input().split())
    for i in range(left_x, right_x):
        for j in range(left_y, right_y):
            bg[i][j] = 1

result = 0
for bg_lst in bg:
    result += sum(bg_lst)

print(result)