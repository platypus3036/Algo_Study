import sys
sys.stdin = open('input.txt')

"""
숫자 = 1~25 


철수 빙고판
11 12 2  24 10
16 1  13 3  25
6  20 5  21 17
19 4  8  14 9
22 15 7  23 18
숫자를 부를때 지우기 = 방문 체크
숫자를 몇번 부를때 빙고가 되는지? = 카운트

사회자 부르는 번호.
5  10 7  16 2
4  22 8  17 13
3  18 1  6  25
12 19 23 14 21
11 24 9  20 15

가로로 한 줄씩 순서대로 => 1차원 리스트로 바꿔서 쉽게 읽기.
    sum([list(map(int, input().split())) for _ in range(5)], [])
    5개 5줄의 리스트를 모두 더해서 하나의 리스트로 만듦.
    [] + [5,10,7,16,2] + ... 
    => [5, 10, 7, 16, 2, 4, 22, 8, 17, 13, ... ]


빙고 : 가로줄, 세로줄, 대각선 => 각 5개의 모든 수가 지워지는 경우.
3줄 이상이 되면 빙고이므로 그만 세기.

1. 빙고판 탐색. 
-> 숫자 부를때 마다 완탐. 최대 25 * 25 = 625번 비교
-> 좌표 번호로 탐색.
   0  1  2  3  4 
0  11 12 2  24 10
1  16 1  13 3  25
2  6  20 5  21 17
3  19 4  8  14 9
4  22 15 7  23 18

좌표 번호 저장
pos = {
  11: (0, 0), 12: (0, 1),  2: (0, 2), 24: (0, 3), 10: (0, 4),
  16: (1, 0),  1: (1, 1), 13: (1, 2),  3: (1, 3), 25: (1, 4),
   6: (2, 0), 20: (2, 1),  5: (2, 2), 21: (2, 3), 19: (2, 4),
   4: (3, 0), 22: (3, 1), 15: (3, 2),  7: (3, 3),  9: (3, 4),
  14: (4, 0), 23: (4, 1), 18: (4, 2), 17: (4, 3),  8: (4, 4)
}

사회자가 5를 부르면, (2,2)에 있음을 바로 알 수 있음.
number = 5  
x, y = pos(number)

- 부르고 나면, 체크하기 True로 바꿈.
- 숫자 체크할 때 마다, 카운트 
"""
# 함수부
def BINGO(Cheolsoo_board, host_numbers):
# 각 숫자의 좌표 딕셔너리에 저장 (찾기 빠르게)
    pos = {}
    for x in range(5):
        for y in range(5):
            pos[Cheolsoo_board[x][y]] = (x, y)  # 즉시 좌표 알 수있음.


    visited = [[False]*5 for _ in range(5)]  # 함수 안에서 참조! 
    count = 0   # 몇 번 불렀는지

    # 사회자 숫자 하나씩 부름
    for number in host_numbers:
        count += 1              # 부를때 마다 카운트
        x, y = pos[number]      # 사회자가 부른 숫자 위치 불러오기.
        visited[x][y] = True    # 빙고 체크


        # 3줄이 동시에 생기려면, 겹쳐서 최소 13개의 숫자(칸) 필요.
        # 최소 13개는 세어야 빙고 발생. ?????
        # 12개 미만은 검사할 필요가 없음.
        if count >= 12:    # 왜 12야 13이 아니라
            bingo = 0

            # 가로 5줄 확인
            for i in range(5):
                if all(visited[i][j] for j in range(5)):
                    bingo += 1
            # 세로 5줄 확인
            for j in range(5):
                if all(visited[i][j] for i in range(5)):
                    bingo += 1

            # 대각선 2개 확인 (X자)
            # 왼쪽 위 시작 : (0,0), (1,1), (2,2), (3,3), (4,4) => [i][i] / 행열 같음.
            if all(visited[i][i] for i in range(5)): 
                bingo += 1
            # 오른쪽 위 시작 : (0,4), (1,3), (2,2), (3,1), (4,0) => 열 = 4-행
            if all(visited[i][4 - i] for i in range(5)):
                bingo += 1

            # 빙고 3줄 이상이면 종료
            if bingo >= 3:
                return count


# 실행부
Cheolsoo_board = [list(map(int, input().split())) for _ in range(5)]
host_board     = [list(map(int, input().split())) for _ in range(5)]
host_numbers = []
for row in host_board:
    for num in row:
        host_numbers.append(num)
# host_board = sum([list(map(int, input().split())) for _ in range(5)], [])
result = BINGO(Cheolsoo_board, host_numbers)
print(result)


"""
0. 대각선 규칙 찾기 
1. visited를 함수 밖에서 정의하고 있어서, 함수에서 사용하려 할 때, 참조 문제가 발생.
   -> 컴파일에러.
2. return count 해야함...
3. all : 조건이 모두 참인지 확인하는 내장함수.
   -> 행의 모든 열을 방문했는지 검사.
   -> 모든 칸이 True인가를 확인.
   -> 모든 칸이 True : 빙고 += 1
   -> 하나라도 False : 아직 빙고 아님.
4.  if count >= 13: 
   -> 13으로 하면 틀리고 12로 하면 맞음.
   -> 둘 다 출력은 15 나옴.

   13 -> 이론적으로 최소 3빙고가 가능한 숫자 -> 수학적 최소값
   12 -> 문제 입력에서 실제 3빙고가 나오는 시점. -> 정답 처리용
   이론적 최소 13 ≠ 문제에서 요구하는 최소 체크 시점

   다시

   3줄 빙고 = 최소 13개 숫자 필요.
   코드는 안전하게 12부터 체크. ???????
   실제 문제 입력과 테스트 케이스에서 12번째 숫자부터 검사해도 정답이 나오도록 하기 위한 안전장치

   count < 12  절대 3빙고 안나옴.
   count >= 12 3빙고 나올 가능성 있음.
   count >= 13 무조건 3빙고 나옴.

   12부터 검사를 할 뿐, 실제 3빙고는 13부터 나옴.


   그럼 13일 때 15출력 되는데, 왜 틀림처리 되는거??


"""