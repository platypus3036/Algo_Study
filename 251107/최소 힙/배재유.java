

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
    	 * 최소힙
    	 * 
    	 * 최소힙 구현보다 그냥 pq쓰자
    	 * 
    	 * 
    	 * */
    	
    	int N = Integer.parseInt(br.readLine());
    	
    	PriorityQueue<Integer> q= new PriorityQueue<>();
    	
    	for(int i = 0; i<N; i++) {
    		int num = Integer.parseInt(br.readLine());
    		if(num == 0) {
    			if(!q.isEmpty()) {
    				bw.write(q.poll()+"\n");
    			} else {
    				bw.write(0+"\n");
    			}
    		} else {
    			q.add(num);
    		}
    	}

    	
    	bw.flush();
    	bw.close();
         
    }
}
