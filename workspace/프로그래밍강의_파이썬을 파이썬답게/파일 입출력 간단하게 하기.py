# EOF를 만날 때까지, 파일 읽기를 반복.

f = open('myfile.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    raw = line.split()
    print(raw)
f.close()

# 파이썬의 with - as 구문을 이용하면 코드를 더 간결하게 짤 수 있습니다. 코드를 아래와 같이 쓰면 다음과 같은 장점이 있다.

# 파일을 close 하지 않아도 됨: with - as 블록이 종료되면 파일이 자동으로 close 된다.
# readlines가 EOF까지만 읽으므로, while 문 안에서 EOF를 체크할 필요가 없다.
with open('myfile.txt') as file:
    for line in file.readlines():
        print(line.strip().split('\t'))
# ⨳ with - as 구문은 파일 뿐만 아니라 socket이나 http 등에서도 사용할 수 있다.

