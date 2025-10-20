'''
1. 문제 분석
str형태의 문자열을 조작하는 여러 방법들을 테스트하는 문제
재할당을 언제 해주어야 하는지(2단계, 3단계)

2. 풀이 방법 구상
단계별로 함수를 이용해 구현
처음에는 2단계와 3단계에서 +=을 이용해 문자열을 재할당함
for in 반복문을 돌면서 그만큼 재할당을 반복해서, 시간복잡도가 올라갈거라 판단

수정 후에는 빈 리스트에 append를 하고, .join()을 이용해 문자열의 형태로 풀어주었음

3. 시간 복잡도
문자열은 불변의 특징을 가짐
+=할때마다, 새로운 문자열을 만들기 때문에, 시간복잡도 O(n**2)
append를 이용해서 마지막에 문자열의 형태로 만드는 방식은 시간복잡도가 O(n)
'''

def solution(new_id):
    new_id = new_id.lower()     # 1단계
    
    new_id_2_lst = []     # 수정 후 2단계
    for spell in new_id:
        if spell.islower() or spell.isdigit() or spell in '-_.':
            new_id_2_lst.append(spell)
    new_id_2 = "".join(new_id_2_lst)

    new_id_3_lst = []    # 수정 후 3단계
    for i in new_id_2:
        if i == '.':
            if not new_id_3_lst or new_id_3_lst[-1] != '.':
                new_id_3_lst.append(i)
        else:
            new_id_3_lst.append('.')
    new_id_3 = "".join(new_id_3_lst)
    
    '''
    new_id_2 = ''     # 2단계
    for spell in new_id:
        if spell.islower() or spell.isdigit() or spell in '-_.':
            new_id_2 += spell

    new_id_3 = ''      # 3단계
    for i in new_id_2:
        if i == '.':
            if not new_id_3 or new_id_3[-1] != '.':
                new_id_3 += '.'
        else:
            new_id_3 += i
    '''

    new_id_3 = new_id_3.strip(".")      # 4단계

    if not new_id_3:     # 5단계
        new_id_3 = 'a'

    if len(new_id_3) >= 16:     # 6단계
        new_id_3 = new_id_3[:15]
    new_id_3 = new_id_3.rstrip(".")

    while len(new_id_3) <= 2:     # 7단계
        new_id_3 += new_id_3[-1]

    return new_id_3
