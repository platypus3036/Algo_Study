import sys
sys.stdin = open('input.txt')

"""
N의 배수를 계속 세는데, 
각 자리수를 떼서 0123456789 모든 숫자를 보는 시점에 종료

1. N을 배수로 계속 출력
2. for문으로 배수 숫자를 쪼갬
3. 쪼갠 숫자를 set에 넣어서 중복 방지하고
   모든 숫자가 다 있는지 확인함.
   다 있으면 반복 종료
4. 모든 숫자가 있을 때의 배수값을 출력. (몇 번째인지 출력하는것 아님.)

예시)
N = 2       2
2N = 4      2, 4
3N = 6      2, 4, 6
4N = 8      2, 4, 6, 8
5N = 10     0, 1, 2, 4, 6, 8
.
.
.
25N = 50    0, 1, 2, 4, 5, 6, 8
35N = 70    0, 1, 2, 4, 5, 6, 7, 8
45N = 90    0, 1, 2, 4, 5, 6, 7, 8, 9


"""

def all_nums(numbers):

    save = set()
    k = 1

    while True:
        multi = numbers * k
        
        for piece in str(multi):
            save.add(piece)
            
        if len(save) == 10:
            return multi
        k += 1


T = int(input())
for tc in range(1, T+1):
    numbers = int(input().strip())
    result = all_nums(numbers)
    print(f"#{tc} {result}")


"""
원래 숫자들을 다 저장해둔 리스트랑 비교하는 방식으로 했는데
어짜피 set은 중복 방지 처리가 되며,
0~9가 다 들어가면 10개가 세어지므로
set에 있는게 == 숫자 리스트랑 같은지 비교할 필요가 없음
그래서 지우고 set에 저장된 save가 10개가 맞는지 확인해서 배수값을 출력.

"""