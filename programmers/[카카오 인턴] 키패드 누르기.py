def exercise():
    print("1번 예제")
    print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))
    print("2번 예제")
    print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left"))
    print("3번 예제")
    print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],"right"))

leftBtn = [1,4,7]
rightBtn = [3,6,9]

btnPos = {
    1:[0,3],2:[1,3],3:[2,3],
    4:[0,2],5:[1,2],6:[2,2],
    7:[0,1],8:[1,1],9:[2,1],
    '*':[0,0],0:[1,0],'#':[2,0]
    }


def solution(numbers, hand):
    leftPos = btnPos['*']
    rightPos = btnPos['#']
    answer = ''

    for i in numbers:
        leftDis = 0
        rightDis = 0
        if leftBtn.count(i) == 1:
                leftPos = btnPos[i]
                answer += 'L'
        elif rightBtn.count(i) == 1:
            rightPos = btnPos[i]
            answer += 'R'
        else:
            leftDis = calDistance(leftPos,btnPos[i])
            rightDis = calDistance(rightPos,btnPos[i])
            if leftDis < rightDis:
                leftPos = btnPos[i]
                answer += 'L'
            elif leftDis > rightDis:
                rightPos = btnPos[i]
                answer += 'R'
            else:
                if hand == 'left':
                    leftPos = btnPos[i]
                    answer += 'L'
                else:
                    rightPos = btnPos[i]
                    answer += 'R'

    return answer

def calDistance(pos1, pos2):
    return ((pos1[0] - pos2[0])**2)**(0.5) + ((pos1[1] - pos2[1])**2)**(0.5)

exercise()