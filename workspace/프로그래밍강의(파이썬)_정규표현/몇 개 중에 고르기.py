# 알파벳 중에 소문자 모음(a,e,i,o,u)만 고르고 싶을 땐 어떻게 할까요?
#
# 그럴 때는 [aeiou]라고 적어주세요. 정규표현식에서 대괄호[ ] 안에 글자를 넣으면 해당 글자를 모두 선택할 수 있습니다.

regex = r'[aeiou]'

search_target = '''Luke Skywarker 02-123-4567 luke@daum.net
다스베이더 070-9999-9999 darth_vader@gmail.com
princess leia 010 2454 3457 leia@gmail.com'''

# 정규표현식과 일치하는 부분을 모두 찾아주는 파이썬 코드입니다.
import re
result = re.findall(regex, search_target)
print("\n".join(result))