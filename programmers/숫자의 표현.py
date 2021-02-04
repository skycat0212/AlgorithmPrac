def exercise():
    print("예제 1번")
    print(solution(15))

a = 0
temp1 = []
for i in range(0,151):
    a += i
    temp1.append(a)

def solution(n):
    answer = 0
    indexN = 0
    for i in temp1:
        if i > n:
            indexN = temp1.index(i)
            break
    for i in range(1,indexN):
        if i%2 == 1:
            if n%i == 0:
                answer += 1
                # print("i는", i)
                # print("answer는", answer)
        elif i%2 == 0:
            if (n%(i//2) == 0) and ((n//(i//2)-1)%2 == 0):
                answer += 1
                # print("i는", i)
                # print("answer는", answer)
    return answer

exercise()