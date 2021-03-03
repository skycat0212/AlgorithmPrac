def exercise():
    print("1번 예제")
    print(solution(10, 2))
    print("2번 예제")
    print(solution(8, 1))
    print("3번 예제")
    print(solution(24, 24))

def solution(brown, yellow):
    answer = []

    n = brown
    m = yellow

    # m = a*b (a = 노란색의 세로, b = 노란색의 가로)
    # m의 약수쌍 구하기
    dividers = getDividers(m)
    print('dividers',dividers)

    for (a,b) in dividers:
        if a+b == (n-4)/2:
            print(a,b)
            answer = [b+2, a+2]
            return answer
    return answer

def getDividers(num):
    dividers = []
    
    if num == 1:
        dividers = [(1,1)]
        return dividers

    for i in range(1,num):
        if num%i == 0:
            dividers.append((i,num//i))
        if (num//i) < i:
            break

    return dividers


exercise()