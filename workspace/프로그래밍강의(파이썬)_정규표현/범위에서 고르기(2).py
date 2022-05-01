# 연속된 영어 소문자를 찾으려면 어떻게 할까요?
#
# 소문자를 뜻하는 [a-z]와
# 반복을 뜻하는 +를 붙여 => [a-z]+를 씁니다.

regex = r'[a-z]+'

search_target = '''Luke Skywarker 02-123-4567 luke@daum.net
다스베이더 070-9999-9999 darth_vader@gmail.com
princess leia 010 2454 3457 leia@gmail.com'''

# 정규표현식과 일치하는 부분을 모두 찾아주는 파이썬 코드입니다.
import re
result = re.findall(regex, search_target)
print("\n".join(result))