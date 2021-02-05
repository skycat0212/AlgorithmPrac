# 접근방법
# 각각의 숫자를 34 -> 3.4, 355 -> 3.55 등의 형태로 소수로 표현하기
# int형은 그대로
# 정렬 후 문자열로 바꾸기(같은 크기일때, int가 float보다 우선순위에 있음)
# 오답 처리 + 시간 초과
# 오답 이유 - 3.-- 일때, 3.33 기준으로 위 아래에 따라서, 3.-일때는 3.3 기준으로 위 아래에 따라서 우선순위가 달라짐.
# 반례 : 372 와 37, 37이 있을 때, 37 37 372가 되어야 하는데 372 37 37 이 됨.

def exercise():
    print("1번 예제")
    print(solution([6, 10, 2]))
    print("2번 예제")
    print(solution([3, 30, 34, 5, 9, 3, 30, 3, 3, 30])) # 문제 내용 수정
    print("반례")
    print(solution([372, 37, 37]))

def solution(numbers):
    answer = ''

    newNumbers = []
    intList = []
    cnt = 0
    for i in numbers:
        if i < 10:
            intList.append([cnt, i])
            newNumbers.append(i)
        else:
            temp = str(i)
            temp = temp[0] + "." + temp[1:]
            newNumbers.append(float(temp))

    # newNumbers 크기 순으로 정렬하기 (같은 값일 경우 int가 float 보다 큼)
    # 
    for i in range(0,len(newNumbers)-1):
        bigger = newNumbers[i]
        biggerIndex = i
        for j in range(i+1,len(newNumbers)):
            if bigger>newNumbers[j]:
                pass
            elif bigger<newNumbers[j]:
                bigger = newNumbers[j]
                biggerIndex = j
            else:
                if type(bigger) == type(1):
                    pass
                elif type(newNumbers[j]) == type(1):
                    bigger = newNumbers[j]
                    biggerIndex = j
                else:
                    pass
        t = newNumbers[i]
        p = newNumbers[biggerIndex]
        newNumbers[i] = p
        newNumbers[biggerIndex] = t

    for i in newNumbers:
        if type(i) == type(1):
            answer += str(i)
        else:
            t = str(i)
            t = t[0] + t[2:]
            t = int(t)
            answer += str(t)

    print("newNumbers", numbers)
    print("")
    return answer

exercise()
