# 문자열 배열 ['1', '100', '33']을 정수 배열 [1, 100, 33]로 바꾸기
# 부동소숫점 튜플 (3.14, 3.5, 22.6)을 정수 배열 (3, 3, 22)로 바꾸기

list1 = ['1', '100', '33']
list2 = []
for value in list1:
    list2.append(int(value))

# 파이썬 map사용
list1 = ['1', '100', '33']
list2 = list(map(int, list1))