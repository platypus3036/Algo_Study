
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
		 * 별찍기
		 * 
		 * 테두리
		 * 한칸 띄우고
		 * 상자
		 * 한칸 띄우고
		 * 
		 * 4n-3
		 * 
		 * 찾은 것
		 * 전체 크기 4*n-3
		 * 공백과 별은 쌍을 이루며 2개씩 채워진다
		 * 중앙값은 2n-2,2n-2
		 * 
		 * 참고
		 * 1. 애초에 공백을 생각하면 안된다. 공백은 초기값으로 주어지고 별만 찍기
		 * 2. 따라서 2칸씩 시작점을 변경한다. 시작점 기준으로 반복을 돌려야지 거시적으로 보지말자
		 * 
		 * */
		
		int N = Integer.parseInt(br.readLine());
		map = new char[4*N-3][4*N-3];
		for(int i = 0; i<4*N-3; i++) {
			for(int j = 0; j<4*N-3; j++) {
				map[i][j] = ' ';
			}
		}
		map[2*N-2][2*N-2] = '*';
		
		draw(0,0,N);
		
		
		                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
		StringBuilder sb;
		for(int i = 0; i<4*N-3; i++) {
			sb = new StringBuilder();
			for(int j=0; j<4*N-3; j++) {
				sb.append(map[i][j]);
			}
			bw.write(sb.toString()+"\n");
			sb.setLength(0);
		}
	
		bw.flush();
		bw.close();
			
	}
 	
 	public static void draw(int x, int y, int n) {
 		
 		if(n==1) {
 			return;
 		}
 		
 		int len = 4*n-3;
 		for(int j=y; j<y+len; j++) {
 			map[j][x] = '*';
 			map[j][x+len-1] = '*';
 		}
 		
 		for(int j=x; j<x+len; j++) {
 			map[y][j] = '*';
 			map[y+len-1][j] = '*';
 		}
 		draw(x+2, y+2, n-1);
 	}

	
}