# 예시) a = 3, b = 'abc'를 a = 'abc', b = 3 으로 바꾸기
#  일반적인 방법
# a = 3
# b = 'abc'
#
# temp = a
# a = b
# b = temp


#  파이썬 문법
a = 3
b = 'abc'

a, b = b, a
print(a)
print(b)