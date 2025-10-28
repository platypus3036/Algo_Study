
import java.util.*;
import java.io.*;

class Main
{
 	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		/*
		 * 
		 * 1. 문제 정의
		 * 준현이와 성민이 중 누가 더 높은 수익률을 내는지
		 * 
		 * 2. 조건
		 * 준현이
		 * 살 수 있는 주식은 무조건 최대한 많이 산다
		 * 살 수 있다면 즉시 매수
		 * 
		 * 성민이
		 * 모든 거래는 전량 매수, 전량 매도, 빚내지는 않는다
		 * 
		 * 3일 연속 가격 상승 -> 3일 째에  무조건 매도 , 가격이 같은건 상승이 아니다
		 * 3일 연속 가격 하락 -> 3일 째에 무조건 매수,
		 * 
		 * 1월 1일 -> 14일까지 
		 * 14일의 자산
		 * 현금 + 1월 14일의 주가 x 주식 수
		 * 
		 * 3. 구현
		 * 준현이 -> 그리디
		 * 
		 * 성민이 -> q에 담아서 비교
		 * 
		 * 
		 * */
		
		int budget = Integer.parseInt(br.readLine());
		
		//zero-idx 제거하고 1부터 14로 처리하자
		int[] price = new int[15];
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		for(int i =1; i<=14; i++) {
			price[i] = Integer.parseInt(st.nextToken());
		}
		
		int sung = budget;
		int sung_stock = 0;
		int zun = budget;
		int zun_stock = 0;
		
		
		//1. 성민이
		int idx = 1;
		while(sung >= 0 && idx <= 14) {
			int cur_price = price[idx];
			if(sung / cur_price != 0) {
				sung_stock += sung/cur_price;
				sung -= (sung/cur_price) * cur_price;
			}
			idx++;
		}
		
		//2. 준현이

		
		for(int i=1; i<=11; i++) {
			//어짜피 14로 정해져있고, 그냥 돌면서 3개씩 확인해서 확인만 하면 된다
			if(price[i] < price[i+1] && price[i+1] < price[i+2]) {
				if(zun_stock != 0) {
					zun += zun_stock*price[i+3];
					zun_stock = 0;
				}
			} else if (price[i] > price[i+1] && price[i+1] > price[i+2]) {
				if(zun / price[i+3] != 0) {
					zun_stock += zun/price[i+3];
					zun -= (zun/price[i+3]) * price[i+3]; 
				}
			}
		}

		//지금 성민이랑 준현이 거꾸로 썻다
		
		int total_sung = sung + sung_stock*price[14];
		int total_zun = zun + zun_stock*price[14];
		if(total_sung < total_zun) {
			bw.write("TIMING");
		} else if (total_sung > total_zun) {
			bw.write("BNP");
		} else {
			bw.write("SAMESAME");
		}

		
	
		bw.flush();
		bw.close();
			
	}
 	
 	

	
}