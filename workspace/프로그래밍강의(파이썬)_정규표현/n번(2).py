# {숫자}는 "숫자번 반복한다"는 뜻입니다. 예를 들어 \d{2}는 "숫자가 연속 두 번 나온다"는 뜻입니다.

regex = r'\d{2}[- ]?\d{3}[- ]?\d{4}'

search_target = '''이상한 전화번호 0030589-5-95826
Luke Skywarker 02-123-4567 luke@daum.net
다스베이더 070-9999-9999 darth_vader@gmail.com
princess leia 010 2454 3457 leia@gmail.com'''

#아래 부분은 본 강의에서 다루지 않습니다.
import re
result=re.findall(regex,search_target)
print(result)