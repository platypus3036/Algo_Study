package algo;

import java.util.*;
import java.io.*;

public class Main {
	
	
    public static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        /*
         * 1. 목표
         * 직사각형들이 차지하는 면적
         * 
         * 2. 조건
         * 네 개의 직사각형
         * 밑변은 가로축에 평행
         * 1. 떨어짐 2. 겹침 3. 포함
         * 
         * 입력
         * 좌하 x,y, 우상 x,y 4번
         * 
         * 3. 구현
         * 주어진 좌표 돌면서 2중 for문 -> 겹침에 대한 두께 존재 x -> 사각형 넓이
         * 좌표 = 점 , 점이 아니라 넓이로 방문처리
         * 
         * 4. 변수, 자료구조
         * visited boolean[101][101]
         * int cnt 
         * 
         * */
        
        boolean[][] visited = new boolean[101][101];
        int cnt = 0;
        for(int i = 0; i<4; i++) {
        	StringTokenizer st = new StringTokenizer(br.readLine());
        	int sx = Integer.parseInt(st.nextToken());
        	int sy = Integer.parseInt(st.nextToken());
        	int ex = Integer.parseInt(st.nextToken());
        	int ey = Integer.parseInt(st.nextToken());
        	
        	//2 = 2~3, 3= 3~4 2->4 = 2~3, 3~4 
        	for(int j = sy; j<=ey-1; j++) {
        		for(int k= sx; k<=ex-1; k++) {
        			if(!visited[j][k]) {
        				visited[j][k] = true;
        				cnt++;
        			}
        		}
        	}
        	
        }
        
        bw.write(cnt+"");
    	bw.flush();
    	bw.close();
    }
    

    public static void main(String[] args) throws Exception {
        solution();
    }
}
