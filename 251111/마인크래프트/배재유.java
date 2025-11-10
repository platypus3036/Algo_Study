

import java.util.*;
import java.io.*;

public class Main
{
    public static void main(String args[]) throws Exception
    {
    	
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    	
    	/*
    	 * 
    	 * 땅을 고르는 데 걸리는 시간과 땅의 높이
    	 * 
    	 * 가로세로높이 3차원
    	 * 땅의 높이를 동일하게 만드는 땅고르기
    	 * 
    	 * 동작
    	 * 1) 좌표의 가장 위의 블록을 제거하여 인벤토리에 넣기
    	 * 2) 인벤토리에서 블록을 하나 꺼내어 좌표에 넣기
    	 * 
    	 * 1번 2초, 2번 1초
    	 * 
    	 * 땅의 높이는 256이 최대, 음수 불가, 기존 블록은 B개 기본값
    	 * 
    	 * N,M,B 
    	 * 
    	 * 인벤토리가 비어있다면 모든 좌표에서 블록을 하나씩 제거
    	 * 
    	 * 시뮬레이션
    	 * 
    	 * M,N -> 250000 400
    	 * 
    	 * 완탐 가능
    	 * 
    	 * 전체탐색
    	 * 균일화
    	 * 
    	 * 가장 많은 높이로 맞추기
    	 * 1. 블럭이 없다면
    	 * 전체 -1씩 낮추어  블록 확보
    	 * 2. 블럭 있다면 다 채우고 없애기
    	 * 각 동작에 대해서도 각각 cnt 확보
    	 * 
    	 * */
    	
    	StringTokenizer st = new StringTokenizer(br.readLine());
    	int N = Integer.parseInt(st.nextToken());
    	int M = Integer.parseInt(st.nextToken());
    	int B = Integer.parseInt(st.nextToken());

    	int[][] map = new int[N][M];
    	for(int i = 0; i<N; i++) {
    		st = new StringTokenizer(br.readLine());
    		for(int j=0; j<M; j++) {
    			map[i][j] = Integer.parseInt(st.nextToken());
    		}
    	}
		
		
		/*
		 * 엣지케이스
		 * 1. most 256, B = 0;
		 * 2. 0일떄는 애초에 나머지를 빼버려서 노상관
		 * 
		 * 엣지는 most 256, B = 0 일때
		 * 
		 * 
		 * 
		 * 
		 * 
		 * */
		
		
		
		int one_cnt = 0;
		int two_cnt = 0;
		int[] time = new int[257];
		Arrays.fill(time, Integer.MAX_VALUE);

		
		for(int i = 0; i<=256; i++) {

			one_cnt = 0;
			two_cnt = 0;
			int temp_B = B;
			for(int j =0; j<N; j++) {
				for (int k =0; k<M; k++) {
					if(map[j][k] > i) {
						temp_B += map[j][k] - i;
						one_cnt+= map[j][k] - i;
					}
				}
			}
			
			for(int j =0; j<N; j++) {
				for (int k =0; k<M; k++) {
					if(map[j][k] < i) {
						temp_B -= i - map[j][k];
						two_cnt+=i - map[j][k];
					}
				}
			}
			
			if(temp_B > -1) {
				time[i] = (one_cnt*2)+two_cnt;
			}
		}
		
		
		int min_time=Integer.MAX_VALUE;
		int max_height=0;
		for(int i = 256; i>-1; i--) {
			if(time[i] < min_time) {
				min_time = time[i];
				max_height = i;
			}
		}
			
			
		
		
		bw.write(min_time+" "+max_height);
		
		
    		
    		
    		
    		
    	
    	
    	
    	

    	
    	bw.flush();
    	bw.close();
         
    }
}
