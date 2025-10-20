package samsung01;

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
		 * 크기가 1x1인 정사각형의 네 꼭지점이 모두 드래곤 커브의 일부인 정사각형의 개수
		 * 
		 * 2. 조건
		 * x는 -> ,y는 아래 고정
		 * 
		 * 속성 3가지
		 * 시작 점, 시작 방향, 세대
		 * 
		 * 0세대는 길이가 1인 선분
		 * 
		 * 1세대
		 * 끝점을 기준으로 90도 회전 , 끝점과 이어붙이기
		 * 
		 * 2세대
		 * 동일하기 끝점 기준 90도 회전
		 * 
		 * 3세대도 동일
		 * 
		 * N 드래곤 커브 개수
		 * x,y 드래곤 커브 시작점, d 시작방향, g 세대
		 * 
		 * 드래곤 커브는 서로 겹칠 수 있다
		 * 
		 * 네 꼭짓점이 모두 드래곤 커브의 일부인 것의 개수
		 * 
		 * 3. 구현
		 * 드래곤 커브를 만들어서
		 * 좌표에 표시, 1x1 단위로 체크해서 총 몇개 인지 확인
		 * 
		 * 핵심은 좌표의 모음을 회전시켜서 좌표 집합에 +하는 것
		 * 새로운 자료구조에 할당시키며 더하기
		 * 
		 * 
		 * */
		boolean[][] map = new boolean[101][101];
		int N = Integer.parseInt(br.readLine());
		for(int i = 0; i<N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			int d = Integer.parseInt(st.nextToken());
			int g = Integer.parseInt(st.nextToken());
			int gene = 0;
			List<int[]> list = new ArrayList<>();
			list.add(new int[] {x,y});
			//회전의 기준이 되는 끝점은 항상 list의 맨 끝에 자리한다 
			//굳이 list 고집 이유가 없다 deque으로
			if(d == 0) {
				list.add(new int[] {x+1,y});
			} else if (d==1) {
				list.add(new int[] {x,y-1});
			} else if (d==2) {
				list.add(new int[] {x-1,y});
			} else {
				list.add(new int[] {x,y+1});
			}
			

			
			while(gene < g) {
				//90도 회전시키는거
				//1) 기준점
				int[] base = list.get(list.size()-1);
				int base_x = base[0];
				int base_y = base[1];
				//2) 기준점 기준으로 모든 좌표 90도 회전
				/*
				 * 기준점 base x,base y로부터 a,b의 좌표 회전
				 * 1. 기준점을 0,0으로 맞춘다
				 * a-base_x, b-base_y
				 * 2. 좌표 회전 , 시계방향은 q,p -> p,-q
				 * b-base_y, base_x-a
				 * 3. 기준점 0,0에서 x,y로
				 * base_x-base_y+b, base_x+base+y-a
				 * 
				 * 
				 * */
				//기존 내용을 보존하고, idx로 접근하려면 list가 맞네
				//list 가변길이
				int len = list.size();
				//이거 리스트 역순으로 돌려야 정렬
				for(int j = len-2; j>-1; j--) {
					int[] cur = list.get(j);
					int cx = cur[0];
					int cy = cur[1];
				    int nx = base_x - (cy - base_y);
				    int ny = base_y + (cx - base_x);
					list.add(new int[] {nx,ny});
				}
				gene++;
			}
			//지도 채우기
			for(int j=0; j<list.size(); j++) {
				int[] cur = list.get(j);
				map[cur[0]][cur[1]] = true;
			}
		}
		int answer = 0;
		//사각형 검사
		
		int cnt = 0;
		for(int i=0; i<101; i++) {
			for(int j=0; j<101; j++) {
				if(map[i][j]) {
					cnt++;
				}
			}
		}
		
		
		for(int i=0; i<100; i++) {
			for(int j=0; j<100; j++) {
				if(map[i][j] && map[i+1][j] && map[i][j+1] && map[i+1][j+1]) {
					answer++;
				}
			}
		}
		
		bw.write(answer+"");
		bw.flush();
		bw.close();
			
	}
	

	
	
}