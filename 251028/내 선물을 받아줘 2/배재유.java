
import java.util.*;
import java.io.*;

class Main
{
	
	static char[][] map;
 	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		

		/*
		 * 
		 * 구사과가 항상 선물을 가져가는 최소의 칸의 선물
		 * 
		 * 구사과는 1xN의 지도에 존재
		 * 1,x로 나타낸다
		 * 지도의 각 칸 E,W
		 * E 전진 , W 후진
		 * 정지 x
		 * 
		 * 시작위치에 관계없이 선물을 주는 방법
		 * N <= 1000
		 * 범위 넘어가는 경우 자체 존재 x
		 * 
		 * 멈추지 않는다 -> EW 쌍 찾기
		 * 
		 * 
		 * */
		
		int N = Integer.parseInt(br.readLine());
		String map = br.readLine();
		char before = ' ';
		int answer = 0;
		for(int i = 0 ; i<map.length(); i++) {
			if(before == 'E' && map.charAt(i) =='W') {
				answer++;
			}
			before = map.charAt(i);
		}
		bw.write(answer+"");
		


		bw.flush();
		bw.close();
			
	}
 	

	
}