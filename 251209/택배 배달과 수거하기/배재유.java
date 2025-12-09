import java.util.*;


class Solution {
    static int max_len;
    public long solution(int cap, int n, int[] deliveries, int[] pickups) {
        
//         /*
//         트럭 하나로 모든 배달과 수거를 마치고 물류창고까지 돌아올 수 있는 최소 이동 거리
        
//         빈 재활용 택배 수거 가능
        
//         트럭에는 최대 cap개 가능
        
//         각 집에 배달 및 수거할 때 원하는만큼 가능
        
//         배달과 수거 2가지 
        
//         물류창고에서 몇 개 들고갈지
//         이후 어느 집을 어떻게 갈지 몇 개 갈지
        
//         최소 이동 거리 =  bfs or dp인데
//         이전의 상태 저장 ?
        
//         가장 많이 들고 이동하는 과정에서 다 뿌리고 회수
//         시작 박스에 따라서 그리디하게 ?
        
//         a = 배달할 상자 b = 빈 박스
//         a+b <=cap
        
//         while a--> 하면서
        
//         1. 창고 -> n, n->창고 자명한가? 
//         이게 최소다
        
//         매번 0이 아닌 집의 최대까지 다 돌아서
        
//         1) 현재 배달, 수거 모두 0이 아닌 max_length
//         2) for문 내림차순 가장 먼 집부터 처리하기
        
//         반복
        
        
//         */
        
//         int[] truck = new int[2];
//         find_max(deliveries,pickups);
//         int answer = 0;
        
//         //거리여서 0-idx아니다
//         //truck[0] 배달박스 [1] 수거박스 
//         for(int i=cap; n>= 0; i--) {
//             truck[0] = i;
//             answer+=max_len+1
//             while(true) {
//                 answer+=(max_len+1);
//                 for(int j = max_len; j>=0; j--) {
//                     /*
//                     1. 배달 항목 경우의 수 만들기 보다는 값으로서 비교
                    
//                     */
//                     if(truck[0] -deliveries[j] >= 0) {
//                         truck[0]-=deliveries[j]
//                         deliveries[j] =0;
                        
//                         if()
        
        int d_n = 0;
        int p_n = 0;
        long answer = 0;
        for(int i= n-1; i>=0; i--) {
            d_n+=deliveries[i];
            p_n+=pickups[i];
            

            while(d_n >0 || p_n >0) {
                answer +=(i+1)*2;
                d_n-=cap;
                p_n-=cap;
            }
            
        }
                        
      return answer;
    }
    
    // public void find_max(int[] deliveries, int[] pickups) {
    //     for(int i =0; i<n; i++) {
    //         if(deliveries[i] !=0 || pickups[i] != 0) {
    //             len_max = i;
    //         }
    //     }
    // }
}
