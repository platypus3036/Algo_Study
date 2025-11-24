"""
A를 재배치
S = A[0] * B[0] + ... + A[N-1] * B[N-1]
단, B에 있는 수는 재배열하면 안 됨.

S 최소값 구하기. 
=> S 최소값만 구하면 되는거면 왜 B 재배열 하면 안됨?


로직 순서
1. 정렬
A 최소값 = 오름차순
B 최대값 = 내림차순 정렬

2. N 인덱스 꺼내서 A[i] * B[i] 해주고 
3. S에 다 더해주기

"""
def S_min(N, A, B):
        
    A.sort()
    B.sort(reverse=True)  # 애초에 이게 최소값. 따로 min 찾을 필요 없음.

    S_sum = 0
    for i in range(N):
        S_sum += A[i] * B[i]

    return S_sum


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
result = S_min(N, A, B)
print(result)

###############


