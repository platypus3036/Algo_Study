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
		 * 직사각형을 그리는데 필요한 PU 명령어 최소값
		 * 
		 * 
		 * fd x x만큼 전진
		 * lt a 반시계 방향으로 a 만큼 회전
		 * rt a 시계방향으로 a만큼 회전
		 * pu 연필을 올린다
		 * pd 연필을 내린다
		 * 
		 * 
		 * 한선 긋기 중복 가능
		 * 
		 * 1. 직접 그리기
		 * 실제 좌표평면에서 시뮬레이션
		 * 
		 * 2. 한점이라도 겹치지 않은 사각형, 겹치는 사각형들은 같은 집합으로 취급하기 각 좌표들의 범위는 같아야한다 
		 * 
		 * 2차원 boolean
		 * 사각형 -> 일정 범위 
		 * 
		 * 1그룹 2그룹 에 동시에 교차하는 사각형 존재 시 1,2그룹 동시에 편입시켜야한다
		 * 
		 * 겹친다 = 하나도 안만난다의 역
		 * 
		 * */
		
		int N = Integer.parseInt(br.readLine());
		int[][] squares = new int[N+1][4];
		StringTokenizer st;
		for(int i = 0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			
			//x1y1 x2y2
			squares[i][0] = Integer.parseInt(st.nextToken());
			squares[i][1] = Integer.parseInt(st.nextToken());
			squares[i][2] = Integer.parseInt(st.nextToken());
			squares[i][3] = Integer.parseInt(st.nextToken());
		}
		
		//좌표평면 음수 처리 
		int[][] visited = new int[1001][1001];
		int[] rank = new int[N+1];
		int[] parent = new int[N+1];
		for(int i = 1; i<=N; i++) {
			parent[i] = i;
		}

		
		// 1. 사각형에 id 부여 
		for(int i = 1; i<=N; i++) {
			//좌표 탐색은 이전과 동일하게 변 탐색
			int sx = squares[i-1][0]+500;
			int sy = squares[i-1][1]+500;
			int ex = squares[i-1][2]+500;
			int ey = squares[i-1][3]+500;

			//Set으로 그룹핑
			Set<Integer> connected = new HashSet<>();
			for(int j= sy; j<= ey; j++) {
				if(visited[sx][j] !=0) {
					connected.add(find_parent(visited[sx][j],parent));
				} else {
					visited[sx][j] = i;
				}
			}
			
			
			
			for(int j= sy; j<= ey; j++) {
				if(visited[ex][j] !=0) {
					connected.add(find_parent(visited[ex][j],parent));
				} else {
					visited[ex][j] = i;
				}
			}
			
			
			for(int j= sx; j<= ex; j++) {
				if(visited[j][sy] !=0) {
					connected.add(find_parent(visited[j][sy],parent));
				} else {
					visited[j][sy] = i;
				}
			}

			
			
			for(int j= sx; j<= ex; j++) {

				if(visited[j][ey] !=0) {
					connected.add(find_parent(visited[j][ey],parent));
				} else {
					visited[j][ey] = i;
				}
			}

			
			//set에 있는것과 현재 그룹 다 union
			for(int group : connected) {
				union(i,group, parent,rank);
			}
		}
		
		//일단 00 확인하고
		int answer = 0;

		//-처리 때문에 00 -> 500, 500
		if(visited[500][500] == 0) {
			answer++;
		} 

		
		Set<Integer> group = new HashSet<>();
		for(int i = 1; i<=N; i++) {
			group.add(find_parent(i,parent));
		}
		
		int total = group.size();
		int zerogroup = -1;
		if (visited[500][500] !=0) {
			zerogroup = find_parent(visited[500][500], parent);
		}
		
		if(zerogroup != -1) {
			total--;
		}
		
		bw.write(total+"");
		bw.flush();
		bw.close();
		
		
		
	}
	
	public static int find_parent(int x, int[] parent) {
		if(parent[x] != x) {
			parent[x] = find_parent(parent[x],parent);
		}
		return parent[x];
	}
	
	
	public static void union(int x, int y, int[] parent, int[] rank) {
		int root_x = find_parent(x, parent);
		int root_y = find_parent(y,parent);
		
		if(root_x != root_y) {
			if(rank[root_x] > rank[root_y]) {
				parent[root_y] = root_x;
			} else if (rank[root_x] < rank[root_y]) {
				parent[root_x] = root_y;
			} else {
				parent[root_x] = root_y;
				rank[root_y]++;
			}
		}
	}
	
}
