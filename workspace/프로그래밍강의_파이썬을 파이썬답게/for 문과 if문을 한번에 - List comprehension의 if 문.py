mylist = [3, 2, 6, 7]
answer = []
for number in mylist:
    if number % 2 == 0:
        answer.append(number**2) # 들여쓰기를 두 번 함

# 파이썬의 list comprehension을 사용하면 한 줄 안에 for 문과 if 문을 한 번에 처리할 수 있다.

mylist = [3, 2, 6, 7]
answer = [number**2 for number in mylist if number % 2 == 0]