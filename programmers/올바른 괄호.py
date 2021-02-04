def exercise():
    print("1번 예제")
    print(solution("()()"))
    print("2번 예제")
    print(solution("(())()"))
    print("3번 예제")
    print(solution(")()("))
    print("4번 예제")
    print(solution("(()("))

def solution(s):
    val = 0
    for i in s:
        if i == "(":
            val += 1
        elif i == ")":
            val -= 1
        if val < 0:
            return False
    if val != 0:
        return False

    return True

exercise()