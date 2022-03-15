# 문제 설명
# 이 문제에는 표준 입력으로 문자열, mystr이 주어집니다. mystr에서 가장 많이 등장하는 알파벳만을 사전 순으로 출력하는 코드를 작성해주세요.

# 예시
# input	output
# 'aab'	'a'
# 'dfdefdgf'	'df'
# 'bbaa'	'ab'
import collections
import itertools

my_str = input().strip()
cnt = collections.Counter(my_str).most_common()
max_count = cnt[0][1]

result = []
for i in cnt:
    if i[1] == max_count:
        result.append(i[0])

print(''.join(sorted(result)))