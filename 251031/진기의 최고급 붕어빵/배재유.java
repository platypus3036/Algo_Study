
import java.util.*;
import java.io.*;

class Solution
{
	
	static char[][] map;
 	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		

		/*
		 * 
		 * 붕어빵 제공 가능한지 판별
		 * 
		 * 0초부터 붕어빵을 만들어 M초 K개의 붕어빵
		 * 
		 * 0초이후 언제 도착하는지 주어지면 모든 손님들에게 붕어빵을 제공할 수 있는지
		 * 
		 * N,M,K
		 * 
		 * N개의 정수 각 손님이 언제 도착하는지
		 * 
		 * 1. 붕어빵 킾이 가능한가 ?
		 * 가능하다면 각 초마다 누적시켜서
		 * 
		 * 약간의 시뮬레이션
		 * 
		 * N <= 100
		 * 11111 * 100
		 * 1111100 시간은 충분
		 * 매번 모든 배열 초기화시켜서 현재 붕어빵 갯수에 대해서 최신화  
		 * 
		 * 
		 * */
		
		int T = Integer.parseInt(br.readLine());
		
		for(int tc = 1; tc<=T; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int N  = Integer.parseInt(st.nextToken());
			int M  = Integer.parseInt(st.nextToken());
			int K  = Integer.parseInt(st.nextToken());
			//0-idx
			int[] arr = new int[11112];
			List<Integer> list = new ArrayList<>();
			st = new StringTokenizer(br.readLine());
			for(int i =0; i<N; i++) {
				list.add(Integer.parseInt(st.nextToken()));
			}
			
			Collections.sort(list);
			for(int i = M; i<arr.length; i+=M) {
				for(int j=i; j<arr.length; j++) {
					arr[j] +=K;
				}
			}
			boolean canEat = true;
			for(int cu : list) {
				if(arr[cu] <=0) {
					canEat = false;
					break;
				}
				for(int i = cu; i<arr.length; i++) {
					arr[i]--;
				}
			}
			
			if(canEat) {
				bw.write(String.format("#%d Possible\n", tc));
			} else {
				bw.write(String.format("#%d Impossible\n", tc));
			}
			
		}

		

		
		
		


		bw.flush();
		bw.close();
			
	}
}