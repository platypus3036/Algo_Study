import java.util.*;
import java.io.*;


public class Main {
	
	static int N;
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	static int[][] moves = {
			{-1,0},
			{1,0},
			{0,1},
			{0,-1},
	};
	public static void main(String[] args)  throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		/*
		 * 
		 * 적록색약
		 * 빨강-초록
		 * 
		 * dfs
		 * 2트 
		 * 
		 * 
		 * */
		
		N = Integer.parseInt(br.readLine());
		char[][] map_A = new char[N][N];
//		StringTokenizer st;
		for(int i = 0; i<N; i++) {
			String temp = br.readLine();
			for(int j=0; j<N; j++) {
				map_A[i][j] = temp.charAt(j);
			}
		}
		
		char[][] map_B = new char[N][N];
		for(int i = 0; i<N; i++) {
			for(int j=0; j<N; j++) {
				map_B[i][j] = map_A[i][j];
			}
		}
		
		
		int A = 0;
		int B = 0;
		Deque<int[]> q = new ArrayDeque<>();
		
		
		
		for(int i = 0; i<N; i++) {
			for (int j = 0; j<N; j++) {
				if(map_A[i][j] =='R' ) {
					q.clear();
					A++;
					q.add(new int[] {i,j});
					map_A[i][j] = '-';
					while(!q.isEmpty()) {
						int[] cur = q.poll();
						for(int k=0; k<4; k++) {
							int ny = cur[0]+moves[k][0];
							int nx = cur[1]+moves[k][1];
							if(isValid(ny,nx) && (map_A[ny][nx]=='R')) {
								q.add(new int[] {ny,nx});
								map_A[ny][nx] = '-';
							}
						}
					}
					
				} else if(map_A[i][j] =='B') {
					q.clear();
					A++;
					q.add(new int[] {i,j});
					map_A[i][j] = '-';
					while(!q.isEmpty()) {
						int[] cur = q.poll();
						for(int k=0; k<4; k++) {
							int ny = cur[0]+moves[k][0];
							int nx = cur[1]+moves[k][1];
							if(isValid(ny,nx) && (map_A[ny][nx]=='B')) {
								q.add(new int[] {ny,nx});
								map_A[ny][nx] = '-';
							}
						}
					}
				} else if(map_A[i][j] =='G') {
					q.clear();
					A++;
					q.add(new int[] {i,j});
					map_A[i][j] = '-';
					while(!q.isEmpty()) {
						int[] cur = q.poll();
						for(int k=0; k<4; k++) {
							int ny = cur[0]+moves[k][0];
							int nx = cur[1]+moves[k][1];
							if(isValid(ny,nx) && (map_A[ny][nx]=='G')) {
								q.add(new int[] {ny,nx});
								map_A[ny][nx] = '-';
							}
						}
					}
				}
			}
		}
		
		for(int i = 0; i<N; i++) {
			for (int j = 0; j<N; j++) {
				if(map_B[i][j] =='R'||map_B[i][j] =='G') {
					q.clear();
					B++;
					q.add(new int[] {i,j});
					map_B[i][j] = '-';
					while(!q.isEmpty()) {
						int[] cur = q.poll();
						for(int k=0; k<4; k++) {
							int ny = cur[0]+moves[k][0];
							int nx = cur[1]+moves[k][1];
							if(isValid(ny,nx) && (map_B[ny][nx]=='R' || map_B[ny][nx]=='G')) {
								q.add(new int[] {ny,nx});
								map_B[ny][nx] = '-';
							}
						}
					}
					
				} else if(map_B[i][j] =='B') {
					q.clear();
					B++;
					q.add(new int[] {i,j});
					map_B[i][j] = '-';
					while(!q.isEmpty()) {
						int[] cur = q.poll();
						for(int k=0; k<4; k++) {
							int ny = cur[0]+moves[k][0];
							int nx = cur[1]+moves[k][1];
							if(isValid(ny,nx) && (map_B[ny][nx]=='B')) {
								q.add(new int[] {ny,nx});
								map_B[ny][nx] = '-';
							}
						}
					}
				}
			}
		}
		
		bw.write(String.format("%d %d", A,B));


		
		bw.write("");
		bw.flush();
		bw.close();
		
	}
	
	public static boolean isValid(int y, int x) {
		return 0<= x && x<N && 0<=y && y<N;
	}
}
