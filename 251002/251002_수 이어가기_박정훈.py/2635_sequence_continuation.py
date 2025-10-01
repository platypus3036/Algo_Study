N = int(input())
max_cnt = 2
max_cnt_list = []
for num in range(1, N+1):
    num_list = []
    cnt = 1
    front = N
    back = num
    num_list.append(front)
    num_list.append(back)
    while back >= 0:
        cnt += 1
        new_back = front - back
        front = back
        back = new_back
        num_list.append(back)

    num_list.pop(-1)
    if max_cnt < cnt:
        max_cnt = cnt
        max_cnt_list = num_list

print(max_cnt)
print(*max_cnt_list)