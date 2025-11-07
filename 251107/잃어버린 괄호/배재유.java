
import java.util.*;
import java.io.*;

public class Main
{
    public static void main(String args[]) throws Exception
    {
    	
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    	
    	/*
    	 * 괄호쳐서 값 최소
    	 * 
    	 * 최소값
    	 * -나오고 + 나올때까지 전부 괄호
    	 * 
    	 * 
    	 * 
    	 * */
    	String input = br.readLine();
    	boolean first = false;
    	int base = 0;
    	StringBuilder sb;
    	int before_ope_idx = 0;
    	char before_ope = ' ';
    	for(int i = 0; i<input.length(); i++) {
    		if(!first) {
    			if (input.charAt(i)-'0' <0 || input.charAt(i)-'0' >9) {
    				first = true;
    				sb = new StringBuilder();
    				for(int j=0; j<i; j++) {
    					sb.append(input.charAt(j));
    				}
    				base = Integer.parseInt(sb.toString());
    				before_ope_idx= i;
    				before_ope = input.charAt(i);
    			}
    		} else {
    			if(input.charAt(i)-'0' <0 || input.charAt(i)-'0' >9) {
    				if(before_ope == '-') {
    					sb = new StringBuilder();
    					for(int j=before_ope_idx+1; j<i; j++) {
    						sb.append(input.charAt(j));
    					}
    					base -=Integer.parseInt(sb.toString());
    					before_ope_idx = i;
    					if(input.charAt(i) == '-') {
    						before_ope = input.charAt(i);
    					}
    				} else {
    					sb = new StringBuilder();
    					for(int j=before_ope_idx+1; j<i; j++) {
    						sb.append(input.charAt(j));
    					}
    					base +=Integer.parseInt(sb.toString());
    					before_ope_idx = i;
    					if(input.charAt(i) == '-') {
    						before_ope = input.charAt(i);
    					}
    				}
    			}
    		}
    	}
    	// 마지막 num처리
    	if(before_ope == '-') {
    		sb = new StringBuilder();
			for(int j=before_ope_idx+1; j<input.length(); j++) {
				sb.append(input.charAt(j));
			}
			base -=Integer.parseInt(sb.toString());
    	} else if (before_ope == '+'){
    		sb = new StringBuilder();
			for(int j=before_ope_idx+1; j<input.length(); j++) {
				sb.append(input.charAt(j));
			}
			base +=Integer.parseInt(sb.toString());
    	} else {
            //그냥 숫자만 들어오는 경우
    		sb = new StringBuilder();
    		for(int j=before_ope_idx; j<input.length(); j++) {
				sb.append(input.charAt(j));
			}
			base +=Integer.parseInt(sb.toString());
    	}
    	
    	bw.write(base+"");
    	bw.flush();
    	bw.close();
         
    }
}
