# 문제 설명
# 입력으로 0이 주어지면 영문 소문자 알파벳을, 입력으로 1이 주어지면 영문 대문자 알파벳을 사전 순으로 출력하는 코드를 짜세요.
num = int(input().strip())
import string
if num is 0:
    print(string.ascii_lowercase)
if num is 1:
    print(string.ascii_uppercase)