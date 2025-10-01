import sys
sys.stdin = open('input.txt')

"""
첫 번째 : 100
두 번째 : 0~ 100 사이 아무 숫자
세 번째 : 첫 번째 - 두 번째
네 번째 : 두 번째 - 세 번째


        i 앞의 앞 숫자 - i 앞 숫자
  a[i] = a[i - 2] - a[i - 1]

음수가 나오면 정지. 음수도 반환 안함.



이 규칙으로 구할 수 있는 최대 개수 구하기.
= 가장 긴 수열

출력 시 
1. 최대 개수
2. 그 수열 한 칸씩 띄워서.


풀이 
1. 몇 개 출력될지 몰라 = while
2. 규칙 (두번째거 이후부터)
   다음 숫자 = 앞앞 - 앞
3. 음수는 종료 if num < 0:
4. 두번째 숫자는 0~100 완탐.. 

"""


N = int(input()) # 시작

longest_count = 0    # 가장 긴 숫자(수열) 개수
longest_seq = []     # 가장 긴 숫자들(수열) 저장

# 두 번째 수 0 ~ 100까지 탐색.
for second in range(N + 1):
    sequence = [N, second]  # [첫번째, 두번째] => i = 0, 1
    
    
    i = 2  # 세번째 수 부터 계산하기 위함.
    while True: 
        next_num = sequence[i-2] - sequence[i-1]
        # 규칙 : 다음 숫자 = 앞앞 - 앞  =>  a[i] = a[i-2] - a[i-1]

        # 종료 조건 = 음수
        if next_num < 0:
            break

        # 음수 안걸릴 때, 수열 저장하기.
        sequence.append(next_num)
        i += 1  # 다음 인덱스로 이동
    
   
    if len(sequence) > longest_count:
        longest_count = len(sequence) # 갱신
        longest_seq = sequence[:]     # 숫자들 다 저장


print(longest_count) # 개수
print(*longest_seq)  # 숫자들

# 메모리 초과..
"""
마지막에 갱신 후 저장하는 부분
longest_seq = sequence 이렇게 하니까 메모리 초과 뜸.

why?
longest가 seq 리스트를 참조하게 됨.
반복 끝날 때 까지 계속 남아있게 돼서,
반복 할 때 마다 더 큰 리스트들이 메모리에 쌓임.

해결 : 복사해서 저장.
longest_seq = sequence[:]
슬라이싱 복사 
longest_seq = list(sequence)
새 리스트로 복사

따로 독립적으로 저장해서 메모리 관리.

"""