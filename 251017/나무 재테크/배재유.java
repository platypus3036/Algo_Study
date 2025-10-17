

import java.util.*;
import java.io.*;

public class Main {

	public static class Point{
		int x;
		int y;
		int age;
		public Point(int x, int y, int age) {
			this.x = x;
			this.y = y;
			this.age = age;
		}
	}
	static int N;
	static int[][] moves = {
			{-1,-1},
			{0,-1},
			{1,-1},
			{-1,0},
			{1,0},
			{-1,1},
			{0,1},
			{1,1},
			
	};
    public static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        /*
         * 
         * 
         * 1. 목표
         * K년이 지난 후 살아남은 나무의 수
         * 
         * 2. 조건
         * NxN 
         * 처음 양분은 5만큼
         * M개의 나무 심었다
         * 한 칸에 여러 개의 나무 심을 수 있다
         * 
         * 봄에는 나이만큼 양분먹고, 나이+1
         * 하나의 칸에 여러 나무가 있다면 나이가 어린 나무부터 양분
         * 만약 양분이 부족해서 나이만큼 못먹으면 바로 즉사
         * 
         * 여름
         * 봄에 죽은 나무가 양분
         * 죽은 나무 나이 /2 양분 (소수점은 버림)
         * 
         * 가을
         * 나무가 번식
         * 번식은 나무 나이가 5의 배수, 인접 8칸에 나이가 1인 나무가 생긴다
         * 
         * 겨울
         * 땅에 양분 추가
         * 각 칸에 추가되는 양분은 A[r][c]
         * 
         * 
         * 3. 구현
         * 시뮬레이션
         * 4배수로 계절 표현
         * 0,1,2,3 1년
         * 4,5,6,7 2년
         * ....
         * 
         * N <=10, NxN <= 100
         * 
         * K <= 1000 -> 4000 * 100 
         * 시간을 고려하지 않고 구현만 하면 될 듯
         * 입력으로 주어지는 나무의 위치 서로 다름 -> 나무 담아서 정렬, 필요 X 어짜피 삽입만 하는거니까
         * 
         * 처음 입력은 A[r][c]
         * 기본 양분 저장 food[][]
         * 
         * 이건 그냥 양분 정보
         * 추가되는 양분의 값이다. 기본 양분 값이 아니다
         * 기본 양분은 5로 고정
         * 
         * 이후 입력받은거 그냥 따로 map에 채워서 
         * 
         * 1. ar 입력받기, map 받기
         * 2. 시뮬레이션 
         * 2-1 계절 별 정리
         * 보유한 나무가 늘어난다, 죽은 나무의 나이 -> 양분
         * 보유한 나무가 늘어난다 -> int 2차원 배열 불가능
         * Map으로 key를 (x,y)로 하고 value list<>해서 담기
         * list는 나이가 가장 어린 나무가 먼저 양분 -> 매번 정렬
         * 죽은 나무 -> 봄 -> 여름이니까 죽자마자 바로 양분으로 처리
         * for-each로 나무 돌리고, 애초에 해당 자리에 나무가 없어지면 map에서 없애기
         * List로 처리하면 나무 나이 , 나무 삭제 처리 불가
         * 
         * 참고 
         * 1) key나 list 내부 값에 대해서 굳이 기존의 list에서 값 갱신 X -> 새 list를 만들어서 변경된 값 넣은 후 기존 k-v 삭제하고 새로운 k-v에 list를 따로 삽입, 
         * 2) hashcode나 equals 오버라이딩하지 않을거면 커스텀 클래스 생성해도 결국 동일하게 새 자료구조에 넣어서 사용
         * 
         * */
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K= Integer.parseInt(st.nextToken());
        //양분 따로 저장
        int[][] food = new int[N+1][N+1];
        for(int i = 1; i<=N; i++) {
        	Arrays.fill(food[i], 5);
        }
        
        
        //입력 받기
        int[][] A = new int[N+1][N+1];
        for(int i = 1; i<=N; i++) {
        	st = new StringTokenizer(br.readLine());
        	for(int j =1; j<=N; j++) {
        		A[i][j] = Integer.parseInt(st.nextToken());
        	}
        }
        
        //모든 큐의 값을 탐색하면서 나무들 정리한 새로운 큐를 재할당시키자
        PriorityQueue<Point> q = new PriorityQueue<>((a,b)-> {
        	return a.age-b.age;
        });
        
        for(int i=1; i<=M; i++) {
        	st = new StringTokenizer(br.readLine());
        	int x = Integer.parseInt(st.nextToken());
        	int y = Integer.parseInt(st.nextToken());
        	int age = Integer.parseInt(st.nextToken());
        	Point point = new Point(x,y,age);
        	q.add(point);
        }
        
        int time = 0;
        while(time <K) {
        	//봄
        	// 나무가 자신의 나이만큼 양분먹고, 나이+1, 나이가 어린 나무부터 -> pq로 처리, 죽은 나무도 따로 List정리해서 처리
        	PriorityQueue<Point> new_q = new PriorityQueue<>((a,b)-> {
        		return a.age-b.age;
        	});
        	
        	List<Point> dead_tree = new ArrayList<>();
        	
        	
        	//양분 가능하면 새 큐에 삽입, 안되면 죽은 나무 리스트에 삽입
        	//참고 2
        	//pq에서 for-each 문을 사용할 시 우선순위가 보장되지 않는다
        	//pq는 heap으로 구현되어 있는데, heap이여서 root가 최소값인것은 보장되지만 나머지 노드들은 정렬 자체가 되어있지 않다
        	//따라서 poll을 사용해야한다
        	while(!q.isEmpty()){
        	    Point point = q.poll();
        	    if(food[point.x][point.y] >= point.age) {
        	        food[point.x][point.y] -= point.age;
        	        point.age++;
        	        new_q.add(point);
        	    } else {
        	        dead_tree.add(point);
        	    }
        	}
        	
        	//새 큐를 할당
        	q = new_q;
        	
        	//여름
        	//양분 처리
        	for(Point point : dead_tree) {
        		food[point.x][point.y] += point.age/2;
        	}
        	
        	//가을
        	//5의 배수만 번식
        	//이것도 새 큐
        	List<Point> breeding = new ArrayList<>();
        	
        	for(Point point : q) {
        		//1. 기존 나무 넣기
        		if(point.age%5 ==0) {
        			//2. 나이가 5의 배수라면 인접 칸 나이 1인 나무 
        			for(int i = 0; i<8; i++) {
        				int nx = point.x+moves[i][0];
        				int ny = point.y+moves[i][1];
        				if(isValid(nx,ny)) {
        					Point new_p = new Point(nx,ny,1);
        					breeding.add(new_p);
        				}
        			}
        		}
        	}
        	
        	//새 큐 다시 할당
        	q.addAll(breeding);
        	
        	
        	//겨울
        	for(int i = 1; i<=N; i++) {
        		for(int j =1; j<=N; j++) {
        			food[i][j] +=A[i][j];
        		}
        	}
        	
        	//1년 지남
        	time++;
        }

        //큐의 길이가 살아있는 나무 개수
        
        bw.write(q.size()+"");
        	

    	bw.flush();
    	bw.close();
    }
    
   
    public static boolean isValid(int x, int y) {
    	return 1<=x && x<=N && 1<= y && y<=N;
    }
    public static void main(String[] args) throws Exception {
        solution();
    }
    


}
