import sys
sys.stdin = open('input.txt')

"""
N명 사람 / M초 시간 / K개 붕어빵 => 1 <= n, m, k <= 100
time N명의 사람이 도착하는  시간. 초 단위. 0~11,111

=> 붕어빵이 완성되면 시간 지연 없이 만들기 시작 가능.

도착 시간이 주어지면, 
모든 손님들에게 기다리는 시간 없이 붕어빵을 제공할 수 있는지 판별하는 프로그램 작성하기.
모든 손님이 기다리는 시간 없이 붕어빵 제공 가능하면 Possible
                                    불가능하면 Impossible

                                    
2명 손님, 2초 붕어빵 만드는 시간, 2개 붕어빵
3초에 도착, 4초에 도착
=> 0 ~ 2초 붕어빵 2개 만듦.
=> 3초 도착 손님 : (3//2)*2 = 2  만들어진 붕어빵 2 >= 손님수 1   : no wait
=> 4초 도착 손님 : (4//2)*2 = 4  만들어진 붕어빵 4 >= 손님수 2 (누적) : no wait
   모두 가능


2명 손님, 2초 붕어빵 만드는 시간, 2개 붕어빵
1초 도착, 2초에 도착
=> 0~ 2초 붕어빵 만듦.
=> 1초 도착 손님 wait X
=> 2초 도착 손님 = 1초 손님 못받았으니까 볼 필요 없음.



1. M초 후에 K개가 처음 완성됨.
2. 0초에는 아직 붕어빵 없음.
3. 처음오는 손님이(시간 정렬하기) 
4. 뒤에 손님은 손님수 누적해서 확인하기.
5. 첫번째에서 붕어빵 부족하면 바로 종료하면 됨.

"""
def no_waiting(N,M,K,times):
    times.sort()  # 시간 순 정렬

    # 손님 온 순서대로 확인
    for i in range(len(times)): # 첫번 째 시간, 두 번째 시간 뽑기
        t = times[i] # 첫번재 1초, 두번째 2초. / 실제 도착한 시간.
        make = (t // M) * K  # (2초 도착 // 붕어빵 만드는 시간 2초) * 2개 만듦 
                             # = t초 까지 만든 붕어빵 수. 

        if make < (i+1): # 사람 명수로 봐야하는데 인덱스 번호니까 +1 // i=0 일때 1명, i=1 일때 2명 누적
            return "Impossible"
    return "Possible"



T = int(input())
for tc in range(1, T+1):
    N, M, K = list(map(int, input().split())) # 2 2 2 
    times = list(map(int, input().split())) # [3, 4] 
    result = no_waiting(N,M,K,times)
    print(f"#{tc} {result}")

