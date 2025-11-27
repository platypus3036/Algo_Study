import java.util.*;
import java.io.*;


public class Main {
	
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	public static void main(String[] args)  throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		/*
		 * 
		 * 모든 집을 칠하는 최소값
		 * 
		 * 집은 빨 초 파 중 하나
		 * 
		 * 1번은 2번과 색이 다르다
		 * --> 각 집은 좌, 우 와 색이 다르다
		 * 각 집에 대해서 빨 초 파로 칠하는 가격이 주어질 때
		 * 
		 * 1. 완탐
		 * N <= 1000
		 * 순서대로 집을 칠할 때 결국 3(1번집) * 2(2번집) *( ) 2 2 2 2
		 * 색칠을 순서대로 한다면 셜국 6 * 2^10 = 1000^ 100 -> 아예 안된다
		 * 
		 * 완탐은 불가능하다
		 * 
		 * 2. 그리디
		 * 이전의 결과가 다음 결과에 영향을 끼치는가 ? O -> 그리디 불가능
		 * 
		 * 3. DP
		 * 결국 dp로 해야지 이전 선택에 대해서 옇향 + 분기가
		 * 
		 * 
		 * */
		
		int N = Integer.parseInt(br.readLine());
		
		int[][] arr = new int[N][3];
		StringTokenizer st;
		for(int i = 0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			arr[i][0] = Integer.parseInt(st.nextToken());
			arr[i][1] = Integer.parseInt(st.nextToken());
			arr[i][2] = Integer.parseInt(st.nextToken());
		}
		
		//1. 일단 완탐느낌으로
		int[][] dp = new int[N][3];
		
//		for(int i = 0; i<N; i++) {
//			for(int j=0; j<3; j++) {
//				if(i==0) {
//					if(dp[i] > arr[i][j]) {
//						dp[i] = arr[i][j];
//						color[i] = j;
//					}
//				} else {
//					if(dp[i] > dp[i-1]+arr[i][j] && color[i-1] != j) {
//						dp[i] = dp[i-1]+arr[i][j];
//						color[i] = j;
//					}
//				}
//			}
//		}
		//그리디하게 해버리면 결국 경우의 수를 다 확인 불가
		/*
		 * 왜 dp인가
		 * 시간이 0.5 -> 완탐이 불가능
		 * 
		 * 탐색을 어떻게 줄일 수 있을까
		 * 특정 지점까지의 최소값
		 * i라면 i-1까지는 최소값이 보장된 값이어야한다
		 * 근데
		 * 
		 * N =10이면
		 * dp[9]까지가 최소합이라고 dp[10] 전체의 최소임을 보장하는가?
		 * -> 이게 그리디 인데
		 * 증명은 불가능할 듯 
		 * 
		 * 메모리제이션 -> 메모리를 통해 시간복잡도를 줄인다
		 * 메모리를 통해 -> 저장하여 들고간다
		 * 
		 * 
		 * 
		 * */
		
		
		dp[0][0] = arr[0][0];
		dp[0][1] = arr[0][1];
		dp[0][2] = arr[0][2];
		for(int i = 1; i<N; i++) {
			dp[i][0] = Math.min(dp[i-1][1],dp[i-1][2]) + arr[i][0];
			dp[i][1] = Math.min(dp[i-1][0],dp[i-1][2]) + arr[i][1];
			dp[i][2] = Math.min(dp[i-1][0],dp[i-1][1]) + arr[i][2];
		}
		
		
		
		
		bw.write(Math.min(dp[N-1][0], Math.min(dp[N-1][1],dp[N-1][2]))+"");
		bw.flush();
		bw.close();
		
	}
}
