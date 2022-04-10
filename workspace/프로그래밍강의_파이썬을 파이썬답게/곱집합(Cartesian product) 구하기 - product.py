# 다른언어 에서는 for 문을 이용해 두 iterable의 원소를 하나씩 곱해간다.

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'

for value1 in iterable1:
    for value2 in iterable2:
        for value3 in iterable3:
            print(value1, value2, value3)



# itertools.product를 이용하면, for 문을 사용하지 않고도 곱집합을 구할 수 있다.

import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'
print(list(itertools.product(iterable1, iterable2, iterable3)))