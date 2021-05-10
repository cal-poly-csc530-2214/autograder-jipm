def addToTen():
    result = 5 + 3 + 2
    return result


# def addToTenNEW():
#     result = {5 + 3 + 2 + 1, 5 + 3 + 2 - 1, 5 + 3 + 2 + 0}
#     return result


def substitute(operation):
    sub = [1, -1, 0]
    generated_operation = []

    for s in sub:
        generated_operation.append(operation + " + " + str(s))

    return generated_operation

print(substitute("v = 5 + 3 + 0"))
