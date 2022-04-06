# len과 index를 이용하여 각 원소에 접근.
def solution(mylist):
    answer = []
    for i in range(len(mylist)-1):
        answer.append(abs(mylist[i] - mylist[i+1]))
    return answer

if __name__ == '__main__':
    mylist = [83, 48, 13, 4, 71, 11]
    print(solution(mylist))

# 파이썬 zip을 이용하면 index를 사용하지 않고 각 원소에 접근할 수 있다.
def solution(mylist):
    answer = []
    for number1, number2 in zip(mylist, mylist[1:]):
        answer.append(abs(number1 - number2))
    return answer

if __name__ == '__main__':
    mylist = [83, 48, 13, 4, 71, 11]
    print(solution(mylist))