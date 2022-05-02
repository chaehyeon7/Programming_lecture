# 한글 단어를 찾으려면 어떻게 할까요?

# 한글의 첫 번째 글자는 가이고 마지막 글자는 힣입니다. 따라서 한글은 [가-힣]으로 찾을 수 있습니다.1

# *** 단, 이 방식으로는 ㄱㄴㄷ이나 ㅏㅑㅓㅕ같은 낱글자는 찾을 수 없습니다.

regex = r'[가-힣]+'

search_target = '''Luke Skywarker 02-123-4567 luke@daum.net
다스베이더 070-9999-9999 darth_vader@gmail.com
princess leia 010 2454 3457 leia@gmail.com'''

# 정규표현식과 일치하는 부분을 모두 찾아주는 파이썬 코드입니다.
import re
result = re.findall(regex, search_target)
print("\n".join(result))