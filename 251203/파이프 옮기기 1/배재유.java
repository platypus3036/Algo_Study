package org.scoula.algorithm;

import java.io.*;
import java.util.*;

class Main {
    static int N;
    static int[][] map;
    static int[][][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        /*
        *
        * bfs로 했는데 안된다
        *
        * 기존의 3차원은 맞지만 dp로 처리
        *
        *
        * */

        /*
         *
         * 파이프의 한쪽 끝을 (N, N)으로 이동시키는 방법의 개수
         *
         * 파이프 경우
         * 2,1
         * 1,2
         * 2,2
         *
         * 밀면서 회전 가능
         *
         * 이동불가하면 0 출력
         * 빈칸만 이동 가능
         * 회전은 45도만 가능
         *
         * 회전과 별개로 각 방향에 대해서
         * 갈 수 있는 방법
         *
         * 좌 우 좌표에 대해서 따로 저장해서 처리하는게
         *
         * 방법의 개수 = 완탐 ?
         * 그런데 현재 파이프 상태에 대해서 경우의 수 누적 = 메모리제이션
         * 계속 이동시키면서 각 좌표에 대해서 dp 누적
         * 근데 좌표가
         * [16][16][16][16]
         * 17^4
         * 괜찮다
         * */



        //완탐처럼 bfs로 뒤로 가는 이동 방법이 없기 때문에
        //dp의 경우 끝좌표면 저장하면 되긴한다

//        int[][] map = new int[N+1][N+1];
//        for(int i = 1; i<=N; i++) {
//            st = new StringTokenizer(br.readLine());
//            for(int j = 1; j<=N; j++) {
//                map[i][j] = Integer.parseInt(st.nextToken());
//            }
//        }

        //현재 좌표, 상태 필요
        //상태 저장 방법 배열이 답인가?
        //방향만 알면 끝점좌표는 고정이니 굳이 따질 필요가 있는가?
        //끝좌표, 상태로
//        boolean[][][] visited=  new boolean[N+1][N+1][3];
//        Deque<int[]> q = new ArrayDeque<>();
//        q.add(new int[]{1,2,0});
//        while(!q.isEmpty()) {
//            int[] cur = q.poll();
//            int ey = cur[0];
//            int ex = cur[1];
//            int dir = cur[2];
//
//            System.out.println(ey+" "+ex);
//            if(ex == N && ey == N) {
//                continue;
//            }
//
//            if(dir ==0) {
//                //cur (2,3)
//                if(isValid(ey+1,ex+1) && map[ey][ex+1] ==0 && map[ey+1][ex+1] == 0 && map[ey+1][ex] == 0) {
//
//                    q.add(new int[]{ey+1,ex+1,2});
//                    dp[ey+1][ex+1] +=1;
//                    visited[ey+1][ex+1][2] = true;
//
//                }
//
//                if(isValid(ey,ex+1) && map[ey][ex+1] == 0) {
//
//                    q.add(new int[]{ey,ex+1,0});
//                    dp[ey][ex+1] +=1;
//                    visited[ey][ex+1][0] = true;
//                }
//            } else if (dir ==1) {
//                if(isValid(ey+1,ex+1) && map[ey][ex+1] ==0 && map[ey+1][ex+1] == 0 && map[ey+1][ex] == 0) {
//
//                    q.add(new int[]{ey+1,ex+1,2});
//                    dp[ey+1][ex+1] +=1;
//                    visited[ey+1][ex+1][2] = true;
//
//                }
//                if(isValid(ey+1,ex) && map[ey+1][ex] == 0) {
//
//                    q.add(new int[]{ey+1,ex,1});
//                    dp[ey+1][ex] +=1;
//                    visited[ey+1][ex][1] = true;
//
//                }
//            } else {
//                if(isValid(ey+1,ex+1) && map[ey][ex+1] ==0 && map[ey+1][ex+1] == 0 && map[ey+1][ex] == 0) {
//
//                    q.add(new int[]{ey+1,ex+1,2});
//                    dp[ey+1][ex+1] +=1;
//                    visited[ey+1][ex+1][2] = true;
//
//                }
//
//                if(isValid(ey,ex+1) && map[ey][ex+1] == 0) {
//
//                    q.add(new int[]{ey,ex+1,0});
//                    dp[ey][ex+1] +=1;
//                    visited[ey][ex+1][0] = true;
//
//                }
//                if(isValid(ey+1,ex) && map[ey+1][ex] == 0) {
//                    q.add(new int[]{ey+1,ex,1});
//                    dp[ey+1][ex] +=1;
//                    visited[ey+1][ex][1] = true;
//
//                }
//            }
//        }


        N = Integer.parseInt(br.readLine());
        map = new int[N + 1][N + 1];
        dp = new int[N + 1][N + 1][3];

        StringTokenizer st;
        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dp[1][2][0] = 1;

        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                if (map[i][j] == 1) continue;


                dp[i][j][0] += dp[i][j - 1][0] + dp[i][j - 1][2];


                if (i > 1) {
                    dp[i][j][1] += dp[i - 1][j][1] + dp[i - 1][j][2];
                }

                if (i > 1 && j > 1 && map[i - 1][j] == 0 && map[i][j - 1] == 0) {
                    dp[i][j][2] += dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1] + dp[i - 1][j - 1][2];
                }
            }
        }

        int result = dp[N][N][0] + dp[N][N][1] + dp[N][N][2];
        bw.write(String.valueOf(result));
        bw.flush();
        bw.close();
    }
}
