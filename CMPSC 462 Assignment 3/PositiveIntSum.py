def PositiveSum(inputNum):
    if inputNum < 1:
        return 0
    else:
        return inputNum + PositiveSum(inputNum - 2)


print(PositiveSum(9))
print(PositiveSum(1))
print(PositiveSum(0))
