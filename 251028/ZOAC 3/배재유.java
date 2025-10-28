
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
		 * 
		 * 문자열 출력 최소 시간
		 * 
		 * 자음 왼손 검지
		 * 모음 오른손 검지
		 * 
		 * 좌표 -> 좌표 이동 택시거리 (절대값 차이)
		 * 
		 * 키를 누르는 시간 1
		 * 동시에 두 손 움직이는거 불가
		 * 
		 * 구현
		 * 
		 * Map으로 좌표 미리 삽입하고 그냥 하는게
		 * 좌, 우 map 2개를 이용해서 key 자판 value 좌표이동 
		 * int left_idx right_idx 두 개로 상태 저장
		 * 
		 * 최소값
		 * 애초에 좌표 좌표 이동인데 그냥 이동이 최소값이 아닌가 ?
		 * 
		 * 배열은 참조 객체
		 * 그냥 x,y로 할당시키자
		 * map hash인데 get해봐야 결국 주소값을 가져온다
		 * 웬만하면 단일 객체에 할당시켜서 안전하게 처리하자
		 * 
		 * */
		
		Map<Character, int[]> left_map = new HashMap<>();
		Map<Character, int[]> right_map = new HashMap<>();
		
		left_map.put('q',new int[] {0,0});
		left_map.put('w',new int[] {0,1});
		left_map.put('e',new int[] {0,2});
		left_map.put('r',new int[] {0,3});
		left_map.put('t',new int[] {0,4});
		left_map.put('a',new int[] {1,0});
		left_map.put('s',new int[] {1,1});
		left_map.put('d',new int[] {1,2});
		left_map.put('f',new int[] {1,3});
		left_map.put('g',new int[] {1,4});
		left_map.put('z',new int[] {2,0});
		left_map.put('x',new int[] {2,1});
		left_map.put('c',new int[] {2,2});
		left_map.put('v',new int[] {2,3});
		
		right_map.put('y', new int[] {0,5});
		right_map.put('u', new int[] {0,6});
		right_map.put('i', new int[] {0,7});
		right_map.put('o', new int[] {0,8});
		right_map.put('p', new int[] {0,9});
		right_map.put('h', new int[] {1,5});
		right_map.put('j', new int[] {1,6});
		right_map.put('k', new int[] {1,7});
		right_map.put('l', new int[] {1,8});
		right_map.put('b', new int[] {2,4});
		right_map.put('n', new int[] {2,5});
		right_map.put('m', new int[] {2,6});
		
		String input = br.readLine();
		char left_start = input.charAt(0);
		char right_start = input.charAt(2);
		//첫 번째는 시작위치가 변경될 수 있다
		int[] left;
		int[] right;
		if (left_map.containsKey(left_start)) {
            left = left_map.get(left_start).clone();
        } else {
            left = right_map.get(left_start).clone();
        }

        if (right_map.containsKey(right_start)) {
            right = right_map.get(right_start).clone();
        } else {
            right = left_map.get(right_start).clone();
        }
		
		
		int time = 0;
		String str = br.readLine();
		for(int i = 0; i<str.length(); i++) {
			char cur = str.charAt(i);
			if(left_map.containsKey(cur)) {
				//좌측
				int[] next_point = left_map.get(cur);
				time += Math.abs(next_point[1]-left[1]) + Math.abs(next_point[0]-left[0]);
				//누르는 시간
				time++;
				//손가락 옮기기
				left[0] = next_point[0];
				left[1] = next_point[1];
			} else {
				//우측
				int[] next_point = right_map.get(cur);
				time += Math.abs(next_point[1]-right[1]) + Math.abs(next_point[0]-right[0]);
				//누르는 시간
				time++;
				//손가락 옮기기
				right[0] = next_point[0];
				right[1] = next_point[1];
			}
			
			
		}
		
		bw.write(time+"");
		bw.flush();
		bw.close();
			
	}
 	

	
}