'''
1. 문제 분석
N이 1 커지면, 바로 전의 모양을 정사각형으로 둘러싸는 모양이 찍힌다.

2. 풀이 방법 고안
바깥에 둘러지는 정사각형의 한 변의 크기는 4 * (N-1) + 1
첫줄과 마지막줄은 별을 전부 찍고,
두번째줄과 뒤에서 두번째 줄은 별 + 빈칸 + 별
중간의 줄들은 별 + 빈칸 + 기존 모양 + 빈칸 + 별

재귀로 만들면 시간복잡도가 너무 커질것이라고 생각
(문자열들이 있는 list를 만들고, N이 하나 커질때마다 새로운 문자열들을 만들어서 넣어줘야 함)

직접 규칙에 따라 만들어보자
for i in range(length)에서 i가 짝수일때, 홀수일때 분리
'''
N = int(input())
length = 4 * (N - 1) + 1
arr = ["" for _ in range(length)]
standard = "* " * ((length - 1) // 2) + '*'

for i in range(length):
    gap = abs(length // 2 - i)
    if i % 2 == 0:      # 짝수번째 줄일때
        arr[i] = standard[:length // 2 - gap] + '*'*((gap*2) + 1) + standard[length // 2 + gap + 1:]
    else:               # 홀수번째 줄일때
        arr[i] = standard[:length // 2 - gap] + ' ' * ((gap * 2) + 1) + standard[length // 2 + gap + 1:]

for words in arr:
    print(words)