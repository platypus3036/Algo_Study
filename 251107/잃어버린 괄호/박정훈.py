'''
1. 문제 분석
양수, +, -로 이루어진 식에 괄호를 적절히 쳐서 값이 최소가 되도록 도출

2. 풀이 방법 고안
가능한 만큼 +를 -으로 바꾸면 해결됨
맨 첫번째 수는 그대로
뒤에 '-'가 올 때 까지 그대로 계산
뒤에 -가 오면, 뒤에 오는 모든 '+'를 '-'로 변환
'''
expression = input()

new_exp = []    # 최소값을 만드는 새 식
num = ''      # 여러자리의 숫자를 저장
is_minus = False

for i in expression:
    if i not in ['+', '-']:
        if num is False:
            if i == '0':
                continue
            else:
                num += i
        else:
            num += i

    else:
        new_exp.append(num)
        num = ''
        if i == '-':
            new_exp.append(i)
            is_minus = True
        else:
            if is_minus:
                new_exp.append('-')
            else:
                new_exp.append('+')

new_exp.append(num)

result = 0
for i in range(len(new_exp)):
    if i == 0:
        result += int(new_exp[i])

    if new_exp[i] == '+':
        result += int(new_exp[i+1])

    elif new_exp[i] == '-':
        result -= int(new_exp[i+1])

print(result)