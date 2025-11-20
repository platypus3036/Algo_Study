import java.io.*;
import java.util.*;





public class Main {
	

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		/*
		 * 
		 * N번째 큰 수를 찾는 프로그램
		 * 
		 * 모든 수는 자신의 한 칸 위에 있는 수보다 크다
		 * 
		 * N번째 큰수
		 * 
		 * 1500 * 1500
		 * 
		 * 2250000
		 * 
		 * 완탐은 가능
		 * 
		 * 위의수 = map[y][x] > map[y-1][x]이 보장된다
		 * 
		 * 메모리 약 400mb 적당하다
		 * 
		 * 완탐도 가능하지만 방법이 없나?
		 * 
		 * 
		 * 
		 * 
		 * */
		
		int N  = Integer.parseInt(br.readLine());
		int map[][] = new int[N][N];
		StringTokenizer st;
		List<Integer> list = new ArrayList<>();
		for(int i = 0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<N; j++) {
				int num = Integer.parseInt(st.nextToken());
				map[i][j] = num;
				list.add(num);
			}
		}
		
		Collections.sort(list, Collections.reverseOrder());
		bw.write(list.get(N-1)+"");
		
		bw.flush();
		bw.close();
		
		
		
		}
		
}
