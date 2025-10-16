"""
N * N 정사각형 격자 => board
격자 가장 아래칸 부터 쌓여있음.
-> stack-top, pop

1. 크레인을 좌우로 움직여서 가장 위 인형을 집어올림.
2. 집어 올린 인형은 바구니에 쌓임.
3. 이때 바구니의 가장 아래부터 인형이 순서대로 쌓임.
4. 바구니에 같은 인형 두개가 만나면 바구니에서 사라짐.
-> 인형 두개가 없어진 것.
5. 크레인을 모두 작동 시킨 이후, 사라진 인형의 개수를 반환.

조건
- 크레인 작동 시 인형이 집어지지 않는 경우는 없음. 
- 아무일도 일어나지 않음. 
- 바구니는 모든 인형이 들어갈 수 있을 만큼 충분히 큼.
- 크레인을 작동 시킨 위치가 담긴 배열 => moves

0 = 없음
1~5 = 같은 인형 번호
[0,0,0,0,0]
[0,0,1,0,3]
[0,2,5,0,1]
[4,2,4,4,2]
[3,5,1,3,1]
 1 2 3 4 5

 moves
 [1, 5, 3, 5, 1, 2, 1, 4]

"""

def solution(board, moves):
    stack = []
    pang = 0

    for move in moves:
        col = move -1   # 인덱스 번호로 맞추기. 0 1 2 3 4

        for row in range(len(board)):
            
            # 0이 아니면 = 인형이 있으면
            if board[row][col] != 0:
                board[row][col] = 0  # 인형 꺼냄

                # 만약 지금 넣은 top이랑 이전 top이 같으면 
                if stack and stack[-1] == board[row][col]:
                    stack.pop() # 제거 = 터뜨리기
                    pang += 2   # 제거할 때, 인형 2개씩 카운트
                # top 인형들이 같지 않다면     
                else:
                    stack.append(board[row][col]) # stack에 다음 인형 넣기
                board[row][col] = 0  # 인형을 stack에 넣으면, board에서 꼭 빼줘야함.
                break 
    return pang