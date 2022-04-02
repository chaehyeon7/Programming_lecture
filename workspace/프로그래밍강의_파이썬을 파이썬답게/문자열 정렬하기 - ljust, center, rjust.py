print('가나다라               ') # 좌측정렬
print('               가나다라') # 우측 정렬
print('       가나다라        ') # 가운데 정렬


### 우측 정렬 예  - for문 사용
s = '가나다라'
n = 7

answer = ''
for i in range(n-len(s)): # 문자열의 앞을 빈 문자열로 채우는 for 문
    answer += ' '
answer += s
print(answer)
print(s)


# 파이썬 코드
s = '가나다라'
n = 7

s.ljust(n) # 좌측 정렬
s.center(n) # 가운데 정렬
s.rjust(n) # 우측 정렬