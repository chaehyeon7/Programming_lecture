# 앞서 배운 \d{2}[- ]?\d{3}[- ]?\d{4} 정규표현식으로는 전화번호를 찾는데 한계가 있습니다.
# 전화번호의 첫 부분에 숫자가 3번(010 2454 3457) 나오는 경우를 인식하지 못하지요.

# 021234567
# 02-123-4567
# 010 2454 3457

# {숫자1, 숫자2}는 "숫자1부터 숫자2까지 반복한다"는 뜻입니다. 예를 들어, \w{2,3}는 "문자가 2 ~ 3번 나온다"는 뜻입니다.
#
# 전화번호의 자릿수는 다음과 같습니다. 따라서 전화번호는 \d{2,3}[- ]?\d{3,4}[- ]?\d{4}와 같이 표현할 수 있습니다.
#
# 자리 수
# 처음	2 ~ 3자리
# 가운데	3 ~ 4자리
# 마지막	4자리

regex = r'{}'

search_target = '''이상한 전화번호 0030589-5-95826
Luke Skywarker 02-123-4567 luke@daum.net
다스베이더 070-9999-9999 darth_vader@gmail.com
princess leia 010 2454 3457 leia@gmail.com'''

#아래 부분은 본 강의에서 다루지 않습니다.
import re
result=re.findall(regex,search_target)
print(result)