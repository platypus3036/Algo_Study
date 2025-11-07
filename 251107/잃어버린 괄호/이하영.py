import sys
sys.stdin = open('input.txt')

"""
0~9 + -
() 괄호를 적절히 쳐서 이 식의 값을 최소로 만들기.


연속해서 두 개 이상의 연산자가 나오지는 않음.
5자리보다 많이 연속되는 숫자는 없음.
식의 길이는 50보다 작거나 같음. 

55-50+40
최소값 만드는 방법
+ 양 옆 숫자를 괄호로 묶기.
- 를 만나면 -를 없애고 두 덩어리로 나누기. => 문자열로 받기!
"55", "50 + 40" 

계산만 하면 되는듯. 괄호를 직접 넣을 필요 없어보임. 

예시
10-20+30-40+50
1. -를 기준으로 나눔
    "10", "20+30", "40+50" 

2. 첫번째 덩어리
    10을 더해줌

3. 두번째 부터 이후 덩어리들 계산해서 
   첫번째 10에다가 다 빼줌.
   10 - 50 - 90

"""

def min_val(math):

    # '-' 기준으로 문자열을 덩어리로 나눔.
    divide = math.split('-')

    # 첫번째 덩어리
    # 문자열이라서 int로 바꾸고, + 기준으로 나눈 다음에, 숫자를 더해주기 sum.
    first_dung = sum(map(int, divide[0].split('+')))

    # 첫번째 뒤로 나머지 덩어리 rest
    # 각각 '+' 기준으로 더해주고
    # 첫번째 덩어리에서 나머지 덩어리를 전부 빼줌
    rest_dung = 0
    for dung in divide[1:]:
        rest_dung += sum(map(int, dung.split('+')))

    return first_dung - rest_dung


math = input().strip()  # 문자열로 받기 = 덩어리로 나누기 위함.
result = min_val(math)
print(result)
