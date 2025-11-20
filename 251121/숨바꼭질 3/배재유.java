import java.io.*;
import java.util.*;





public class Main {
	
 	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		/*
		 * 
		 *   
		 *   수빈이가 동생을 찾는 가장 빠른 시간
		 *   
		 *   겉는다 = x-1, x+1 , time+1
		 *   순간이동 = 2*x, time
		 *   
		 *   가장 빠른 시간 = bfs 모든 분기 탐색
		 *   방문처리로 가지치기
		 * 
		 * */
		
		boolean[] visited = new boolean[100001];
		Deque<int[]> q = new ArrayDeque<>();
		
		int time = 0;
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		q.add(new int[] {N,0});
		//1. 방문처리 int크기를 한참 벗어난다
//		visited |= 1<<N;
		visited[N] = true;
		
		int answer = 0;
		
		while(!q.isEmpty()) {
			
			
			int[] cur = q.poll();
			int cidx = cur[0];
			int ctime = cur[1];
			// 경우는 걷기, 순간이동

			if(cidx == K) {
				answer = ctime;
				break;
			}
			
			if(cidx*2<=100000&& cidx*2>= 0 &&!visited[cidx*2]) {
				q.add(new int[] {cidx*2,ctime});
				visited[cidx*2] = true;
			}
			
			
			if(cidx-1<=100000&& cidx-1>= 0 &&!visited[cidx-1]) {
				q.add(new int[] {cidx-1,ctime+1});
				visited[cidx-1] = true;
			}
			
			if(cidx+1<=100000 && cidx+1>= 0 &&!visited[cidx+1]) {
				q.add(new int[] {cidx+1,ctime+1});
				visited[cidx+1] = true;
			}
			
			
			
		}

		bw.write(answer+"");
		bw.flush();
		bw.close();
		
		
		
		}
		
}
