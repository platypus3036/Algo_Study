

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
    	 * 도착점에 도착하게 하는 최소 주사위 수
    	 * 
    	 * 10x10
    	 * 맵에 1~100까지 적혀잇다
    	 * 
    	 * i 자리 -> 주사위 j -> i+j로 이동
    	 * i+j > 100 이동 불가
    	 * 도착한 칸 사다리 -> 사다리타고
    	 * 도착한 칸 뱀 -> 뱀타고
    	 * 
    	 * 
    	 * 현재 map에서 1~100까지 어떻게 도달인지 표기 x
    	 * -> dp로
    	 * 
    	 * dp가 안되나 ?
    	 * 
    	 * 
    	 * */
    	
    	
    	StringTokenizer st = new StringTokenizer(br.readLine());
    	
    	int N = Integer.parseInt(st.nextToken());
    	int M = Integer.parseInt(st.nextToken());
    	
    	boolean[] visited = new boolean[101];
    	int[] way = new int[101];
    	for(int i =0; i<N; i++) {
    		st = new StringTokenizer(br.readLine());
    		way[Integer.parseInt(st.nextToken())] = Integer.parseInt(st.nextToken());
    	}
    	for(int i =0; i<M; i++) {
    		st = new StringTokenizer(br.readLine());
    		way[Integer.parseInt(st.nextToken())] = Integer.parseInt(st.nextToken());
    	}
    	Deque<int[]> q = new ArrayDeque<>();
    	q.add(new int[] {1,0});
    	visited[1] = true;
    	int answer = 0;
    	while(!q.isEmpty()) {
    		int[] cur = q.poll();
    		int cidx = cur[0];
    		int ccnt = cur[1];
    		
    		if(cidx == 100) {
    			answer = ccnt;
    			break;
    		}
    		
    		
    		for(int i = 1; i<=6; i++) {
    			if(cidx+i <= 100 && !visited[cidx+i]) {
    				if(way[cidx+i] == 0) {
    					q.add(new int[] {cidx+i,ccnt+1});
    				} else {
    					q.add(new int[] {way[cidx+i],ccnt+1});
    					visited[way[cidx+i]] = true;
    				}
    				visited[cidx+i] = true;
    			}
    		}
    	}
    	
    	
    	
    	
    	


    	bw.write(answer+"");
    	bw.flush();
    	bw.close();
         
    }
}
