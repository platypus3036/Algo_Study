import java.util.*;

class Solution {
    public int solution(int n, int w, int num) {
        
        /*
        
        몇 개의 상자를 꺼내야 하는지
        
        한 층에 w개씩
        
        1. 조건
        꺼낸거는 set
        
        이거는 실제 꺼내서 제외시켜야 한다 = 0으로 처리하기
        
        배열로 처리 -> for문으로 탐색
        
        시간복잡도는 괜찮다
        
        일단 채우고 꺼내보자
        
        */
        
        int[][] map = new int[(n/w)+1][w];
        for(int i = 0; i<(n/w)+1; i++) {
            for(int j =0; j<w; j++) {
                if(i %2 ==0) {
                    if(i >1) {
                        map[i][j] = map[i-1][0]+1+j;
                    } else {
                        map[i][j] = j+1;
                    }
                } else {
                    map[i][j] = map[i-1][0]+(2*w-1)-j;
                }
            }
        }
        
        int answer = 0;
        for(int i = 0; i<map[0].length; i++) {
            int cnt = 0;
            for(int j = map.length-1; j>-1; j--) {
                if(map[j][i] <=n) {
                    cnt++;
                }
                
                if(map[j][i] == num) {
                    answer=  cnt;
                    break;
                }
            }
        }
        
      

        return answer;
    }
}
