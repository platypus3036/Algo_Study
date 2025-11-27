import sys
sys.stdin = open('input.txt')

"""
N개의 자연수 주어짐
M개를 골라서 만들 수 있는 모든 수열을 출력
- 순열
- 같은 수열 중복 금지 (방문 체크)
- 오름차순으로 출력

예시)
N = 3, M =  2
숫자 = 4 5 2

1. 숫자를 정렬.
    2 4 5
2. 이 중 2개로 만들수 있는 순열 나열
    2 4 
    2 5 
    4 2 
    4 5
    5 2
    5 4
    => 2 4, 4 2 는 다름!
       조합이 아니라 순열 문제라서.
    
       
로직 
1. 숫자를 정렬
2. 숫자를 고름. (선택)
2-1. 그 숫자로 시작되는 모든 경우를 만듦. (재귀)
3. 모든 경우 만들어서 더 만들수 없으면,
   다른 숫자를 고름.  -> 1단계로 되돌아감. (선택 취소)
4. 중복 방지 -> 방문 체크 필요.

=> dfs - 백트래킹
모든 경우를 다 봐야함.
선택 과정이 단계별로 진행됨.
선택을 취소. 되돌려야 함. 
중복 없이 만들어야 함. 


"""

def backtrack():
    # 종료 조건 = 수열의 길이가 M개 다 채워졌는지 확인.
    if len(result) == M:
        print(*result)  # 출력해도 전체 탐색은 끝나지 않음.
        return
    
    for i in range(N):
        if not visited[i]: # 아직 이 숫자를 사용하지 않았다면. = 선택 안됨. false
            result.append(nums[i])  # 그 숫자를 현재 수열에 추가.
            visited[i] = True  # 선택했으니까, true로 바꿈.
            
            backtrack() # 재귀호출 
            result.pop() # 최근 넣은 숫자를 뺌. 2, 4 -> 2
            visited[i] = False # 다시 뺐으니 4를 사용할 수 있게 false로 바꿈.


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
visited = [False] * N 
result = []

backtrack()