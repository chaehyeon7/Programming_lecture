# 문자열 배열 ['1', '100', '33']을 이어 붙여 문자열 '110033' 만들기
# 정수형 튜플 (3, 22, 91)을 이어붙여 문자열 '32291' 만들기

my_list = ['1', '100', '33']
answer = ''
for value in my_list:
    answer += value


# 파이썬의 str.join(iterable)을 사용하면 이 코드를 두 줄로 줄일 수 있습니다 .

my_list = ['1', '100', '33']
answer = ''.join(my_list)