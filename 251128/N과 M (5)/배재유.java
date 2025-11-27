import java.util.*;
import java.io.*;


public class Main {
	
	static int N;
	static int M;
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	static int[] answer;
	public static void main(String[] args)  throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		/*
		 * 
		 * 수열은 사전 순으로 증가하는 순서대로
		 * 그냥 백트래킹 안되나
		 * 
		 * */
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		int[] arr = new int[N];
		answer = new int[N];
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i<N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		Arrays.sort(arr);
		int visited = 0;
		dfs(arr, visited, 0);
		bw.flush();
		bw.close();
		
	}
	
	public static void dfs(int[] arr, int visited, int cnt) throws IOException {
		if(cnt == M) {
			for(int i=0; i<M; i++) {
				bw.write(answer[i]+" ");
			}
			bw.write("\n");
			return;
		}
		
		for(int i = 0; i<N; i++) {
			if((visited & 1<<i)==0) {
				answer[cnt] = arr[i]; 
				dfs(arr,visited | (1<<i),cnt+1);

			}
		}
	}
}
