#  search_target변수에는 주소록이 있습니다.
regex = r'0\d{1,2}[ -]?\d{3,4}[ -]?\d{3,4}'  #전화번호를 찾는 정규표현식.
search_target = '''Luke Skywarker 02-123-4567 luke@daum.net
다스베이더 070-9999-9999 darth_vader@gmail.com
princess leia 010 2454 3457 leia@gmail.com'''


# 정규표현식과 일치하는 부분을 모두 찾아주는 파이썬 코드.
import re
result = re.findall(regex, search_target)
print("\n".join(result))
# print(search_target)




# search_target에 들어있는 모든 전화번호를 찾아내서 한 줄씩 출력하는 걸 알 수 있다.