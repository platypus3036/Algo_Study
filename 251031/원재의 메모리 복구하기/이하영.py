import sys
sys.stdin = open('input.txt')

"""
메모리 비트 중 하나를 골라 0인지 1인지 결정.
해당 값이 메모리의 선택한 부분 부터, 끝까지 덮어 씌우는 것.

0100 -> 세번째 비트 1 선택  0111


초기화 된 0 상태에서 -> 원래 상태로 돌아가는데 걸리는 횟수 계산 / 0011, 100
0000 -> 세번째 비트 1 선택  0011                            : 1번
0000 -> 두번째 비트 1 선택  0111 -> 세번째 비트 0 선택 0100   : 2번


1. 초기값 0을 원래값 크기만큼 맞춰서 시작
2. 0000과 원래 값 네 자리를 비교
    - 첫번째 자리, 두번째 자리, 세번째 자리, 네번째 자리 확인
    - 같으면 통과
    - 다르면 0또는 1로 넣어줌.
    - 원래값이 j라고 하면,
    - 0000의 i를 -> j로 치환.
    - 치환 할때 마다 count +1
    - 초기값과 원래값이 같으면 종료.

"""

def change_count(origin_numbers):
    count = 0
    start = [0] * len(origin_numbers)


    for i in range(len(origin_numbers)):
        
        if start[i] != origin_numbers[i]:
            start[i:] = [origin_numbers[i]] * (len(start) - i)  # 다른 부분부터 끝까지 j로 치환
            count += 1  # 숫자 바꾸고 카운트
    return count


T = int(input())
for tc in range(1, T+1):
    origin_numbers = list(map(int, input()))
    result = change_count(origin_numbers)
    print(f"#{tc} {result}")


"""
1. 같을 때는 확인 안해도 됨.
2. 다를 때만 확인하고 치환하기.
3. 굳이 초기값과 원래값이 같아졌는지 확인할 필요 없음.
   같을 때는 안바꾸기 때문에. 

   
슬라이싱으로 치환할때 주의
    start[i:] = origin_numbers[j] => 타입에러 뜸
    origin_numbers[j]는 리스트가 아니라 하나의 값!
    start[i:] = 1 이렇게 대입이 불가능함. 
    하나의 값이 아니라 리스트, 튜플 처럼 반복 가능한 객체여야 함.

해결
길이를 유지한 채로 리스트 사용
start[i:] = origin_numbers[j] * (len(start) - i)
(len(start) - i) 이걸로 j를 슬라이싱 뒤쪽 길이만큼 반복 시킴. 

        start[i:] = [origin_numbers[j]] * (len(start) - i)
        1. len(start) = 4
        2. i = 2
        3. (len(start) - i) = 2
        4. origin_numbers[j] = 1
        5. [origin_numbers[j]] * 2 = [1, 1]
        6. start[2:] = [1, 1]
        start = [0, 0, 1, 1] 

   

start도 origin이랑 길이같으니까 어짜피 i번호는 같음.
for문 하나만 사용.
j는 다 i로 고침.
"""