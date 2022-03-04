# 문제 설명
# 문자열 s와 자연수 n이 입력으로 주어집니다. 문자열 s를 좌측 / 가운데 / 우측 정렬한 길이 n인 문자열을 한 줄씩 프린트해보세요.

s, n = input().strip().split(' ')
print(s.ljust(int(n)))
print(s.center(int(n)))
print(s.rjust(int(n)))