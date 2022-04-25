# \d+[- ]?\d+[- ]?\d+ 정규표현식으로는 전화번호를 찾는데 한계가 있습니다.
# "0030589-5-95826"과 같이 연결된 숫자가 너무 많은 문자열도 전화번호라고 인식합니다.


regex = r'\d+[- ]?\d+[- ]?\d+'

search_target = '''이상한 전화번호 0030589-5-95826
Luke Skywarker 02-123-4567 luke@daum.net
다스베이더 070-9999-9999 darth_vader@gmail.com
princess leia 010 2454 3457 leia@gmail.com'''

import re
result=re.findall(regex,search_target)
print(result)