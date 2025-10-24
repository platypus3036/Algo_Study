
import java.util.*;
import java.io.*;

class Main
{
	
	
	static int[][] moves = {
			{-1,0},
			{1,0},
			{0,1},
			{0,-1}
	};
 	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		/*
		 * 
		 * 1. 목표
		 * 도연이가 만날 수 있는 사람의 수
		 * 
		 * 2. 조건
		 * 캠퍼스의 크기 NxM
		 * 캠퍼스에서 이동 -> 상하좌우
		 * 그냥 델타문제
		 * 
		 * 메모리제한도 크다 -> 600x600x 8byte
		 * 360000 2880000 byte -> 약 3000 MB -> String은 불가
		 * char로 하자
		 * 
		 * 
		 * */
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		char[][] map = new char[N][M];
		for(int i = 0; i<N; i++) {
			String line = br.readLine();
			for(int j =0; j<M; j++) {
				map[i][j] = line.charAt(j);
			}
		}
		
		int sy = -1;
		int sx = -1;
		//1. 도연이 찾기
		for(int i=  0; i<N; i++) {
			for(int j=0; j<M; j++) {
				if(map[i][j] == 'I') {
					sy = i;
					sx = j;
					break;
				}
			}
		}
		
		int cnt= 0;
		
		boolean[][] visited= new boolean[N][M];
		
		Deque<int[]> q=  new ArrayDeque<>();
		q.add(new int[] {sy,sx});
		visited[sy][sx] = true;
		while(!q.isEmpty()) {
			int[] cur = q.poll();
			if(map[cur[0]][cur[1]] == 'P') {
				cnt++;
			}
			
			for(int i =0; i<4; i++) {
				int ny = cur[0]+moves[i][0];
				int nx = cur[1]+moves[i][1];
				if(isValid(ny,nx,N,M) && !visited[ny][nx] && map[ny][nx] != 'X') {
					q.add(new int[] {ny,nx});
					visited[ny][nx] = true;
				}
			}
		}
		
		
		if(cnt==0) {
			bw.write("TT");
		} else {
			bw.write(cnt+"");
		}
		
		
		bw.flush();
		bw.close();
			
	}
 	
 	public static boolean isValid(int sy,int sx, int N, int M) {
 		return 0<=sy && sy < N && 0<= sx && sx <M;
 	}
	
}
