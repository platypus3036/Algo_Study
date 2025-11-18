import java.util.*;


class Solution {
    public int[] solution(String[] info, String[] query) {
        
        
        /*
        50000 * 100000 => 무조건 넘친다
        
        0 = 모두 0보다 크거나 같다 처리
        
        현재 문제는 조건 -> info 탐색이 너무 오래 걸린다
        
        String 결합으로 처리하기 -> - 처리가 안된다
        
        info + query로 해야지 문제 해결
        
        일종의 트리 -> 중간 값 - 처리 불가
        
        합집합 = 진짜 비트마스킹 같은데
        
        분할 마킹은 가성비 떨어진다
        
        cpp 1 java 2 python 3 backend 4 frontend ... 해서 이 값 안에 존재하는지
        
        근데 이거 애초에 50000*5 도 안되면 불가능하다
        
        교집합의 개념이 들어가야 한다 
        
        - 그러면 그냥 모든 자리마다 -를 추가하여서 
        언어의 -, 직군의 -, 경력의 -,
        
        언어 - 1, java 2 cpp 3 python 4 
        
        1<<1, 1<<2 and 1<<5, 1<<7 and + 점수 기억
        마스킹해도 결국 완탐 + 점수 기억 못함
        1123 = 0
        
        
        */
        
        
        int[][] visited = new int[info.length][5];
        Map<String,List<Integer>> score = new HashMap<>();

        StringBuilder sb = new StringBuilder();
        for(int i = 0; i<info.length; i++) {
            String[] temp = info[i].split(" ");
            String[][] cv = new String[4][2];
            for(int j=0; j<4; j++) {
                cv[j][0] = temp[j];
                cv[j][1] = "-";
            }
            //2^4 16개씩 Map에 추가 -> 24 * 50000 1200000 삽입 
            //-에 속한 모든 경우의 수 키값 저장
            //value에 list로 탐색 가능 ? ?? 
            
            for(int j = 0; j<2; j++) {
                for(int k=0; k<2; k++) {
                    for(int l=0; l<2; l++) {
                        for(int m=0; m<2; m++) {
                            sb.setLength(0);
                            sb.append(cv[0][j]);
                            sb.append(cv[1][k]);
                            sb.append(cv[2][l]);
                            sb.append(cv[3][m]);
                            String key = sb.toString();
                            // 자료구조면 분리해서 
                            score.putIfAbsent(key,new ArrayList<>());
                            score.get(key).add(Integer.parseInt(temp[4]));
                        }
                    }
                }
            }

            
        }
        for (List<Integer> list : score.values()) {
            Collections.sort(list);
        }
        int[] answer = new int[query.length];
        //key -> 바로 값 나오도록
        for(int i = 0; i<query.length; i++) {
            String[] filter = query[i].split(" and ");
            int score_filter = Integer.parseInt(filter[3].split(" ")[1]);
            sb.setLength(0);
            for(int j=0; j<3; j++) {
                sb.append(filter[j]);
            }
            sb.append(filter[3].split(" ")[0]);

            List<Integer> cv_list = score.get(sb.toString());
            //효율성 통과 못함 -> 이분탐색으로 (참고)
            if (cv_list != null) {
                int left = 0;
                int right = cv_list.size(); 

                while (left < right) {
                    int mid = (left + right) / 2;
                    if (cv_list.get(mid) >= score_filter) {
                        right = mid;
                    } else {
                        left = mid + 1;
                    }
                }
                answer[i] = cv_list.size() - left;
            }
                
            
        }
        
        
        
        
        return answer;
    }
}
