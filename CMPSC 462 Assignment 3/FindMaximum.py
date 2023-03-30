def FindMaxList(inputList, maxInt=None):
    if maxInt is None:
        if len(inputList) == 0:
            return 0
        elif len(inputList) == 1:
            return inputList[0]
        else:
            return FindMaxList(inputList[1:], inputList[0])
    else:
        if len(inputList) == 0:
            return maxInt
        if maxInt < inputList[0]:
            maxInt = inputList[0]
            return FindMaxList(inputList[1:], maxInt)
        else:
            return FindMaxList(inputList[1:], maxInt)


list1 = [1, 4, 20, 15, 39, 40, 4, 9, 15, 10, 24, 7]
print(FindMaxList(list1))
list2 = [1]
print(FindMaxList(list2))
list3 = []
print(FindMaxList(list3))
