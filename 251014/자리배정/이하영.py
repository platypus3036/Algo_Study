import sys
sys.stdin = open('input.txt')

"""
좌표를 시계방향으로 돌아야 함.

이동 순서
1,1 시작
위 -> 오른쪽 -> 아래 -> 왼쪽

방향 전환 시점
1. 한 번 갔던 곳 안가고 방향전환 => 방문 체크 필요
2. 격자 범위 끝 부분. 안넘어가게. => 범위 체크 필요


로직 순서
1. 시작과 동시에 현재 좌표 방문 체크
2. 다음 좌표로 이동
3. 이동 할 때마다 count 세기
4. 격자 범위 체크, 방향 전환.
5. count == K 같아지면 종료.

- C * R 최대 좌석 수 보다 K 값이 더 크면 못들어 감.
=> 0 반환하고 종료.



[방향을 반복하는 방법]
dir_idx = (dir_idx + 1) % 4  
현재 이동 방향 = +1 해주면 다음 방향으로

위 -> 오른쪽 -> 아래 -> 왼쪽
0번    1번      2번    3번     반복!!


%4를 해주면 나머지로 계속 +1을 해줘도 다시 0으로 돌아올 수 있게됨.

0 % 4 = 0
1 % 4 = 1
2 % 4 = 2
3 % 4 = 3
4 % 4 = 0  ← 다시 0으로 돌아옴!
5 % 4 = 1
6 % 4 = 2
7 % 4 = 3
8 % 4 = 0

4방향이 계속 반복되게 해줌.

"""

def find_position(C, R, K):

    # 자리에 못들어 갈 때.
    if C * R < K: 
        return 0 
    
    # 방향 = 위, 오른쪽, 아래, 왼쪽
    dir = [[0,1],[1,0],[0,-1],[-1,0]] 

    # 현재 어느 방향으로 나아가고 있는지
    # 0번 : 위 / 1번 : 오른쪽 / 2번 : 아래 / 3번 : 왼쪽
    dir_idx = 0  

    # 방문 표시
    # 좌표가 1,1 부터 시작인데, 실제 인덱스는 0,0부터 라서 + 1 해줘야 함.
    visited = [[False]* (R+1) for _ in range(C+1)]


    x, y = 1, 1           # 시작 좌표
    visited[x][y] = True  # 현재 위치 방문 체크
    count = 1             # 현재 위치부터 1번으로 시작.

    # 반복 조건 = 번호가 K번 보다 작을때만 반복.
    # count == K 이면 종료.
    while count < K :  
        dx, dy = dir[dir_idx]
        nx, ny = x+dx, y+dy

        # 범위 벗어나거나, 방문한 자리면 방향 전환.
        if nx < 1 or nx > C or ny < 1 or ny > R or visited[nx][ny]:
            dir_idx = (dir_idx + 1) % 4   # 방향 : 0-1-2-3 반복.
            dx, dy = dir[dir_idx]         # 좌표 : 리스트[i번]
            nx, ny = x + dx, y + dy       # 이동

        x, y = nx, ny           # 현재 좌표 = nx, ny 업데이트
        visited[x][y] = True    # 방문체크 필수
        count += 1              # K 도달 위해 카운트 세주기.

    return (x, y)


T = int(input())
for tc in range(1, T+1):
    C, R = map(int, input().split())
    K = int(input())
    result = find_position(C, R, K)
    print(result)
    # if result == 0:  # 자리 없어서 0 반환해야 할 때.
    #     print(0)
    # else:            # 정상 좌표
    #     print(result[0], result[1])


# 백준 제출.
C, R = map(int, input().split())
K = int(input())
result = find_position(C, R, K)
if result == 0:  # 자리 없어서 0 반환해야 할 때.
    print(0)
else:            # 정상 좌표
    print(result[0], result[1])
