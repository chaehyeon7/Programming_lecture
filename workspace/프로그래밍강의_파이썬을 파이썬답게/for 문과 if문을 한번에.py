# 제 설명
# 정수를 담은 리스트 mylist를 입력받아,
# 이 리스트의 원소 중 짝수인 값만을 제곱해 담은 새 리스트를 리턴하는 solution함수를 완성해주세요. 예를 들어, [3, 2, 6, 7]이 주어진 경우
#
# 3은 홀수이므로 무시합니다.
# 2는 짝수이므로 제곱합니다.
# 6은 짝수이므로 제곱합니다.
# 7은 홀수이므로 무시합니다.
def solution(mylist):
    answer = []
    answer = [i**2 for i in mylist if i%2 == 0]
    return answer

# for문과 if를 나눠서 쓸경우 (시간이 더 오래 걸림)
mylist = [3, 2, 6, 7]
answer = []
for number in mylist:
    if number % 2 == 0:
        answer.append(number**2)
