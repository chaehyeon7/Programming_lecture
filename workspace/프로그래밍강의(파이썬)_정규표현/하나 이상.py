# \d는 숫자를 한글자만 찾습니다. 하지만 전화번호를 구성하는 043이나 2568같이 연결된 숫자를 찾고 싶을 때는 어떻게 해야 할까요?

# 그럴 땐 +를 이용하면 됩니다. +는 "하나 혹은 그 이상 연결된"이라는 뜻입니다.
# 따라서 \d+는 "하나 혹은 그 이상 연결된 숫자"를 의미합니다.

regex = r'\d+'
search_target = '''Luke Skywarker 02-123-4567 luke@daum.net
다스베이더 070-9999-9999 darth_vader@gmail.com
princess leia 010 2454 3457 leia@gmail.com'''

import re
result=re.findall(regex,search_target)
print(result)