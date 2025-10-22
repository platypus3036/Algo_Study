
import java.util.*;
import java.io.*;

class Main
{
	static int[] color;
	static int[][] map;
	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		/*
		 * 
		 * 1. 목표
		 * 잘라진 하얀색 색종이 와 파란색 색종이의 개수
		 * 
		 * 2. 조건
		 * 각 색종이를 N/2로 햇을 때 구성 칸이 동일 색이 될 때까지
		 * 
		 * DFS로 각 나눈 값이 같은 컬러로 되었는지 확인하며 개수 확인
		 * N == 1 이면 그냥 그 컬러
		 * 
		 * 3. 구현
		 * DFS
		 * 컬러는 실제 color[2] 해서 0 0개수  1 1개수
		 * 
		 * */
		
		color = new int[2];
		
		int N = Integer.parseInt(br.readLine());
		map = new int[N][N];
		
		for(int i = 0; i<N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for(int j = 0; j<N; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		dfs(0,0,N);
		
		
		bw.write(color[0]+"\n");
		bw.write(color[1]+"");
		
		bw.flush();
		bw.close();
			
	}
	
	public static void dfs(int sy, int sx, int N) {
		
		int base_color = map[sy][sx];
		//종료 조건
		if(N == 1) {
			color[base_color]++;
			return;
		}
		
		
		
		if(isSame(N,sy,sx)) {
			color[base_color]++;
			return;
		}
		
		//0-idx
		//4/2 = 2 01, 23 N/2-1 
		dfs(sy, sx,N/2);
		dfs(sy, sx+N/2,N/2);
		dfs(sy+N/2,sx,N/2);
		dfs(sy+N/2,sx+N/2,N/2);
		
		
		
	}
	
	public static boolean isSame(int N, int sy, int sx) {
		for(int i = sy; i<sy+N; i++) {
			for(int j= sx; j<sx+N; j++) {
				if(map[i][j] != map[sy][sx]) {
					return false;
				}
			}
		}
		return true;
	}
	
}