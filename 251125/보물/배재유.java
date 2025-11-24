import java.util.*;
import java.io.*;


public class Main {

	public static void main(String[] args)  throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		/*
		 * 
		 * S의 최솟값 = 
		 * 큰수를 순서대로 작은수와 곱하게 한다
		 * b는 정렬 금지
		 * 
		 * */
		
		int N = Integer.parseInt(br.readLine());
		int[] A = new int[N];
		int[] B = new int[N];
		StringTokenizer st = new StringTokenizer(br.readLine());

		for(int i = 0; i<N; i++) {
			A[i] = Integer.parseInt(st.nextToken());
		}
		
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i<N; i++) {
			B[i] = Integer.parseInt(st.nextToken());
		}
		
		Arrays.sort(B);
		Arrays.sort(A);
		
		int answer = 0;
		for(int i = 0; i<N; i++) {
			answer+= B[i]*A[N-1-i];
		}
		
		bw.write(answer+"");
		bw.flush();
		bw.close();
		
	}
}
