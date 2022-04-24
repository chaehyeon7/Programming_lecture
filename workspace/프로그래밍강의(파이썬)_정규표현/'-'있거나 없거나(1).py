# 전화번호는 "-"을 포함하거나, 포함하지 않을 수 있습니다. 예를 들어, 다음은 모두 유효한 전화번호입니다.
#
# 021234567
# 02-123-4567

# 따라서 전화번호는 연속되는 숫자 3 ~ 4개 사이에 -가 있거나 없다고 표현할 수 있습니다.

# ?는 '있거나 없거나'라는 뜻입니다. 따라서 -?는 "-가 있거나 없다"를 의미합니다.
# 따라서 이를 연속하는 숫자는 \d+와 조합하면 전화번호를 찾는 정규표현식을 만들 수 있습니다.

regex = r'\d+-?\d+-?\d+'

search_target = '''Luke Skywarker 02-123-4567 luke@daum.net
다스베이더 070-9999-9999 darth_vader@gmail.com
princess leia 010 2454 3457 leia@gmail.com'''

#아래 부분은 본 강의에서 다루지 않습니다.
import re
result=re.findall(regex,search_target)
print(result)