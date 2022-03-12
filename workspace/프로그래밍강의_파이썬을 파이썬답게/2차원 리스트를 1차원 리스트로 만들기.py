# 문제 설명
# 문자열을 담은 이차원 리스트, mylist 가 solution 함수의 파라미터로 주어집니다.
# solution 함수가 mylist를 일차원 리스트로 만들어 리턴하도록 코드를 작성해주세요.

# 예시
# input	output
# [[1], [2]]	[1, 2]
# [['A', 'B'], ['X', 'Y'], ['1']]	['A', 'B', 'X' ,'Y', '1']


import itertools
def solution(mylist):
    answer =list(''.join(list(map(''.join,mylist))))
    return answer