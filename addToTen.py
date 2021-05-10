def addToTen():
    result = 5 + 3 + 2
    return result


# def addToTenNEW():
#     result = {5 + 3 + 2 + 1, 5 + 3 + 2 - 1, 5 + 3 + 2 + 0}
#     return result


def substitute(operation, correct):
    parsed = operation.split()
    sub = [1, -1, 0]
    potential_result = []

    # assuming operations is all + and is in correct format
    user_res = int(parsed[2]) + int(parsed[4]) + int(parsed[6])

    for s in sub:
        potential_result.append(user_res + s)

    for value in potential_result:
        if value == correct:
            return True

    return False

print(substitute("v = 5 + 3 + 0", 10))
