# 문제 설명
# 다음을 만족하는 함수, solution을 완성해주세요.
#
# 예를 들어 mylist [[1, 2, 3], [4, 5, 6], [7, 8, 9]]가 주어진 경우, solution 함수는
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]] 을 리턴하면 됩니다.
def solution(mylist):
    answer = list(map(list, zip(*mylist)))
    return answer