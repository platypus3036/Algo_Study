
import java.util.*;
import java.io.*;

class Main
{
	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		/*
		 * 1. 목표
		 * 사회자가 몇 번째 수를 부른 후 철수가 빙고를 부르는지
		 * 
		 * 2. 조건
		 * 빙고 판 5x5 고정
		 * 
		 * 6번째 ~ 10번째까지 한 줄에 다섯 개씩 빈칸을 두고 주어진다
		 * 
		 * 
		 * 3. 구현
		 * 진짜 생 구현 같다
		 * 빙고 -> 지금 빙고 몇개 ? 조건 만족하면 종료
		 * 
		 * 
		 * */
		
		int[][] bingo = new int[5][5];
		
		StringTokenizer st;
		
		//1. 채우기
		for(int i = 0; i<5; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j<5; j++) {
				bingo[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		//2. 빙고 진행
		int cnt = 0;
		find:
		for(int i = 0; i<5; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j<5; j++) {
				int num = Integer.parseInt(st.nextToken());
				//1) 빙고 처리
				check_num(bingo, num);
				//빙고 처리하고 몇개 째 인지 확인
				cnt++;
				//2) 현재 빙고 확인
				if(check_bingo(bingo) >= 3) {
					bw.write(cnt+"");
					break find;
				}
			}
		}
		
		bw.flush();
		bw.close();
			
	}
	
	public static void check_num(int[][] bingo, int goal) {
		for(int i = 0; i<5; i++) {
			for(int j=0 ; j<5; j++) {
				if(bingo[i][j] == goal) {
					bingo[i][j] = 0;
					return;
				}
			}
		}
	}
	
	public static int check_bingo(int[][] bingo) {
		int bingo_cnt= 0;
		//빙고 확인
		//가로
		for(int i = 0 ; i<5 ; i++) {
			int zero_cnt=  0;
			for(int j=0 ; j<5; j++) {
				if(bingo[i][j] == 0) {
					zero_cnt++;
				}
			}
			if(zero_cnt == 5) {
				bingo_cnt++;
			}
			
		}
		//세로
		for(int i = 0 ; i<5 ; i++) {
			int zero_cnt=  0;
			for(int j=0 ; j<5; j++) {
				if(bingo[j][i] == 0) {
					zero_cnt++;
				}
			}
			if(zero_cnt == 5) {
				bingo_cnt++;
			}
			
		}
		
		//대각선
		int cross_cnt = 0;
		for(int i =0 ;i<5; i++) {
			if(bingo[i][i] == 0) {
				cross_cnt++;
			}
		}
		if(cross_cnt == 5) {
			bingo_cnt++;
		}
		
		int cross_cnt2 = 0;
		for(int i =0 ;i<5; i++) {
			if(bingo[4-i][i] == 0) {
				cross_cnt2++;
			}
		}
		
		if(cross_cnt2 == 5) {
			bingo_cnt++;
		}
		
		
		return bingo_cnt;
	}
	
}