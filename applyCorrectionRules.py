def generateMPY(operation):
    sub = [0, 1, -1]
    generated_operation = []
    result = []

    for s in sub:
        if (s != "v" and s != "="):
            generated_operation.append(operation + " + " + str(s))

    for s in generated_operation:
        result.append(s[4:])

    return result


