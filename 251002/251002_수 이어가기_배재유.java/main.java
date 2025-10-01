package algo;

import java.util.*;
import java.io.*;

public class Main {
	
	
    public static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        /*
         * 
         * 1. 목표
         * 규칙을 만족하는 최대 개수의 수들 구하기
         * 
         * 2. 조건
         * 1) 양의 정수
         * 2) 양의 정수중 하나
         * 3) 이후에 나오는 모든 수는 (2번 앞 - 1번 앞)
         * 4) 음수가 만들어지면 음의 정수 버리고 종료
         * 
         * 입력
         * 첫 번째 수
         * 
         * 첫 번째 수 주어지고 -> 이후 두 번째 수까지만 변수, 나머지는 고정된다
         * 
         * 3. 구현
         * 첫 번째수 N <= 30000
         * 
         * 최대 개수 -> 두 번째 수 = N/2 근처 수 => O(logN) -> 크기 않다 = 완전탐색
         * 
         * 4. 자료구조, 변수
         * List<Integer> list 
         * 선언하고 초기화하면서 사용, 재사용
         * 
         * List<Integer> answer
         * 배열도 출력해야해서 최대값 갱신되면 복사할 list 필요
         * 
         * int max_len
         * int temp 입력 값
         * int idx 각 배열에서 2앞 설정, 0부터 시작
         * 
         * */
        
        int first_num = Integer.parseInt(br.readLine());
        List<Integer> list = new ArrayList<>();
        List<Integer> answer = new ArrayList<>();
        
        int max_len = 0;
        
        for(int i = first_num; i>0; i--) {
//        	System.out.println(i);
        	list.clear();
        	list.add(first_num);
        	list.add(i);
        	
        	// list size < 2 -> 그냥 삽입 / 2 >= 뺀 값이 음수가 나올 떄 까지
        	
    		int idx= 0;
    		while(true) {
    			int first = list.get(idx);
    			int second = list.get(idx+1);
    			//음의 정수 = 0 가능하다
    			int new_num = first - second;
    			if( new_num > -1 ) {
    				list.add(new_num);
    				idx++;
    			} else {
    				break;
    				}
    			}

        	
        	if (list.size()> max_len) {
        		answer = new ArrayList<>(list);
        		max_len = list.size();
        	}
        }
        
        bw.write(max_len+"\n");
        for(int i = 0; i<max_len; i++) {
        	if (i != max_len-1) {
        		bw.write(answer.get(i)+" ");
        	} else {
        		bw.write(answer.get(i)+"");
        	}
        	
        }
        
        
    	bw.flush();
    	bw.close();
    }
    

    public static void main(String[] args) throws Exception {
        solution();
    }
}
