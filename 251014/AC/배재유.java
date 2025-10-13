
import java.util.*;
import java.io.*;

public class Main {


    public static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        /*
         * 
         * 1. 목표
         * 최종 결과를 구하는 프로그램
         * 
         * 2. 조건
         * R 뒤집기
         * D 버리기
         * 
         * R 배열의 순서를 뒤집는 함수
         * D 첫 번째 수를 버리는 함수
         * 배열이 비어있는데, D를 사용하면 에러
         * 함수는 조합하여 한번에 사용 가능
         * RDD 같은
         * 
         * 입력
         * T<= 100
         * 1<= p 함수 <= 100000
         * 배열에 있는 수의 개수 n <= 100000
         * 배열에 들어잇는 정수 xi <= 100
         * p의 길이의 합 + n의 합 < 700000
         * 입력순서
         * 함수
         * 배열 길이
         * 실제 배열
         * 
         * 3. 구현
         * []와 같은 파싱이 문제, 문제 자체는 그냥 실제 구현하면 될 듯
         * 첫 번째 수를 버린다 -> 큐에 담아서 처리하는게
         * 
         * 큐 사용 -> 시간초과
         * for문으로 뒤집어서 시간초과 예상
         * list 뒤집기 O(logN), 첫 번째 숫자 제거 O(N)
         * q 뒤집기 O(N) 첫 번째 숫자 제거 O(1)
         * 
         * 뭔 방법을 써도 시간초과가 뜬다
         * 애초에 직접 뒤집어야 할까 ?
         * 덱으로 앞 뒤로 자르는데 시간복잡도 
         *  
         * */
        
        int T = Integer.parseInt(br.readLine());
        for(int i = 0; i<T; i++) {
        	String operation = br.readLine();
        	int arr_len = Integer.parseInt(br.readLine());

        	//가지치기 1. 길이 0일때
        	//이게 잘못된 가지치기 
            //에러 조건은 D일때 빈배열이면 애초에 len이랑 무관
        	
        	String input_arr = br.readLine();
        	Deque<Integer> q = new ArrayDeque<>();
        	//char로 나누면 이게 자리수가 한자리만 가능하다
        	StringBuilder sb = new StringBuilder();
        	int idx = 1;
        	if (arr_len > 0) {
                StringTokenizer st = new StringTokenizer(input_arr.substring(1, input_arr.length() - 1), ",");
                while (st.hasMoreTokens()) {
                    q.add(Integer.parseInt(st.nextToken()));
                }
            }
        	boolean isReverse = false;
        	boolean isError = false;
        	for (char op : operation.toCharArray()) {
                if (op == 'R') {
                    isReverse = !isReverse;
                } else { // 'D' 연산
                    // 문제 1 해결: 'D'를 할 때 비어있을 경우에만 에러
                    if (q.isEmpty()) { 
                        isError = true;
                        break;
                    }
                    if (isReverse) {
                        q.pollLast();
                    } else {
                        q.pollFirst();
                    }
                }
            }
        	int q_size = q.size();
            
        	if(isError) {
        		bw.write("error\n");
        	} else {
        		 bw.write("[");
                 sb = new StringBuilder();
                 while(!q.isEmpty()) {
                     if(isReverse) {
                         sb.append(q.pollLast());
                     } else {
                         sb.append(q.pollFirst());
                     }
                     if(!q.isEmpty()) {
                         sb.append(",");
                     }
                 }
                 bw.write(sb.toString());
                 bw.write("]\n");
        	}
        	
        	
        }
        
        
        	

    	bw.flush();
    	bw.close();
    }
    
   
    public static void main(String[] args) throws Exception {
        solution();
    }
    


}
