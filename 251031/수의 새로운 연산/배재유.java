
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
		 * 명령어 이후 맵의 상태
		 * 
		 * 시뮬레이션
		 * 
		 * 전차는 어짜피 1대
		 * 매번 전차 위치 확인하여 문제 처리
		 * 
		 * 
		 * */
		
		int T = Integer.parseInt(br.readLine());
		for(int tc =1; tc<=T; tc++) {
			StringTokenizer st = new StringTokenizer (br.readLine());
			H = Integer.parseInt(st.nextToken());
			W = Integer.parseInt(st.nextToken());
			char[][] map = new char[H][W];
			for(int i = 0; i<H; i++) {
				map[i] = br.readLine().toCharArray();
			}
			int command_len = Integer.parseInt(br.readLine());
			//시뮬레이션 시작 전 위치 찾기
			int sy = -1;
			int sx = -1;
			int dir = -1;
			//방향은 상 부터 시계방향으로 0123
			for(int i = 0; i<H; i++) {
				for(int j=0; j<W; j++) {
					if(map[i][j] == '^') {
						sy = i;
						sx = j;
						dir = 0;
						break;
					} else if(map[i][j] == '>')  {
						sy = i;
						sx = j;
						dir = 1;
						break;
					} else if(map[i][j] == 'v') {
						sy = i;
						sx = j;
						dir = 2;
						break;
					} else if(map[i][j] == '<') {
						sy = i;
						sx = j;
						dir = 3;
						break;
					}
				}
				
			}
			
			String command = br.readLine();
			for(int i = 0; i<command_len; i++) {
				if(command.charAt(i) == 'S') {
					if(dir == 0) {
						//sy에서 0까지 탐색
						for(int j = sy-1; j>-1; j--) {
							if(map[j][sx] == '#') {
								break;
							} else if(map[j][sx] == '*') {
								map[j][sx] = '.';
								break;
							} 
						}
					} else if (dir ==1) {
						//우측 sx에서 W까지
						for(int j = sx+1; j<W; j++) {
							if(map[sy][j] == '#') {
								break;
							} else if(map[sy][j] == '*') {
								map[sy][j] = '.';
								break;
							} 
						}
					} else if (dir==2) {
						//하단 sy에서 H까지
						for(int j = sy+1; j<H; j++) {
							if(map[j][sx] == '#') {
								break;
							} else if(map[j][sx] == '*') {
								map[j][sx] = '.';
								break;
							} 
						}
					} else {
						//좌측 sx부터 0까지
						for(int j = sx-1; j>-1; j--) {
							if(map[sy][j] == '#') {
								break;
							} else if(map[sy][j] == '*') {
								map[sy][j] = '.';
								break;
							} 
						}
					}
				} else if (command.charAt(i) == 'U') {
					//방향 위로, 평지면 이동, 이동 전 범위 확인
					//방향은 이동 불가와 상관없이 변경
					//방향 변경에 대해서도 탱크 표시도 기본적으로 변경해야한다
					dir = 0;
					map[sy][sx] = '^';
					int ny = sy-1;
					int nx = sx;
					if(isValid(ny,nx) && map[ny][nx] == '.') {
						char temp = map[sy][sx];
						map[sy][sx] = '.';
						map[ny][nx] = temp;
						//이동 후 좌표 변경
						sy = ny;
						sx = nx;
					}
				} else if (command.charAt(i) == 'R') {
					//방향 우측, 평지면 이동, 이동 전 범위 확인
					//방향은 이동 불가와 상관없이 변경
					dir = 1;
					map[sy][sx] ='>';
					int ny = sy;
					int nx = sx+1;
					if(isValid(ny,nx) && map[ny][nx] == '.') {
						char temp = map[sy][sx];
						map[sy][sx] = '.';
						map[ny][nx] = temp;
						//이동 후 좌표 변경
						sy = ny;
						sx = nx;
					}
				} else if (command.charAt(i) == 'D') {
					//방향 아래, 평지면 이동, 이동 전 범위 확인
					//방향은 이동 불가와 상관없이 변경
					dir = 2;
					map[sy][sx] ='v';
					int ny = sy+1;
					int nx = sx;
					if(isValid(ny,nx) && map[ny][nx] == '.') {
						char temp = map[sy][sx];
						map[sy][sx] = '.';
						map[ny][nx] = temp;
						//이동 후 좌표 변경
						sy = ny;
						sx = nx;
					}
				} else if (command.charAt(i) == 'L') {
					//방향 좌측, 평지면 이동, 이동 전 범위 확인
					//방향은 이동 불가와 상관없이 변경
					dir = 3;
					map[sy][sx] ='<';
					int ny = sy;
					int nx = sx-1;
					if(isValid(ny,nx) && map[ny][nx] == '.') {
						char temp = map[sy][sx];
						map[sy][sx] = '.';
						map[ny][nx] = temp;
						//이동 후 좌표 변경
						sy = ny;
						sx = nx;
					}
				} 
			}
			//출력
			//첫 번째 줄은 tc와 함께 출력
			String temp = String.format("#%d ", tc);
			for(int i = 0 ; i<W; i++) {
				temp+=String.valueOf(map[0][i]);
			}
			bw.write(temp+"\n");
			for(int i = 1; i<H; i++) {
				StringBuilder sb = new StringBuilder();
				for(int j =0; j<W; j++) {
					sb.append(map[i][j]);
				}
				bw.write(sb.toString()+"\n");
			}
			
			
		}
		

		

		
		
		


		bw.flush();
		bw.close();
			
	}
 	
 	public static boolean isValid(int y, int x) {
 		return 0<=x && x<W && 0<=y && y<H;
 	}
}