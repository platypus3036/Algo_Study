package org.scoula.algorithm;

import java.io.*;
import java.util.*;

class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        /*
        *
        * 반지름 i -> i번 째
        * M개의 정수 원판에
        * i번째 원판 j번째 수  i, j
        *
        * i, 1 = i,2 , i, m과 인접
        * i, m = i,m-1, i,1 과 인접
        * i,j = i, j-1, i, j+1 (2<= j <= M-1)
        * 1, j = 2, j와 인접
        * N, j는 N-1, j와 인접
        * i,j 는 i-1,j, i+1,j와 인접
        *
        * 조건 6개
        *
        * T번 회전시킨 후 원판에 적힌 수의 합
        *
        * 1. xi 배수원판을 d1방향으로 ki칸 회전 (di 0 시계 1 반시계)
        * 2. 원판에 수가 남아 있으면 인접하면서 수가 같은 것 모두 찾기
        * 3-1. 수 있으면 -> 인접, 같은 수 전부 제거
        * 3-2. 수 없으면 -> 원판의 평균 평균보다 큰수 -1, 평균보다 작은수 +1
        *
        *
        * 수 배치
        * 12시부터 시계방향으로
        *
        * 1. 회전
        * 원판 50 * 50 ->
        * 허용
        * LinkedList는 과하다
        *
        * 회전 -> 인접 조건 확인 -> 처리
        * 반복
        *
        *
        *
        * */

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int T = Integer.parseInt(st.nextToken());

        //각 deque에 대해서 index로 접근하여 회전시켜야한다
        //모든 접근에 대해서 index로 접근가능해야 처리 가능
        //배열 사용해야한다 -> 메모리 재사용 고려
        int[][] arr = new int[N+1][M+1];
        //0-idx
        for(int i = 1; i<=N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j=1; j<=M; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        //x d k
        //배수 방향 칸
        Deque<Integer> q = new ArrayDeque<>();
        for(int i = 0; i<T; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());
            boolean iscon = false;
            for(int j=x; j<=N; j+=x) {
                // x배수의 원판
                //1. 회전 0 시계 tail->head, 1 반시계 head -> tail
                q.clear();
                for(int l=1; l<=M; l++) {
                    q.add(arr[j][l]);
                }

                if(d == 0) {
                    //재활용 deque 사용하기
                    for(int l=0; l<k; l++) {
                        q.addFirst(q.pollLast());
                    }

                } else {
                    for(int l=0; l<k; l++) {
                        q.addLast(q.pollFirst());
                    }
                }

                for(int l = 1; l<=M; l++) {
                    arr[j][l] = q.poll();
                }

            }
            boolean[][] needChange = new boolean[N+1][M+1];
            //2. 인접 수 찾기 인접수는 완탐으로 다 검사해야한다
            for(int l = 1; l <= N; l++) {
                for(int a = 1; a <= M; a++) {
                    if(arr[l][a] == -1) continue;

                    int num = arr[l][a];

                    // 좌
                    int left = (a == 1) ? M : a - 1;
                    if(arr[l][left] != -1 && arr[l][left] == num) {
                        needChange[l][a] = true;
                        needChange[l][left] = true;
                        iscon = true;
                    }

                    // 우
                    int right = (a == M) ? 1 : a + 1;
                    if(arr[l][right] != -1 && arr[l][right] == num) {
                        needChange[l][a] = true;
                        needChange[l][right] = true;
                        iscon = true;
                    }

                    // 상
                    if(l > 1) {
                        if(arr[l-1][a] != -1 && arr[l-1][a] == num) {
                            needChange[l][a] = true;
                            needChange[l-1][a] = true;
                            iscon = true;
                        }
                    }

                    // 하
                    if(l < N) {
                        if(arr[l+1][a] != -1 && arr[l+1][a] == num) {
                            needChange[l][a] = true;
                            needChange[l+1][a] = true;
                            iscon = true;
                        }
                    }
                }
            }

            //인접한게 없다면
            //인접 여부는 원판 단위로
            if(!iscon) {
                double sum = 0;
                int cnt = 0;
                for(int l = 1; l<=N; l++) {
                    for (int a = 1; a <= M; a++) {
                        if (arr[l][a] != -1) {
                            sum += arr[l][a];
                            cnt++;
                        }
                    }
                }
                sum /= cnt;
                for(int l = 1; l<=N; l++) {
                    for(int a = 1; a<=M; a++) {
                        if (arr[l][a] == -1) continue;

                        if(arr[l][a] > sum) {
                            arr[l][a]--;
                        } else if (arr[l][a] < sum) {
                            arr[l][a]++;
                        }
                    }
                }

            } else {
                for(int j=1; j<=N; j++) {
                    for(int l =1; l<=M; l++) {
                        if(needChange[j][l]) {
                            arr[j][l] = -1;
                        }
                    }
                }
            }
        }

        int answer = 0;
        for(int i= 1; i<=N; i++) {
            for (int j = 1; j<=M; j++) {
                if(arr[i][j] !=-1) {
                    answer+=arr[i][j];
                }
            }
        }

        bw.write(answer+"");
        bw.flush();
        bw.close();
    }

}
