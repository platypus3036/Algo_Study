

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
    	 * 길이가 M인 수열 모두 구하기
    	 * 
    	 * 1~N까지 자연수 중 M개를 고른 수열
    	 * 
    	 * 같은 수를 여러 번 골라도 된다
    	 * 고른 수열은 비내림차순 = 올림+같은 수 가능
    	 * 
    	 * 이거 그냥 백트래킹 = 완탐
    	 * for문의 개수 = M개
    	 * 메모리 유의
    	 * M = 8까지는 List 크기 괜찮다
    	 * 
    	 * */
    	
    	StringTokenizer st = new StringTokenizer(br.readLine());
    	
    	int N = Integer.parseInt(st.nextToken());
    	int M = Integer.parseInt(st.nextToken());
    	
    	//여기서만 새 리스트 생성
    	//지금 순열만들었다 다음 수에 대해서 인지는 하고 있어야 한다
    	dfs(N,M,1,new ArrayList<>());



    	bw.flush();
    	bw.close();
         
    }
    
    public static void dfs(int N, int M,int num,List<Integer> list) throws IOException {
    	if(list.size()==M) {
    		StringBuilder sb = new StringBuilder();
    		for(int i = 0; i<list.size(); i++) {
    			if(i != list.size()-1) {
    				sb.append(list.get(i)+" ");
    			} else {
    				sb.append(list.get(i)+"\n");
    			}
    		}
    		bw.write(sb.toString());
    		return;
    	}
    	
    	
    	for(int i = num; i<=N; i++) {
    		list.add(i);
    		dfs(N, M,i,list);
    		list.remove(list.size()-1);
    	}
    }
    
    
}
