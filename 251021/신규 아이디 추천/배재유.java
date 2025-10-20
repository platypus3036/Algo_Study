import java.util.*;


class Solution {
    public String solution(String new_id) {
        /*
        1.목표
        단계별 구현
        
        2. 조건
        N <= 1000
        그냥 생 구현 같다
        
        
        
        
        */
        
        StringBuilder sb = new StringBuilder();
        
        //1. 대문자 -> 소문자
        //toLowerCase 메서드는 인스턴스 메서드, 해당 객체를 변경하는 것
        String case1 = new_id.toLowerCase();
        //2. 알파벳 소문자, 숫자, - , _, 마침표 제외
        for(int i = 0; i<case1.length(); i++) {
            if((case1.charAt(i)>= 'a' && case1.charAt(i)<= 'z') || (case1.charAt(i)-'0' >= 0 && case1.charAt(i)-'0'<=9) || case1.charAt(i)== '-' || case1.charAt(i)== '_' || case1.charAt(i)== '.') {
                sb.append(case1.charAt(i));
            }
        }
        String case2 = sb.toString();
        //끝나고 sb정리
        sb.setLength(0);
        
        //3. .가 2번 이상 연속된 부분을 하나의 .로 치환
        int point_cnt = 0; 
        for(int i =0; i<case2.length(); i++) {
            if(case2.charAt(i) == '.') {
                point_cnt++;
            } else {
                if(point_cnt > 0) {
                    sb.append('.');
                    point_cnt = 0;
                }
                sb.append(case2.charAt(i));
            }
        }
        
        if(point_cnt >0) {
            sb.append('.');
        }
        
        String case3 = sb.toString();
        
        //sb 초기화
        sb.setLength(0);

        //4. .이 처음이나 끝에 위치하면 제거
        Deque<Character> q= new ArrayDeque<>();
        for(int i = 0; i<case3.length(); i++) {
            q.add(case3.charAt(i));
        }
        
        while(!q.isEmpty() && q.peekFirst() == '.') {
            q.pollFirst();
        }
        
        while(!q.isEmpty() && q.peekLast() == '.') {
            q.pollLast();
        }
        
        while(!q.isEmpty()) {
            sb.append(q.poll());
        }
        
        String case4 = sb.toString();
        sb.setLength(0);
        q.clear();
        //5. case4가 빈배열이면 a 대입
        if(case4.equals("")) {
            case4 += "a";
        }

        
        //6. 16자 이상이면 15개제외하고 전부제거
        // 제거후 .가 끝에 위치하면 끝에 위치한 문자 제거
        
        String case6 = "";
        if(case4.length() >= 16) {
            for(int i = 0 ; i<15; i++) {
                q.add(case4.charAt(i));
            }
            while(q.peekLast()=='.') {
                q.pollLast();
            }
            
            while(!q.isEmpty()) {
                sb.append(q.poll());
            }
            
            case6 = sb.toString();
            
        } else {
            case6 = case4;
        }
        //sb
        sb.setLength(0);
        // System.out.println(case6);
        //7. 길이가 2이하면 마지막 문자를 길이가 3이 될 때까지 반복
        
        String case7 = "";
        if(case6.length() <=2 &&case6.length() >0 ) {
            char last = case6.charAt(case6.length()-1);
            for(int i=0; i<case6.length(); i++) {
                sb.append(case6.charAt(i));
            }
            
            while(sb.length() <3) {
                sb.append(last);
            }
            case7 = sb.toString();
        } else {
            case7 = case6;
        }
        // System.out.println(case7);
        
    
        
        
        
        
        
        String answer = case7;
        return answer;
    }
}