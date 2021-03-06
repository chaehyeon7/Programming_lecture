# 정규표현식으로 010, 123, 456 중 자연수를 찾으려면 어떻게 해야 할까요? 자연수는
#
# 0으로 시작하지 않으니 자연수의 첫자리는 반드시 1 ~ 9 중에 하나이어야 합니다.

# 그다음 자리부터는 0~9 사이의 숫자가 나올 수도 있고, 나오지 않을 수도 있지요.
# 다시 말해, 자연수는 다음과 같이 표현할 수 있습니다.
#
# 처음에 1~9중 하나의 숫자가 나온 다음
# 그 뒤에는 숫자가 0개 이상 나오면

# *은 "0개 이상"이라는 뜻입니다. 따라서 \d*는 "숫자가 0개 이상이다"를 의미합니다.
# 이를 이용하면 자연수는 [1-9]\d*로 표현할 수 있습니다.
regex = r'[1-9]\d*'

search_target = '''Luke Skywarker 02-123-4567 luke@daum.net
다스베이더 070-9999-9999 darth_vader@gmail.com
princess leia 010 2454 3457 leia@gmail.com'''

# 정규표현식과 일치하는 부분을 모두 찾아주는 파이썬 코드입니다.
import re
result = re.findall(regex, search_target)
print("\n".join(result))