
import java.util.*;
import java.io.*;

class Main
{
	
	static char[][] map;
 	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		

		/*
		 * 
		 * 매번 2등 선수가 누구인지 출력
		 * 여러명 가능
		 * 
		 * 랭킹에 있으면 +1점씩
		 * 
		 * 각 선수는 1~10000으로 구분
		 * 테스트케이스 여러개
		 * 
		 * N,M
		 * N주 동안의 매주 상위 M의 랭킹
		 * 
		 * N행의 인풋
		 * 한 주의 랭킹 정보
		 * 최고점의 선수는 단 한명
		 * 
		 * 메모리, 시간 부족해보여도 사실 탐색이 많이 않다
		 * 
		 * */
		List<Integer> list;
		List<Integer> list2;
		Set<Integer> set;
		int[] score;
		while(true) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			if(N ==0) break;
			score = new int[10001];
			for(int i = 0; i<N; i++) {
				st = new StringTokenizer(br.readLine());
				for(int j=0; j<M; j++) {
					score[Integer.parseInt(st.nextToken())]++;
				}
				/*
				 * 2등
				 * 1등보다 작고 3등보다 크다
				 * 메모리 충분 
				 * set등을 통해서 중복제거 내림차순의 2번째 수를 찾기
				 * Treeset을 통해서 정렬 구현
				 * 
				 * 2등을 구하기
				 * 매번 정렬해야한다
				 * 각 인덱스 = 선수번호
				 * 배열 정렬은 불가
				 * 
				 * 2등의 번호를 알면 2등인 인덱스만 찾으면 된다
				 * 
				 * Set -> List -> 정렬
				 * 10000 + 10000 + logN ) * 500
				 * 
				 * 20000 * 500
				 * 10 0000 00 천만 -> 시간 괜찮을듯
				 * 
				 * 애초에 문제 이해를 잘못했다
				 * 각 랭킹은 모든 주가 끝나고 정산
				 * 
				 * */
			}
			
			set = new HashSet<>();
			list = new ArrayList<>();
			for(int temp : score) {
				set.add(temp);
			}
			
			for(int temp : set) {
				list.add(temp);
			}
			Collections.sort(list,Collections.reverseOrder());
			int second = list.get(1);
			list2 = new ArrayList<>();
			//index를 알아야한다
			for(int j=0; j<score.length; j++) {
				if(second == score[j]) {
					list2.add(j);
				}
			}
			
			for(int j = 0; j<list2.size(); j++) {
				if(j != list2.size()-1) {
					bw.write(list2.get(j)+" ");
				} else {
					bw.write(list2.get(j)+"\n");
				}
			}
				
			
		}

		bw.flush();
		bw.close();
			
	}
 	

	
}