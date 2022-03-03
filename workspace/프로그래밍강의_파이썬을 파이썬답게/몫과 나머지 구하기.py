# 문제 설명
# 숫자 a, b가 주어졌을 때 a를 b로 나눈 몫과 a를 b로 나눈 나머지를 공백으로 구분해 출력해보세요.

a, b = map(int, input().strip().split(' '))
print(*divmod(a,b))