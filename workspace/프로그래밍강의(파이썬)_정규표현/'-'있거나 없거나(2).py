# 앞에서 배운 \d+-?\d+-?\d+ 정규표현식은 한계가 있습니다.
# "010 2454 3457"과 같이 공백이 포함된 전화번호를 찾을 수 없지요.
#
# 021234567
# 02-123-4567
# 010 2454 3457
# 모든 전화번호를 찾으려면
#
# "-가 있거나 없다"는 조건이 아니라
# "- 또는 공백이 있거나 없다"는 조건을 써야 합니다.
# - 또는 (공백)이 있거나 없다는 조건은 [- ]?로 표현할 수 있습니다.

regex = r'\d+[- ]?\d+[- ]?\d+'

search_target = '''Luke Skywarker 02-123-4567 luke@daum.net
다스베이더 070-9999-9999 darth_vader@gmail.com
princess leia 010 2454 3457 leia@gmail.com'''

#아래 부분은 본 강의에서 다루지 않습니다.
import re
result=re.findall(regex,search_target)
print(result)