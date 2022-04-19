# 1. 전화번호를 찾기 위한 첫 단계는 숫자를 찾아내는 겁니다.
# 2. \d는 숫자를 대표하는 정규표현식입니다. 이때 d는 digit을 뜻합니다.
# Output으로 search_target에 들은 모든 숫자가 한 줄씩 나올 겁니다.

regex = r'\d'

search_target = '''Luke Skywarker 02-123-4567 luke@daum.net
다스베이더 070-9999-9999 darth_vader@gmail.com
princess leia 010 2454 3457 leia@gmail.com'''

# 정규표현식과 일치하는 부분을 모두 찾아주는 파이썬 코드입니다.
import re
result = re.findall(regex, search_target)
print("\n".join(result))