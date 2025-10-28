import java.util.*;
import java.io.*;

class Main
{
 	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		

		/*
		 * 
		 * 연속해서 나타나는 그룹단어만 확인
		 * 
		 * 그냥 개수 세기
		 * 
		 * 
		 * */
		boolean[] arr = new boolean[300];
		int N = Integer.parseInt(br.readLine());
		int answer = 0 ;
		for(int i = 0; i<N; i++) {
			arr = new boolean[300];
			String cur = br.readLine();
			char now = 0;
			boolean check = true;
			for(int j=0; j<cur.length(); j++) {
				if(cur.charAt(j) != now) {
					if(arr[cur.charAt(j)]) {
						check = false;
						break;
					}
					arr[now] = true;
					now = cur.charAt(j);
				}
			}
			if(check) {
				answer++;
			}
		}
		                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
		bw.write(answer+"");
	
		bw.flush();
		bw.close();
			
	}
 	
 	

	
}