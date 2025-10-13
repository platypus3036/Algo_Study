

import java.util.*;
import java.io.*;

public class Main {

	static int[][] moves = {
			{0,1},
			{1,0},
			{0,-1},
			{-1,0},
	};
	static int C;
	static int R;
    public static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        /*
         * 
         * 1. 목표
         * 대기 순서가 K인 관객에게 배정될 좌석 번호 (x,y)
         * 
         * 2. 조건
         * 0-idx 아니다
         * y부터 증가 
         * 
         * y가 꽉차면 우측으로
         * 우측 다되면 아래 아래가 다되면 => 시계방향으로 돌면서
         * 
         * C,R <= 1000
         * K<= 100000000
         * 완탐 시간복잡도 ? 아슬아슬하다
         * 
         * 일단 해보고 안되면 다른 방법 찾아보자
         * 
         *  
         * */
        StringTokenizer st = new StringTokenizer(br.readLine());
        C = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        
        int[][] map =new int[C+1][R+1];
        int N = Integer.parseInt(br.readLine());
        int dir = 0;
        int x = 1;
        int y = 1;
        int idx = 1;
        map[1][1] = 1;
        while(idx < N && idx < R*C) {
        	int nx = x+moves[dir][0];
        	int ny = y+moves[dir][1];
        	if(isValid(nx,ny) && map[nx][ny] == 0) {

        		map[x][y] = idx;
        		idx++;
        		x = nx;
        		y = ny;
        	} else {
        		dir= (dir+1)%4;
        	}
        }
        if (N > R*C) {
        	bw.write("0");
        } else {
        	bw.write(String.format("%d %d", x,y));
        }
       

    	bw.flush();
    	bw.close();
    }
    
   
    public static void main(String[] args) throws Exception {
        solution();
    }
    
    public static boolean isValid(int x, int y) {
    	return 1<= x && x<=C && 1<=y && y <=R;
    }

}
