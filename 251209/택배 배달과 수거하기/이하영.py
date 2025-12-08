import sys
sys.stdin = open('input2.txt')


"""
함수만 작성
-----
cap = 트럭에 실을 수 있는 상자 최대 개수
n = 일렬로 나열된 집의 수
    물류창고 0 번  / 트럭 초기 위치
    i번 째 집은 물류창고에서 i만큼 떨어져있음.
    i번 째 집은 j번째 집과 거리 j-i 만큼 떨어져있음. 
    1 <= i <= j <= n

((각 집마다 배달, 수거 개수))
deliveries = 배달
pickups = 수거

((이동 방식))
물류창고 출발 -> 각 집에 배달 -> 빈 상자 수거해서 다시 물류창고 도착
각 집마다 배달할 상자 개수, 수거할 빈 상자 개수 주어짐. 
각 집에 배달 및 수거할 때, 원하는 개수 만큼 배달 및 수거 가능. 
"트럭 하나로 모든 배달과 수거를 마치고 물류창고까지 돌아올 수 있는 최소 이동거리."
= 최소 이동거리 return


4
5
1 0 3 1 2
0 3 0 4 0
이 경우에는 return 16 반환

로직 구현
1. 배달, 수거 하는 집보다 멀리있는데, 일없는 집은 갈 필요 없음.
    즉, 현재 남은 작업이 있는 집 중에서 가장 먼 곳 까지만 움직이면 됨.
2. 먼 집을 나중에 갈 필요 없음. 지금 갈 수 있을때 가는게 최적임.
3. 한 번 갈 때 cap만큼 처리하기. 
=> 그리디.
=> 물류창고 -> 먼 집 -> 돌아오기(왕복)

1. 가야하는 곳 중 제일 멀리있는 집 찿기
- 인덱스 뒤에서부터 확인.
- 0이면 왼쪽으로 땡김. -1
=> 배달/수거 해야하는 가장 멀리있는 집을 찾기 위해서 뒤에서 부터 줄여감. 

2. 매번 출발할 때 배달/수거 중 가장 멀리 가야하는 집을 결정.

3. 용량 남아있고, 배달/수거 해야할 집이 남아있을 때
   용량에서 배달/수거 개수만큼 빼고
   해당 집은 배달/수거 했으니까 0으로 바꿈. 

4. else 남은 용량보다 배달/수거 개수가 더 많으면?  
    남은 용량만큼만 배달하고 종료
    나머지는 다음 출발때 다시 처리.
   
    수거를 남은 용량만큼 했으면? => 트럭 용량이 꽉 찼다는 뜻.    
    remain 수거 후 남은 용량을 = 0 으로 직접 바꿔야함. => 트럭 꽉 차서 수거 더 못한다는 뜻.
    다음 반복이 실행되면 안되기 때문. 
    안해주면 while문 반복 조건 때문에 remain > 0 이므로 한 번 더 돌게됨.

    
"""
def solution(cap, n, deliveries, pickups):
    answer = 0      # 총 이동거리
    d_idx = n - 1   # 배달 가장 끝 집 인덱스
    p_idx = n - 1   # 수거 가장 끝 집 인덱스

    # 뒤에서부터 배달/수거 마지막 지점을 찾으며 진행.
    # 배달/수거 하나라도 있으면 계속 반복.
    while d_idx >= 0 or p_idx >= 0:

        # 배달/수거 인덱스가 범위안이고 배달/수거 할 게 없으면 건너뛰고 
        # 할 일이 0인 집은 볼 필요 없으니까 줄여줌. 왼쪽 집으로 감.
        # 배달 마지막 위치
        while d_idx >= 0 and deliveries[d_idx] == 0:
            d_idx -= 1
        # 수거 마지막 위치
        while p_idx >= 0 and pickups[p_idx] == 0:
            p_idx -= 1


        # 배달/수거 중에 제일 멀리 가야 하는 곳을 선택.
        farthest = max(d_idx, p_idx)  # 배달/수거 중 더 멀리있는 집으로.
        # 둘 다 -1이면 = 할 일 없음. 
        if farthest < 0:  
            break

        # 이동한 거리 누적
        # 0 부터 시작이니까 far + 1 해주고 왕복이니까 *2
        answer += (farthest + 1) * 2


        # 배달 처리
        remain = cap # 배달/수거한 후 남은 용량 = cap - 배달하면서 용량 감소
        while d_idx >= 0 and remain > 0: # 배달할 집이 남아있고 아직 배달용량이 있으면 반복.
            if deliveries[d_idx] <= remain:  # 만약 배달 개수가 트럭 남은 용량보다 적거나 같으면 =  배달 가능.
                remain -= deliveries[d_idx]  # 용량을 해당 집 배달량 만큼 빼고
                deliveries[d_idx] = 0        # 그 집 배달을 0으로 바꿈.
                d_idx -= 1                   # 다음 집으로 이동
            else:  # 배달해야하는 개수가 남은 용량보다 많으면 
                deliveries[d_idx] -= remain  # 남은것만 배달하고 끝
                remain = 0                   # 트럭 꽉 찼으니까 배달 종료함.

        # 수거 처리
        remain = cap # 배달/수거한 후 남은 용량 = cap - 수거하면서 용량 감소
        while p_idx >= 0 and remain > 0:    # 수거 용량 있으면 반복
            if pickups[p_idx] <= remain:    # 만약 수거량이 남은 용량보다 적거나 같으면 = 수거 가능
                remain -= pickups[p_idx]    # 용량을 수거량 만큼 빼고
                pickups[p_idx] = 0          # 그 집 수거량을 0으로 바꿈
                p_idx -= 1                  # 그리고 왼쪽 집으로 이동.
            else:   # 수거 개수가 남은 용량보다 많으면
                pickups[p_idx] -= remain    # 남은 것만 수거하고 끝
                remain = 0                  # 용량 다 찼으므로 0으로 바꾸고 배달 종료

    return answer




cap = int(input())
n = int(input())
deliveries = list(map(int, input().split()))
pickups = list(map(int, input().split()))

result = solution(cap, n, deliveries, pickups)
print(result)