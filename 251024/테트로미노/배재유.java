
import java.util.*;
import java.io.*;

class Main
{
	
	static int max = 0;
 	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		/*
		 * 
		 * 1. 목표
		 * 테트로미노가 놓인 칸에 쓰여잇는 수들의 합을 최대로하기
		 * 
		 * 2. 조건
		 * 점사각형은 겹치면 안된다
		 * 도형은 모두 연결되어있다
		 * 정사각형의 변끼리 연결되어 있어야 한다
		 * 
		 * NxM
		 * 
		 * 3. 구현
		 * 폴리오미노  각 종류마다 다 탐색돌려서
		 * NxM <= 250000
		 * 그냥 완탐돌려서 
		 * 
		 * 완전 순수 구현문제
		 * 
		 * 1) 직선
		 * 가로 /세로
		 * 
		 * 2) 네모
		 * 1가지
		 * 
		 * 3) 1번 꺾임
		 * 4방향
		 * 3x2 4가지
		 * 2x3 4가지
		 * 
		 * 4) 2번 꺾임
		 * 동일하게
		 * 3x2 2가지
		 * 2x3 2가지
		 * 
		 * 5) ㅗ
		 * 이것도 
		 * 3x2 2가지
		 * 2x3 2가지
		 * 
		 * 
		 * */
		
		StringTokenizer st=  new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		int[][] map = new int[N][M];
		for(int i = 0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<M; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		//1) 직선
		//가로
		for(int i = 0; i<N; i++) {
			for(int j=0; j<M-3; j++) {
				int temp = map[i][j]+map[i][j+1]+map[i][j+2]+map[i][j+3];
				max =Math.max(temp, max);
			}
		}
		//세로
		for(int i = 0; i<N-3; i++) {
			for(int j=0; j<M; j++) {
				int temp = map[i][j]+map[i+1][j]+map[i+2][j]+map[i+3][j];
				max =Math.max(temp, max);
			}
		}
		
		//2) 네모
		for(int i = 0; i<N-1; i++) {
			for(int j=0; j<M-1; j++) {
				int temp = 0;
				temp+=map[i][j];
				temp+=map[i+1][j];
				temp+=map[i][j+1];
				temp+=map[i+1][j+1];
				max = Math.max(temp, max);
			}
		}
		
		//3) 1번꺾임
		//세로
		for(int i = 0; i<N-2; i++) {
			for(int j=0; j<M-1; j++) {
				int temp1 = map[i][j]+map[i+1][j]+map[i+2][j]+map[i+2][j+1];
				int temp2 = map[i][j]+map[i+1][j]+map[i+2][j]+map[i][j+1];
				int temp3 = map[i][j+1]+map[i+1][j+1]+map[i+2][j+1]+map[i][j];
				int temp4 = map[i][j+1]+map[i+1][j+1]+map[i+2][j+1]+map[i+2][j];
				max = Math.max(max, Math.max(Math.max(temp1, temp2), Math.max(temp3, temp4)));
			}
		}
		
		//가로
		for(int i = 0; i<N-1; i++) {
			for(int j=0; j<M-2; j++) {
				int temp1 = map[i][j]+map[i][j+1]+map[i][j+2]+map[i+1][j];
				int temp2 = map[i][j]+map[i][j+1]+map[i][j+2]+map[i+1][j+2];
				int temp3 = map[i+1][j]+map[i+1][j+1]+map[i+1][j+2]+map[i][j];
				int temp4 = map[i+1][j]+map[i+1][j+1]+map[i+1][j+2]+map[i][j+2];
				max = Math.max(max, Math.max(Math.max(temp1, temp2), Math.max(temp3, temp4)));
			}
		}
		
		//4) 2번 꺾임
		//세로
		for(int i = 0; i<N-2; i++) {
			for(int j=0; j<M-1; j++) {
				int temp1 = map[i][j]+map[i+1][j]+map[i+1][j+1]+map[i+2][j+1];
				int temp2 = map[i][j+1]+map[i+1][j+1]+map[i+1][j]+map[i+2][j];
				max = Math.max(max, Math.max(temp1, temp2));
			}
		}
		//가로
		for(int i = 0; i<N-1; i++) {
			for(int j=0; j<M-2; j++) {
				int temp1 = map[i][j]+map[i][j+1]+map[i+1][j+1]+map[i+1][j+2];
				int temp2 = map[i+1][j]+map[i+1][j+1]+map[i][j+1]+map[i][j+2];
				max = Math.max(max, Math.max(temp1, temp2));
			}
		}
		
		//5) ㅗ
		//세로
		for(int i = 0; i<N-2; i++) {
			for(int j=0; j<M-1; j++) {
				int temp1 = map[i][j]+map[i+1][j]+map[i+2][j]+map[i+1][j+1];
				int temp2 = map[i][j+1]+map[i+1][j+1]+map[i+2][j+1]+map[i+1][j];
				max = Math.max(max, Math.max(temp1, temp2));
			}
		}
		//가로
		for(int i = 0; i<N-1; i++) {
			for(int j=0; j<M-2; j++) {
				int temp1 = map[i+1][j]+map[i+1][j+1]+map[i+1][j+2]+map[i][j+1];
				int temp2 = map[i][j]+map[i][j+1]+map[i][j+2]+map[i+1][j+1];
				max = Math.max(max, Math.max(temp1, temp2));
			}
		}
		
		bw.write(max+"");
		bw.flush();
		bw.close();
			
	}
 	
 	public static boolean isValid(int y, int x, int N, int M) {
 		return 0<= y && y<N && 0<= x && x<M;
 	}
 	

	
}
