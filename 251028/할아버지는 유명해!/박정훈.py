'''
1. 문제 분석
각 테스트케이스에서 최고점의 선수는 단 한명만 존재
각 줄은 선수번호가 올라오는데, 줄에 번호가 올라오면 포인트 +1
2등인 선수들의 번호를 출력

2. 풀이 방법 고안
index를 저장하는 list를 만들어서, 포인트를 저장
list를 오름차순으로 두고, [1]의 포인트를 확인
전체 list에서 [1]의 포인트와 같은 값들을 따로 저장 후 출력
'''
while True:
    N, M = map(int, input().split())
    if N==M==0:
        break

    point = [0] * 10001

    for _ in range(N):
        arr = list(map(int, input().split()))
        for num in arr:
            point[num] += 1

    second = sorted(point, reverse=True)[1]

    for i in range(10001):
        if point[i] == second:
            print(i, end=" ")
    print()