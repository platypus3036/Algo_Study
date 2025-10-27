'''
1. 문제 분석
단어의 문자 중, 같은 문자들이 모두 연속하는 단어의 개수를 세는 문제

2. 풀이 방법 고안
visited를 사용하면 될것같음
visited에 알파벳을 넣고, visited에 있는 단어이면서 바로전의 단어와 다른 단어라면 그룸단어가 x
'''
N = int(input())
cnt = 0
for i in range(N):
    check = True
    visited = [False] * 26
    word = input()
    for j in range(len(word)):
        if j == 0:
            visited[ord(word[j]) - ord('a')] = True
        else:
            if visited[ord(word[j]) - ord('a')] and word[j] != word[j-1]:
                check = False
                break
            else:
                visited[ord(word[j]) - ord('a')] = True
    if check:
        cnt += 1

print(cnt)