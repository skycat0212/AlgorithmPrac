dataSample = [8,9,3,6,1,7,2,4,5]
print("원래 데이터 : ", dataSample)

def selectionSort(data):
    for i in range(0, len(data)):
        biggest = data[i]
        biggestIndex = i
        for j in range(i, len(data)):
            if biggest >= data[j]:
                pass
            else:
                biggest = data[j]
                biggestIndex = j
        data[i],data[biggestIndex] = data[biggestIndex],data[i]
        print(data)
    return data

selectionSort(dataSample)


