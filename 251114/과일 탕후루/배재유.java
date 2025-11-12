import java.util.*;
import java.io.*;

public class Main
{
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String args[]) throws Exception
    {
    	
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    	/*
    	 * 
    	 * 과일의 개수가 가장 많은 탕후루의 과일 개수
    	 * 
    	 * N개의 과일이 탕후루 (중복 가능)
    	 * 과일 1~9까지
    	 * 앞에서 a개, 뒤에서 b개 제거
    	 * 
    	 * 과일개수 = len(탕후루)
    	 * 
    	 * 과일 N <= 200000
    	 * 
    	 * Set or int 조절해서 
    	 * Set 매번 생성은 별로다 
    	 * set 재사용
    	 * 
    	 * Deque
    	 * 앞 뒤 제거, 매번 Set에 담아서 len(set) 확인
    	 * 
    	 * 재귀로 deque을 넘긴다 ? 메모리가 충분하긴 하다
    	 * 각 dfs 시행하다 
    	 * 앞 제거 /뒤 제거 분기를 나눈다
    	 * 
    	 * deque에 담기 200000 + 제거 후 set에 담기 200000 
    	 * 시간 복잡도는 괜찮다 
    	 * 스택메모리 200000짜리 200000인데 
    	 * 1) deque 옮겨보고
    	 * 
    	 * 일단 dfs 
    	 *
    	 * 굳이 dfs말고 최소값 구해야한다 = bfs
    	 * 
    	 * 근데 굳이 자료구조에서 직접 뺼 필요가 있나 ?
    	 * idx로 접근하여 투포인터
    	 * 
    	 * dfs+투포인터는 시간초과
    	 * 
    	 * 
    	 * 
    	 * */
    	
    	int N = Integer.parseInt(br.readLine());
    	StringTokenizer st = new StringTokenizer(br.readLine());
    	
    	
    	int[] stick = new int[N];
    	for(int i =0 ; i<N; i++) {
    		stick[i] = Integer.parseInt(st.nextToken());
    	}
    	int[] fruit = new int[10];
    	int a = 0;
    	int b = N;
    	//일반 2중 for문도 시간초과
    	//애초에 모든 for문을 도는게 아니라 가지치기 필요하다
    	//애초에 모든 범위를 다 탐색하는 경우는 드물다
    	//이거 슬라이딩 윈도우 + 투포인터로 해서 범위 가지치기
    	
    	
    	/*
    	 * 1 범위 
    	 * 범위에서 전체 범위가 아니고 줄어든 범위를 알아야 시작점 이동에 대해서 처리
    	 * 2 시작점
    	 * 3 반복
    	 * 
    	 * 슬라이딩 윈도우 + 투포인터지만 매번 모든 범위를 탐색 -> 불필요
    	 * 
    	 * 결국 매번 탐색을 하지만 탐색하는 대상을 변경하여
    	 * int[10]으로 해당 과일 개수에 직접적으로 관여하여
    	 * 100000짜리 반복이 아닌
    	 * 10짜리 반복
    	 * 
    	 * */
    	
    	//처음은 모든 과일 다 담기 -> 200000
    	for(int i =0 ;i<stick.length; i++) {
    		fruit[stick[i]]++;
    	}
    	
    	//대상이 과일로 변경되면 dfs도 가능
    	//결국 이것도 완탐이다 
  	

    	//참고
        //탐색의 방향을 단방향으로 바꾸어 결국 윈도우크기를 고정하는게아니라
        //우측으로 계속 가면서 윈도우 크기 증가하다가 과일 개수가 초과할때만 그 지점까지만 당기는 식으로
        //유연하게 윈도우 크기 조절하여 시간복잡도 감소시키기
    	HashMap<Integer,Integer> fruitCount = new HashMap<>();
    	
    	int Maxlen = 0;
    	int left = 0;
    	for(int right = 0; right<N; right++) {
    		int curFruit = stick[right];
    		fruitCount.put(curFruit,fruitCount.getOrDefault(curFruit, 0)+1);
    		
    		while(fruitCount.size()>2) {
    			int leftFruit = stick[left];
    			fruitCount.put(leftFruit,fruitCount.get(leftFruit)-1);
    			
    			if(fruitCount.get(leftFruit) ==0) {
    				fruitCount.remove(leftFruit);
    			}
    			
    			left++;
    		}
    		
    		Maxlen = Math.max(Maxlen, right-left+1);
    		
    		
    	}
    	
    	bw.write(Maxlen+"");
    	bw.flush();
    	bw.close();
         
    }
    
 
    
    
}
