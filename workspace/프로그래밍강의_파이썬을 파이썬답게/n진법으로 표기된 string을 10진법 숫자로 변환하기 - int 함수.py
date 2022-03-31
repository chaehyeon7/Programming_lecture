num = '3212'
base = 5

answer = 0
for idx, number in enumerate(num[::-1]):
    answer += int(number) * (base ** idx)

# 파이썬의 int(x, base=10) 함수는 진법 변환을 지원합니다.

num = '3212'
base = 5
answer = int(num, base)