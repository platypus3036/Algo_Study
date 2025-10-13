

import java.util.*;
import java.io.*;

public class Main {

	static int N;
    public static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        /*
         * 
         * 1. 목표
         * 스위치들의 마지막 상태 
         * 
         * 2. 조건
         * 스위치는 8개
         * 1 on 0 off
         * 학생들을 뽑아 자연수 N을 하나씩 나누어 주었다
         * 
         * 1) 남자
         * 스위치 번호가 자기가 받은 수의 배수면 상태 바꾼다 
         * 2) 여자
         * 번호 스위치 중심으로 좌우가 대칭인 부분 모두를 바꾼다
         * 해당 번호는 무조건 변경
         * 
         * 남자 1 여자 2
         * 출력
         * 
         * 스위치는 1부터 시작 o-index
         * 출력을 20개씩 한다
         * 스위치 N <= 100
         * 
         * 3. 구현
         * 함수로 입력에 따라 스위치 변경
         * 출력 주의하기
         * 
         *  
         * */
        
        N = Integer.parseInt(br.readLine());
        int[] switchs = new int[N+1];
        //0-index
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 1; i<= N; i++) {
        	switchs[i] = Integer.parseInt(st.nextToken());
        }
        
        int T = Integer.parseInt(br.readLine());
        for(int i = 0; i<T; i++) {
        	st = new StringTokenizer(br.readLine());
        	int gender = Integer.parseInt(st.nextToken());
        	int idx =  Integer.parseInt(st.nextToken());
        	change_switch(switchs,gender,idx);
        }
        

        
        for(int i = 1; i<=N; i+=20) {
        	for(int j=i; j<=i+19; j++) {
        		if (j <=N) {
        			if(j!=i+19) {
            			bw.write(switchs[j]+" ");
            		} else {
            			bw.write(switchs[j]+"");
            		}
        		}
        		
        	}
        	bw.write("\n");
        }

    	bw.flush();
    	bw.close();
    }
    
    public static void change_switch(int[] switchs, int gender, int idx) {
    	//남자
    	if(gender == 1) {
    		for(int i = idx; i<switchs.length; i+=idx) {
    			switchs[i]^=1;
    		}
    	} else {
    		switchs[idx]^=1;
    		int range = 1;
    		while(true) {
    			if(isValid(N,idx+range)&& isValid(N,idx-range)) {
    				if(switchs[idx+range] == switchs[idx-range]) {
    					switchs[idx+range]^=1;
        				switchs[idx-range]^=1;
        				range++;
    				} else {
    					break;
    				}
    			} else {
    				break;
    			}
    		}
    	}
    }


    public static void main(String[] args) throws Exception {
        solution();
    }
    
    public static boolean isValid(int N, int idx) {
    	return 1<= idx && idx<=N;
    }
}
