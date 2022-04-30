# 소문자 알파벳만 고르고 싶을 때
# [abcdefghijklmnopqrlstuvwxyz]처럼 대괄호 안에 소문자를 모두 나열할 수도 있습니다.
#
# 우리는 간단히 [a-z]를 쓰도록 합시다. [a-z]는 "a부터 z까지 글자를 모두 선택하라"는 의미입니다.

regex = r'[a-z]'

search_target = '''Luke Skywarker 02-123-4567 luke@daum.net
다스베이더 070-9999-9999 darth_vader@gmail.com
princess leia 010 2454 3457 leia@gmail.com'''

# 정규표현식과 일치하는 부분을 모두 찾아주는 파이썬 코드입니다.
import re
result = re.findall(regex, search_target)
print("\n".join(result))