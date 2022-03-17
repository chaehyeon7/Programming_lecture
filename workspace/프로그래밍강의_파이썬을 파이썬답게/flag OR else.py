# 설명
#
# 수를 곱해나가면 2, 8, 16, 80, 80 이 나옵니다. 16은 4를 제곱해 나온 수이므로 이 수는 제곱수입니다. 따라서 found를 출력합니다.
#
# 예시 2
# 입력
#
# 5
# 1
# 2
# 3
# 1
# 출력
#
# not found

import math

if __name__ == '__main__':
    numbers = [int(input()) for _ in range(5)]
    multiplied = 1
    for number in numbers:
        multiplied *= number
        if math.sqrt(multiplied) == int(math.sqrt(multiplied)):
            print('found')
            break
    else:
        print('not found')