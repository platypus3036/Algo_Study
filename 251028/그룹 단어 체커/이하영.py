import sys
sys.stdin = open('input_1.txt')

"""
연속하는 문자 또는 글자 하나 = 그룹 단어
aaba = a가 떨어져 있으므로 != 그룹 단어

1. 처음부터 순서대로 단어를 쪼개서 확인
   나온 문자를 기억해야함. -> 저장해두기

2. 저장 방법 : list
3. 규칙 : 저장된 단어가 끊겼다가 다시 나오면 X
        끊기지 않고 연결되서 나오거나, 하나일 경우 O
        카운트


"""

def group_words_count(words):
    count = 0

    for word in words: # 단어들 묶음 
        seen = set() # 나왔던 모든 문자 저장
        front = ''    # 바로 앞에 문자 하나만 저장
        group = True


        for w in word: # 단어들을 하나씩 빼보기.
            if w != front: # 이전 문자랑 지금 문자랑 다를 때.

                if w in seen: # 이전에 나왔던 적이 있다면
                    group = False
                    break # 반복 중지 = 이미 그룹 아니므로.
                else:
                    seen.add(front)  # 나왔던 모든 문자에 저장하고
                    front = w        # 현재 문자를 바로 앞에 문자로 갱신
        if group:
            count +=1
    return count



N = int(input())
words = [input().strip() for _ in range(N)]
result = group_words_count(words)
print(result)