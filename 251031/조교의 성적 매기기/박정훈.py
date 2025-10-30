'''
1. 문제 분석
총점을 같은 비율로 학생들에게 부여(N은 항상 10의 배수)
K번째 학생의 학점을 출력

입력값으로 중간, 기말, 과제 순으로 각 학생의 성적을 받음

2. 풀이 방법 고안
총점이 같은 학생은 주어지지 않기 때문에, sort(reverse=True)으로 성적순으로 나열하고, index를 찾으면 된다
'''
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    score_lst = [0] * N
    grade = [0] * N
    for student_idx in range(N):
        score_1, score_2, score_3 = map(int, input().split())
        score_lst[student_idx] = (score_1 * 35 + score_2 * 45 + score_3 * 20) / 100

    sort_score_lst = sorted(score_lst, reverse=True)
    for i in range(N):
        grade[score_lst.index(sort_score_lst[i])] = i+1

    grade_sample = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
    gap = N // 10
    grade_idx = (grade[K-1] - 1) // gap
    print(f'#{tc} {grade_sample[grade_idx]}')