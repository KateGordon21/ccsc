def integerBounces(n):
    outputs = []
    for i in range(n):
        dh = input('').split(' ')
        d, h = int(dh[0]), int(dh[1])

        numOfBounces = 0
        if d == 1:
            outputs.append(h)
        elif h / d % 1 != 0:
            outputs.append(0)
        else:
            while h / d % 1 == 0:
                numOfBounces += 1
                h = h / d
            outputs.append(numOfBounces)

    for element in outputs:
        print(element)


if __name__ == "__main__":
    n = int(input())
    integerBounces(n)
