import java.util.*;
import java.io.*;
 
class Solution
{
     
    static char[][] map;
    public static void main(String args[]) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
         
 
        /*
         * 
         * 최소 몇 번 양을 세었을 때 이전에 봤던 숫자들의 자릿수에서 0에서 9까지 모든 숫자 보게 되는지
         * 
         * 0부터 9까지 모든 숫자를 보게 되는지 출력
         * 
         * set으로 확인
         * 
         * 그냥 검사 종료될 때 종료
         * 
         * 
         * 
         * */
         
        int T = Integer.parseInt(br.readLine());
        for(int tc=1; tc<= T; tc++) {
            int N = Integer.parseInt(br.readLine());
            Set<Character> set = new HashSet<>();
//          int cnt = 1;
            int num = N;
            while(true) {
                //N을 쪼개어
                String str = num+"";
                for(int i = 0; i<str.length(); i++) {
                    set.add(str.charAt(i));
                }
                if(check_num(set)) {
                    break;
                }
                //2의 배수가 아니라 N의 배수
                num+=N;
            }
            //출력도 현재  num
            bw.write(String.format("#%d %d\n",tc,num));
        }
 
         
 
         
         
         
 
 
        bw.flush();
        bw.close();
             
    }
     
    public static boolean check_num(Set<Character> set) {
//      System.out.println(set);
 
        return set.size() == 10;
    }
     
 
     
}
