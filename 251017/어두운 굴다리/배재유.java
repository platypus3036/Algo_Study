

import java.util.*;
import java.io.*;

public class Main {


    public static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        /*
         * 1. 목표
         * 굴다리를 모두 비추기 위한 가로등의 최소 높이
         * 
         * 2. 조건
         * 가로등 설치 개수 M, 위치 x결정
         * 가로등은 높이만큼 주위를 비출 수 있다
         * 모든 가로등의 높이는 같아야 하고, 정수
         * 
         * 첫 번째 줄 N 굴다리 길이
         * 두 번째 줄 M 가로등 개수
         * M개의 가로등 위치 x 주어짐
         * 
         * 3. 구현
         * 모든 길이를 돈다 -> ?
         * 결국 0, 가로등 위치 , 가로등 위치 그냥 따져가면서 Math.max하면서 최소 길이 찾으면 될 듯
         * 
         * 좌,우 모두를 비춘다 -> 좌우 모두 비교 ? 
         * 
         * Math.max가 아니다
         * 길을 비춘다
         * * 길을 비춘다 = 최소한으로 모든 거리를 모두 비춘다 
         * 같은 말 아닌가
         * 최소값이니 Math.max가 아니라 0이 아닌 수 min도 아닌데 
         * 좌 우를 생각을 못했네
         * 비교할 때 
         * 0 -> 1번 장소
         * 끝자리가 아니면 사이간 절반만 가더라도 가능
         * 최소는 0~1번가로등 /끝가로등 -> 끝자리 
         * 이후에는 절반씩만 가도 된다 
         * 
         *  
         * */
        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());
        List<Integer> list = new ArrayList<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i<M; i++) {
        	list.add(Integer.parseInt(st.nextToken()));
        }
        //1. 최소 길이
        Collections.sort(list);
        int answer = 0;
        answer = Math.max(list.get(0)-0, N-list.get(list.size()-1));
        
        //어짜피 초기값 설정 = list.size() == 1 짜리 처리
        if (list.size()>1) {
        	for(int i = 0; i<list.size(); i++) {
            	if(i == 0) {
            		//절반이 가능해도 다 덮으러면 올림해서
            		//Math.ceil는 double 타입 
            		//정수 연산으로 올림 구현해야한다
            		//gap +1 /2 로 해서 정수 올림 처리 
            		int gap = list.get(i+1)- list.get(i);
            		int ceil_num = (gap+1)/2;
            		answer = (int) Math.max(answer, ceil_num);
            	} else if (i == list.size()-1) {
            		int gap = list.get(i)- list.get(i-1);
            		int ceil_num = (gap+1)/2;
            		answer = (int) Math.max(answer, ceil_num);
            	} else {
            		int gap1 = list.get(i+1)- list.get(i);
            		int gap2 = list.get(i)- list.get(i-1);
            		int ceil_num1 = (gap1+1)/2;
            		int ceil_num2 = (gap2+1)/2;
            		answer = (int) Math.max(answer, ceil_num1);
            		answer = (int) Math.max(answer, ceil_num2);
            	}
            }
        }
        
        
      

        
        
        bw.write(answer+"");
        	

    	bw.flush();
    	bw.close();
    }
    
   
    public static void main(String[] args) throws Exception {
        solution();
    }
    


}
