# 직사각형을 만드는 데 필요한 4개의 점 중 3개의 좌표가 주어질 때, 나머지 한 점의 좌표를 구하려고 합니다.
# 점 3개의 좌표가 들어있는 배열 v가 매개변수로 주어질 때, 직사각형을 만드는 데 필요한 나머지 한 점의 좌표를 return 하도록 solution 함수를 완성해주세요.
# 단, 직사각형의 각 변은 x축, y축에 평행하며, 반드시 직사각형을 만들 수 있는 경우만 입력으로 주어집니다.
#
# 제한사항
# v는 세 점의 좌표가 들어있는 2차원 배열입니다.
# v의 각 원소는 점의 좌표를 나타내며, 좌표는 [x축 좌표, y축 좌표] 순으로 주어집니다.
# 좌표값은 1 이상 10억 이하의 자연수입니다.
# 직사각형을 만드는 데 필요한 나머지 한 점의 좌표를 [x축 좌표, y축 좌표] 순으로 담아 return 해주세요.

import collections


def solution(v):
    x = [i[0] for i in v]
    y = [i[1] for i in v]
    x_count = collections.Counter(x)
    y_count = collections.Counter(y)

    x_re = [i for i in x_count if x_count[i] == 1]
    y_re = [i for i in y_count if y_count[i] == 1]

    answer = x_re + y_re

    return answer


# XOR 이용
def solution(v):
    x = [i[0] for i in v]
    y = [i[1] for i in v]

    for i in range(2):
        x[0] ^= x[i + 1]
        y[0] ^= y[i + 1]
    answer = [x[0], y[0]]

    return answer