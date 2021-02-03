def exercise():
    print("1번 예제")
    print(solution(45))
    print("2번 예제")
    print(solution(125))

def solution(n):
    answer = 0
    base3 = transNBase(n,3)
    reversedVal = ''
    
    for i in base3:
        reversedVal = i + reversedVal
    
    answer = int(reversedVal,3)
    return answer

def transNBase(n,base): # n을 base진수의 문자열로 바꾸어주는 함수
    val = ''
    while n != 0:
        temp = n%base
        val = str(temp) + val
        n = n//base

    return val
    
exercise()
