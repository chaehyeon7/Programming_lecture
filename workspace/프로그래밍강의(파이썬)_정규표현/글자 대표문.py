# \w는 글자를 대표하는 정규표현식입니다.
# a, b, c, 가, 나, 다, 1, 2와 같은 문자와 숫자를 포함합니다.
# 특수문자는 포함하지 않지만, _(언더스코어)는 포함합니다.
# \w입력한다면 모든 문자와 숫자가 한 줄씩 나올 겁니다.

regex = r'\w'

search_target = '''Luke Skywarker 02-123-4567 luke@daum.net
다스베이더 070-9999-9999 darth_vader@gmail.com
princess leia 010 2454 3457 leia@gmail.com'''

# 정규표현식과 일치하는 부분을 모두 찾아주는 파이썬 코드입니다.
import re
result = re.findall(regex, search_target)
print("\n".join(result))