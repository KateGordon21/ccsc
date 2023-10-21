def findMaxWorkingConsecDays(days):
    maxWorkingDays = 0
    currentWorkingDays = 0

    for day in days:
        if day > 6:
            currentWorkingDays += 1
            maxWorkingDays = max(maxWorkingDays, currentWorkingDays)
        else:
            currentWorkingDays = 0

    return maxWorkingDays

if __name__=="__main__":
    x=input()
    working_status = list(map(int, input().split()))
    print(findMaxWorkingConsecDays(working_status))