import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        /*
        1. 목표
        크레인을 모두 작동시킨 후 터트려 사라진 인형의 개수
        
        2. 조건
        모든 인형은 아래칸부터 차곡차곡
        같은 모양의 인형 두개가 바구니에 연속해서 쌓이면 터진다
        인형이 없는 곳에 크레인 작동시키면 무반응
        
        board NxN N<=30
        각 칸에는 정수 <=100
        moves 배열 1000<=
        
        조건 딱히 없다 -> 구현에만 
        moves 도 0-idx 아니다 -> +1하던 -1하던 따지자
        
        3. 구현
        
        시뮬레이션
        1) list에 인형 옮기기
        2) 인형 터트리기
        
        1) list 옮기기
        각 x 정해지면 for문 돌면서
        if board[][] != 0이면 그 자리 0 만들고, list에 해당 인형 삽입
        
        1000 * 30
        30000 다 탐색해봐야 30000
        시간복잡도 신경 X
        
        2) 인형 터트리기
        중복 인형 터트리기
        근데 인형 넣을때마다 확인하면 굳이 따로 탐색 안해도 될 듯
        이러면 list가 아닌 stack이나 deque으로 확인
        
        
        */
        
        int depth = board.length;
        int answer = 0;
        Deque<Integer> q= new ArrayDeque<>();
        for(int i = 0; i<moves.length; i++) {
            //1. 탐색 x idx 0-idx로 변환
            int search_x = moves[i]-1;
            for(int j= 0; j <depth; j++) {
                //인형 나올 때까지 탐색
                if(board[j][search_x]!=0) {
                    //여기서 바로 확인하기
                    if(!q.isEmpty() && q.peekLast() == board[j][search_x]) {
                        q.pollLast();
                        answer+=2;
                    } else {
                        q.add(board[j][search_x]);
                    }
                    //공통적으로 가져오는 행위는 동일하게
                    board[j][search_x] = 0;
                    break;
                }
            }
        }
        
        
        return answer;
    }
}