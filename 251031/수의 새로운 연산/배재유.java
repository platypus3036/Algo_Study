import java.util.*;
import java.io.*;
 
class Solution
{
     
    static int H;
    static int W;
    public static void main(String args[]) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
         
 
        /*
         * 
         * p별q 구하기
         * 
         * #좌표 -> 숫자
         * &숫자 -> 좌표
         * 
         * p별q = 해당 좌표의 값
         * 
         * 
         * */
         
        int T = Integer.parseInt(br.readLine());
        //미리 arr에 계산
        //시간 초과가 여기 좌표 볌위 설정 제대로 해서 처리
        //n범위가 100이나까 해봐야 140 단위
        int[][] arr=  new int[601][601];
        for(int n = 1; n<=500; n++) {
            //i=n
            //sum(n) 10000 20000 대략 140까지
            for(int x = 1; x<=n;x++) {
                int y = -x+1+n;
                arr[y][x] = (((n)*(n-1))/2)+x; 
            }
        }
         
        for(int tc = 1; tc<=T; tc++) {
            //미리 10000 10000까지 정해둔다 -> ? 
            //좌표는 저까지 아니다  num <= 20000
            //x,y <= 대략 [1000][1000] 널널하게
            //좌표의 값을 구하는 방법을
            //-x+2 1개 -x+3 2개 -x+4 3개
            /*
             * (-x+1)+n n개 x=1부터  -x+n>=1 까지
             * y= (-x+1)+n
             * 
             * n = y+x-1
             * 
             * n = 1
             * 
             * num = !이 아니라 sum()
             * 
             * num = (n*(n-1))/2 + x
             * 
             * (y+x-1)(y+x-2) /2  + x
             * 
             * 4,2
             * 
             * num = (5)*(4) /2 + 2 = 12
             * 
             * 맞다
             * 
             * 좌표는 
             * 
             * 1 = (n*(n-1))/2 +x 
             * = 
             * 
             * */
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int ay = 0;
            int ax = 0;
            int by = 0;
            int bx = 0;
            //a찾기
            for(int i = 1; i<=600; i++) {
                for(int j =1; j<=600; j++) {
                    if(arr[i][j] == a) {
                        ay = i;
                        ax = j;
                    } 
                    if (arr[i][j] == b) {
                        by = i;
                        bx = j;
                    }
                }
            }
            //여기서 좌표를 더하는데 범위 설정이 문제다
            int cy = ay+by;
            int cx = ax+bx;
            int answer = arr[cy][cx];
            bw.write(String.format("#%d %d\n", tc,answer));
             
             
             
        }
     
 
 
        bw.flush();
        bw.close();
             
    }
 
}
