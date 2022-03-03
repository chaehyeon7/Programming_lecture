# 문제 설명
# base 진법으로 표기된 숫자를 10진법 숫자 출력해보세요.


num, base = map(int, input().strip().split(' '))

answer = int(str(num), int(base))
print(answer)