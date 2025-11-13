import sys
sys.stdin = open('input2.txt')

"""
N 자연수 
M 길이

3 1
= 123 까지 자연수
= 1개씩 출력
1
2
3

4 2
= 1234 까지 자연수
= 2개씩 출력
11
12
13
14
22 
23
24
33
34
44

-> 중복되는 숫자 세트는 출력 안해도 됨.


조합 생성 문제. 
1. 그냥 반복으로 할지 = (1 ≤ M ≤ N ≤ 8) 작아서 가능은 할 듯. but, 길이가 너무 길어질 듯. 
2. 재귀로 할지 

길이 M만큼 출력 len(M)
"""

N, M = map(int, input().split())
result = []

def dfs(start, end):
    if len(end) == M:
        result.append(end)
        return
    
    # start 1 반복 끝나면 2 -> N이 start 2부터 시작하기 때문에 2보다 작은 숫자로 시작하지 않게됨. 
    # 중복 처리 안해도 2,1, 3,1, 3,2 등이 안생김.
    for i in range(start, N+1): # i = 1~4 까지 반복 
        dfs(i, end +[i]) # i를 start로 넘겨서 고정. // end + i가 아니라 end +[i] 
                         # 리스트 end + 리스트 [i] 라서 숫자값을 더하는게 아니라 list끼리 결합한 것. 

dfs(1, []) 
for rst in result:
    print(*rst)  # 잊지말고 리스트 언팩 해주기.

##############################################

N, M = map(int, input().split())

for a in range(1, N + 1):
    if M == 1:
        print(a)
        continue
    for b in range(a, N + 1): # start를 a로
        if M == 2:
            print(a, b)
            continue
        for c in range(b, N + 1):
            if M == 3:
                print(a, b, c)
                continue
            for d in range(c, N + 1):
                if M == 4:
                    print(a, b, c, d)
                    continue
                for e in range(d, N + 1):
                    if M == 5:
                        print(a, b, c, d, e)
                        continue
                    for f in range(e, N + 1):
                        if M == 6:
                            print(a, b, c, d, e, f)
                            continue
                        for g in range(f, N + 1):
                            if M == 7:
                                print(a, b, c, d, e, f, g)
                                continue
                            for h in range(g, N + 1):
                                if M == 8:
                                    print(a, b, c, d, e, f, g, h)
                                    continue
