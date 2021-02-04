def exercise():
    print("예시 1")
    print(solution("...!@BaT#*..y.abcdefghijklm"))
    print("예시 2")
    print(solution("z-+.^."))
    print("예시 3")
    print(solution("=.="))
    print("예시 4")
    print(solution("123_.def"))
    print("예시 5")
    print(solution("abcdefghijklmn.p"))

def solution(new_id):
    answer = step7(step6(step5(step4(step3(step2(step1(new_id)))))))
    return answer

def step1(inputVal):
    outputVal = inputVal.lower()
    return outputVal

def step2(inputVal):
    outputVal = ''
    for i in inputVal:
        asciiVal = ord(i)
        if (asciiVal >= 97 and asciiVal <= 122) or (asciiVal>=48 and asciiVal<= 57) or (asciiVal == 45) or (asciiVal == 95) or (asciiVal == 46):
            outputVal += i
            
    return outputVal

def step3(inputVal):
    while inputVal.count("..") >= 1:
        targetIndex = inputVal.index("..")
        inputVal = inputVal[:targetIndex] + inputVal[targetIndex+1:]
    return inputVal

def step4(inputVal):
    if inputVal != "" and inputVal[0] == ".":
        inputVal = inputVal[1:]
    if inputVal != "" and inputVal[-1] == ".":
        inputVal = inputVal[:-1]
    return inputVal

def step5(inputVal):
    if inputVal == "":
        inputVal = "a"
    return inputVal

def step6(inputVal):
    if len(inputVal) >= 16:
        inputVal = inputVal[:15]
    inputVal = step4(inputVal)
    return inputVal

def step7(inputVal):
    while len(inputVal) <= 2:
        inputVal += inputVal[-1]
    return inputVal

exercise()