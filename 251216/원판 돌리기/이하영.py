import sys
sys.stdin = open('input.txt')

"""
N개의 원판 / 1번 부터 N번의 원판
각 원판 마다 M개의 숫자 -> 원형으로 배치됨.
같은 인덱스(위치)에 있으면 위아래로 인접함.

회전 = T번
x의 배수 번호인 원판들만 회전함.
원형 구조이므로 회전 시 끝과 처음을 연결해줘야 함. 
좌우 이동 시 (i - 1) % M 

d 방향 
0 = 시계방향
1 = 반시계방향

k 회전 칸 수 


[규칙]
1. 인접하면서 같은 숫자를 제거
- 같은 원판 좌우 인접
- 다른 원판 상하 인접
- 같은 숫자가 2개 이상 인접하면 모두 제거 => 0으로 변경

2. 제거된 숫자가 하나도 없다면
- 0이 아닌 숫자들의 평균을 계산
- 평균보다 큰 수는   -1
- 평균보다 작은 수는 +1
- 평균과 같으면 변화 없음.


숫자를 제거하고 나서
원판에 남아있는 숫자들의 총 합을 출력함. 


[구현 시 주의]
1. 원형 배열이니까 다시 돌아오도록 좌우 이동 시 (i - 1) % M 
시계 방향 d=0
    plate = [1,2,3,4]
    k_mod = 1

    plate[-1:] -> [4]
    plate[:-1] -> [1,2,3]

    ==> [4,1,2,3]

반시계방향 d=1
    plate = [1,2,3,4]
    k_mod = 1

    plate[1:] -> [2,3,4]
    plate[:1] -> [1]

    ==> [2,3,4,1]



2. 제거해야하는 숫자를 동시에 제거해야 하므로 
    - 지워야 할 위치를 배열에 표시함.
    - 찾자마자 바로 지우면 다른 숫자들 비교가 잘못될 수 있음.
    - 원판 [1, 2, 2, 3]
    - 체크 [F, T, T, F]
    - 제거 [1, 0, 0, 3]

3. 평균 계산 시 0은 제외
4. 모든 숫자가 0일 경우 평균 계산 안함.  


"""

def rotate(N, M, T, board, commands):

    # 각 명령에서 x의 배수 원판, d방향, k회전 칸수 뽑음.
    for x, d, k in commands:

        # 1. 원판 회전
        for i in range(x - 1, N, x): # x배수 원판만 선택. 0번 인덱스부터 시작해하므로 x-1
            k_mod = k % M # 시작-끝 반복 되도록.
            if d == 0:  # 시계 방향 / 뒤에서 k_mod개를 떼서 앞에 붙임. => 뒤에 있던걸 앞으로 오게 한 것.
                board[i] = board[i][-k_mod:] + board[i][:-k_mod]
            else:       # 반시계 방향 / 앞에서 k_mod개를 떼서 뒤에 붙임. => 앞에 있던걸 뒤로 가게 한 것.
                board[i] = board[i][k_mod:] + board[i][:k_mod]

        # 2. 인접한 같은 숫자 체크
        removed = [[False] * M for _ in range(N)] # 제거할 위치 표시
        find = False  # 같은 숫자가 하나라도 발견됐는지 확인. 

        # 완탐
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0:  # 이미 0인거는 지워진거니까 넘어감.
                    continue

                # 좌우 비교
                for nj in [(j - 1) % M, (j + 1) % M]:
                    # 숫자가 같으면 제거 표시
                    if board[i][j] == board[i][nj]:
                        removed[i][j] = True
                        removed[i][nj] = True
                        find = True

                # 위아래 원판의 상하 비교
                for ni in [i - 1, i + 1]:
                    # 범위 안이고 숫자가 같으면 제거 표시. // 다른 원판을 보는거니까
                    if 0 <= ni < N and board[i][j] == board[ni][j]:
                        removed[i][j] = True
                        removed[ni][j] = True
                        find = True

        # 3. 제거, 평균 처리
        if find:  # 제거할 숫자가 있으면 체크된 칸만 한번에 0으로 변경
            for i in range(N):
                for j in range(M):
                    if removed[i][j]:  
                        board[i][j] = 0

        else: # 제거할 숫자 없으면 
            total = 0
            count = 0
            for i in range(N):
                for j in range(M):
                    if board[i][j] != 0: # 0을 제외하고 
                        total += board[i][j] # 합
                        count += 1 # 개수를 계산
            # 평균계산
            if count > 0:
                avg = total / count
                for i in range(N):
                    for j in range(M):
                        # 평균보다 크면 -1, 작으면 +1
                        if board[i][j] == 0:
                            continue
                        if board[i][j] > avg:
                            board[i][j] -= 1
                        elif board[i][j] < avg:
                            board[i][j] += 1

    # 계산이후 모든 원판 숫자 합 계산해서 반환.
    return sum(sum(row) for row in board)


N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)] # 원판 상태
commands = [tuple(map(int, input().split())) for _ in range(T)] # 회전 명령

result = rotate(N, M, T, board, commands)
print(result)
