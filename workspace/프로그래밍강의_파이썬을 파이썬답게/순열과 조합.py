# 문제 설명
# 숫자를 담은 일차원 리스트, mylist에 대해 mylist의 원소로 이루어진 모든 순열을 사전순으로 리턴하는 함수 solution을 완성해주세요.

# 예시
# mylist	output
# [2, 1]	[[1, 2], [2, 1]]
# [1, 2, 3]	[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
import itertools

def solution(mylist):
    print(list(map(''.join, itertools.permutations(mylist, 2))))