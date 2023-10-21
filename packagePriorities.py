def packagePriority(n):
    I, A, T, S, R = [], [], [], [], []

    for i in range(n):
        inputs = input().split(' ')
        I.append(int(inputs[0]))
        A.append(int(inputs[1]))
        T.append(int(inputs[2]))
        S.append(int(inputs[3]))
        R.append(int(inputs[4]))

    numOfPackages = n
    packages = []
    order = []

    while len(packages) < n:
        if len(I):


        RPriority = min(R)
        SPriority = min(S)

        minR = [I[i] for i in range(len(R)) if R[i] == RPriority]
        minS = [minR[i] for i in range(len(minR)) if S[i] == SPriority]

        if len(packages) == 1:
            packages.append(minR[0])
        elif len(minS) == 1:
            packages.append(minS[0])
        else:
            minimumArrivalTime = 100001
            minIndex = 0
            for element in minS:
                index = I.index(element)
                if A[index] < minimumArrivalTime:
                    minimumArrivalTime = A[index]
                    minIndex = index
            packages.append(I[minIndex])
        for i in range(5):
            print(I)
            index = I.index(packages[-1])
            I.pop(index)
            A.pop(index)
            R.pop(index)
        return packages


print(packagePriority(2))
