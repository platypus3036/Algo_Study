'''
1. 문제 해석
스위치의 처음 상태가 주어지고, 각 학생들이 순서대로 스위치를 조작
학생의 성별에 따라 조작하는 방법이 다름
1) 남성 : 받은 수의 배수 번호들을 반대로 조작
2) 여성 : 받은 수를 기준으로, 좌우의 상태가 대칭인 최대의 범위를 모두 반대로 조작
모든 학생들이 조작한 뒤의 마지막 상태를 출력

2. 방법 찾기
스위치 개수가 100 이하, 학생수가 100 이하
제한시간은 2초
차례대로 완전 탐색해도 시간이 충분함

3. 고려사항
스위치의 처음 상태를 리스트로 받고, 20개씩 끊어서 언패킹으로 출력
학생이 여성이 경우, 최대의 범위를 찾는 과정에서 전체 범위를 벗어나지 않아야 함
'''
N = int(input())
switch = list(map(int, input().split()))
student = int(input())
for stud in range(student):
    gender, switch_num = map(int, input().split())

    if gender == 1:   # 남성일 경우
        for i in range(switch_num, N+1, switch_num):
            if switch[i-1] == 1:
                switch[i-1] = 0
            else:
                switch[i-1] = 1

    else:    # 여성일 경우
        width = 1       # 받은 수를 기준으로 좌우 너비
        if switch[switch_num - 1] == 1:  # 받은 수의 스위치 바꾸기
            switch[switch_num - 1] = 0
        else:
            switch[switch_num - 1] = 1
        while switch_num - 1 - width >= 0 and switch_num - 1 + width < N:
            if switch[switch_num - 1 - width] == 1 and switch[switch_num - 1 + width] == 1:
                switch[switch_num - 1 - width] = 0
                switch[switch_num - 1 + width] = 0
            elif switch[switch_num - 1 - width] == 0 and switch[switch_num - 1 + width] == 0:
                switch[switch_num - 1 - width] = 1
                switch[switch_num - 1 + width] = 1
            else:
                break
            width += 1

for i in range(len(switch) // 20 + 1):
    print(*switch[20 * i : 20 * (i + 1)])
