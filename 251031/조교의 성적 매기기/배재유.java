
import java.util.*;
import java.io.*;

class Solution
{
	
	static int H;
	static int W;
 	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		

		/*
		 * 
		 * K번째 학생의 학점을 출력
		 * 
		 * 평점 10개
		 * 
		 * 총점 = 중간 + 기말 + 과제
		 * 
		 * 총점 기준으로
		 * 
		 * 평점 자르는 기준은 N/10으로
		 * 
		 * 
		 * 
		 * */
		
		int T = Integer.parseInt(br.readLine());
		for(int tc=1; tc<=T; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int K = Integer.parseInt(st.nextToken());
			//0-index
			int[] scores = new int[N+1];
			for(int i=1; i<=N; i++) {
				st = new StringTokenizer(br.readLine());
				int mid = Integer.parseInt(st.nextToken());
				int fin = Integer.parseInt(st.nextToken());
				int homework = Integer.parseInt(st.nextToken());
				scores[i] = 35*mid + fin* 35 + homework*20;
			}
			
			int line = N/10;
			//idx, 번호로 나눠야한다
			List<int[]> list = new ArrayList<>();
			for(int i =1; i<=N; i++) {
				list.add(new int[] {i,scores[i]});
			}
			
			Collections.sort(list,(a,b)-> {
				return b[1]-a[1];
			});
			String[] grade = new String[10];
			grade[0] = "A+";
			grade[1] = "A0";
			grade[2] = "A-";
			grade[3] = "B+";
			grade[4] = "B0";
			grade[5] = "B-";
			grade[6] = "C+";
			grade[7] = "C0";
			grade[8] = "C-";
			grade[9] = "D0";
			
			int grade_idx= 0;
			for(int i = 0; i<N; i+=line) {
				for(int j=i; j<i+line; j++) {
					if(list.get(j)[0] == K) {
						bw.write(String.format("#%d %s\n", tc,grade[grade_idx]));
						break;
					}
				}
				grade_idx++;
			}
		}
		
		


		bw.flush();
		bw.close();
			
	}

}