

import java.util.*;
import java.io.*;

public class Main
{
    public static void main(String args[]) throws Exception
    {
    	
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    	
    	/*
    	 * 
    	 * x1 -> xn까지 좌표 압축시킨거 
    	 * 
    	 * xi = xi > xj을 만족하는 서로다른 좌표 xj의 개수와 동일
    	 * 
    	 * N <= 1000000
    	 * 
    	 * 최적화가 필요해보인다
    	 * 
    	 * 직접적인 수로 판단하기에는 메모리 초과
    	 * 애초에 저장할 필요 x 
    	 * 현재 input의 숫자가 list에서 몇 번째 인덱스인지만 알면 된다
    	 * 
    	 * */
    	
    	//set -> list로 중복제거된 상태에서 해당 len-idx가 값이다
    	
    	int N = Integer.parseInt(br.readLine());
    	
    	StringTokenizer st = new StringTokenizer(br.readLine());
    	int[] input = new int[N];
    	for(int i = 0; i<N; i++) {
    		input[i] = Integer.parseInt(st.nextToken());
    	}
    	Set<Integer> set = new HashSet<>();
    	
    	for(int i = 0; i<N; i++) {
    		set.add(input[i]);
    	}
    	
    	List<Integer> list = new ArrayList<>();
    	
    	for(int num : set) {
    		list.add(num);
    	}
    	
    	Collections.sort(list);
    	int[] output = new int[N];
    	//Map에 1000000 괜찮은가 ? 
    	Map<Integer,Integer> map = new HashMap<>();
    	for(int i = 0; i<list.size(); i++) {
    		map.put(list.get(i), i);
    	}
    	
    	
    	
    	
    	StringBuilder sb = new StringBuilder();
    	for(int i = 0; i<N; i++) {
    		if(i!=N-1) {
    			sb.append(map.get(input[i])+" ");
    		} else {
    			sb.append(map.get(input[i])+"");
    		}
    	}
    	
    	
    	



		
		
		bw.write(sb.toString());
		
		

    	
    	bw.flush();
    	bw.close();
         
    }
}
