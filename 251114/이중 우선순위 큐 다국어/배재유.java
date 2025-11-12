
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
    	 * 
    	 * q에 저장된 데이터 중 최대값과 최솟값을 출력하는 프로그램
    	 * 
    	 * 그냥 pq쓰면 될듯
    	 * 
    	 * 여기서 이중 우선순위라는게
    	 * 결국 최대최소 -> 2개가 필요하다
    	 * 
    	 * 1. 고려사항
    	 *  
    	 * 우선순위 큐 or 자료구조 정렬을 변경하는 시간 / 우선순위 두 개 사용 시간복잡도
    	 * 1)
    	 * 1000000 시간이 6초 -> 차라리 정렬을 여러번 하는 방법
    	 * -> 시간초과
    	 * 
    	 * 2) 다른방법
    	 * 필요한 연산
    	 * 정렬된 상태 
    	 * -> 삭제 삽입용이 = LinkedList ? 
    	 * 인덱싱 필요x, 추가, 삭제가 필요하다 = treeset 중복제거가 자동으로 되어버린다
    	 * 결국 pq로 돌아간다
    	 * 
    	 * pq 
    	 * 
    	 * 결국 pq두개를 이용하여 각 peek와 비교하여서 삽입 여부 확인
    	 * 두 개써도 엣지케이스 발생
    	 * 
    	 * desc의 최소값이 asc의 최소값보다 작은지 비교를 해야한다 매번 
    	 * 
    	 * 
    	 * 
    	 * */
    	
//    	int T = Integer.parseInt(br.readLine());
//    	List<Integer> list = new ArrayList<>();;
//    	for(int tc = 0; tc<T; tc++) {
//    		int N = Integer.parseInt(br.readLine());
//    		list.clear();
//    		for(int i = 0; i<N; i++) {
//    			String[] input = br.readLine().split(" ");
//    			String ope = input[0];
//    			int num = Integer.parseInt(input[1]);
//    			if(ope.equals("I")) {
//    				list.add(num);
//    			} else {
//    				if(list.size()>0) {
//    					if(num == 1) {
//        					Collections.sort(list);
//        					list.remove(list.size()-1);
//        				} else {
//        					Collections.sort(list,Collections.reverseOrder());
//        					list.remove(list.size()-1);
//        				}
//    				}
//
//    			}
//    		}
//    		if(list.size() ==0) {
//    			bw.write("EMPTY\n");
//    		} else {
//    			//최대 최소
//    			Collections.sort(list);
//    			bw.write(list.get(list.size()-1)+" "+list.get(0)+"\n");
//    		}
//    		
//    	}
    	
    	
    	
    	int T = Integer.parseInt(br.readLine());
    	PriorityQueue<Integer> asc = new PriorityQueue<>();
    	PriorityQueue<Integer> desc = new PriorityQueue<>(Collections.reverseOrder());
    	Map<Integer,Integer> map = new HashMap<>();
    	for(int tc = 0; tc<T; tc++) {
    		int N = Integer.parseInt(br.readLine());
    		map.clear();
    		asc.clear();
    		desc.clear();
    		for(int i = 0; i<N; i++) {
    			String[] input = br.readLine().split(" ");
    			String ope = input[0];
    			int num = Integer.parseInt(input[1]);
    			if(ope.equals("I")) {
    				map.put(num, map.getOrDefault(num, 0)+1);
    				asc.add(num);
    				desc.add(num);
    			} else {
					if(num == 1) {
						if(!desc.isEmpty()) {
							while(true && !desc.isEmpty()) {
								int max = desc.peek();
								if(map.get(max) != 0) {
									max = desc.poll();
									map.put(max, map.get(max)-1);
									break;
								} else {
									int temp = desc.poll();
								}
							}
						}
    				} else {
    					if(!asc.isEmpty()) {
							while(true&& !asc.isEmpty()) {
								int min = asc.peek();
								if(map.get(min) != 0) {
									min = asc.poll();
									map.put(min, map.get(min)-1);
									break;
								} else {
									int temp = asc.poll();
								}
							}
						}
    				}
    			}
    		}
    		
    		while(!desc.isEmpty() && map.get(desc.peek()) == 0) {
    		    desc.poll();
    		}
    		while(!asc.isEmpty() && map.get(asc.peek()) == 0) {
    		    asc.poll();
    		}

    		if(desc.isEmpty() || asc.isEmpty()) { 
    		    bw.write("EMPTY\n");
    		} else {
    		    bw.write(desc.peek() + " " + asc.peek() + "\n");
    		}
    		
    	}
    	
    	/*
      int T = Integer.parseInt(br.readLine());
    	
    	for(int tc = 0; tc<T; tc++) {
    		int N = Integer.parseInt(br.readLine());
    		TreeMap<Integer,Integer> map = new TreeMap<>();
    		for(int i = 0; i<N; i++) {
    			String[] input = br.readLine().split(" ");
    			String ope = input[0];
    			int num = Integer.parseInt(input[1]);
    			if(ope.equals("I")) {
    				map.put(num, map.getOrDefault(num, 0)+1);
    			} else {
    				if(map.size()==0) continue;
    				
    				
					if(num == 1) {
						 int maxKey = map.lastKey();
	                        int count = map.get(maxKey);
	                        if (count == 1) {
	                            map.remove(maxKey); 
	                        } else {
	                            map.put(maxKey, count - 1); 
	                        }
						
    				} else {
    					  int minKey = map.firstKey();
                          int count = map.get(minKey);
                          if (count == 1) {
                              map.remove(minKey); 
                          } else {
                              map.put(minKey, count - 1); 
                          }
    					
    				}
    			}
    		}
    		
    		if(map.size() ==0) { 
    		    bw.write("EMPTY\n");
    		} else {
    		    bw.write(map.lastKey() + " " +map.firstKey() + "\n");
    		}
    		
    	}
    	
      
      
      
      */
    	
    	

    	bw.flush();
    	bw.close();
         
    }
    
 
    
    
}
