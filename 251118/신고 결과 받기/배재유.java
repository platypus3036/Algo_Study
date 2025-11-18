import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        
        /*
        유저별 처리 결과 메일을 받은 횟수
        
        한 번에 한 명의 유저만 신고 가능
        서로 다른 유저 계속해서 신고 가능
        
        동일 유저 신고 = 1회로 처리
        
        K번 이상 신고된 유저 = 정지
        해당 유저를 신고한 모든 유저에게 정지 사실 메일로 발송
        
        Map 사용
        split으로 구분
        
        map을 두 개 써서 신고 횟수, 신고한 사람 구분하여
        for -> map
        
        report -> 200000
        어짜피 1회 탐색, 그리고 map이여서 key로 검색 -> O(1)
        
        */
        //list가 아니라 set에 담아서 contains + 중복 처리
        Map<String, Set<String>> reportList = new HashMap<>();
        Map<String, Integer> trollerCnt = new HashMap<>();
        Map<String, Integer> reportCnt = new HashMap<>();
        for(int i = 0; i<report.length; i++) {
            String reporter = report[i].split(" ")[0];
            String troller = report[i].split(" ")[1];
            
            //set -> 신고자, [신고받은사람]
            //cnt -> 트롤 , cnt
            //참고 set.add는 반환값이 boolean t/f 이다.
            reportList.putIfAbsent(reporter, new HashSet<String>());
            if(!reportList.get(reporter).contains(troller)) {
                reportList.get(reporter).add(troller);
                trollerCnt.put(troller,trollerCnt.getOrDefault(troller,0)+1);
            }
            
            //이렇게 되면 중복 신고처리 불가 -> 했다 안했다 -> boolean ? 
            // trollerCnt.put(troller,trollerCnt.getOrDefault(troller,0)+1);
        }
        
        int[] answer = new int[id_list.length];
        
        //트롤 for reporter
        //index를 알면 더 빠르니까 
        //각 reporter 돌면서 find
        
        for(String reporter: reportList.keySet()) {
            Set<String> set = reportList.get(reporter);
            for(String troller : set) {
                
                if(trollerCnt.get(troller) >= k) {
                    reportCnt.put(reporter,reportCnt.getOrDefault(reporter,0)+1);
                }
            }
        }
        
        for(String temp : reportCnt.keySet()) {
            System.out.println(temp);
        }
        
        // System.out.println(reportCnt);
        for(int i = 0; i<id_list.length; i++) {
            answer[i] = reportCnt.getOrDefault(id_list[i],0);
        }
        
        
        
        
        return answer;
    }
}
