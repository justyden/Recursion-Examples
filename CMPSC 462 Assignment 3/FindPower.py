def FindPowerInt(inputNum, inputPower):
    if inputNum == 0:
        return 0
    elif inputPower == 0:
        return 1
    elif inputPower == 1:
        return inputNum
    else:
        return inputNum * FindPowerInt(inputNum, (inputPower - 1))


print(FindPowerInt(4, 5))
