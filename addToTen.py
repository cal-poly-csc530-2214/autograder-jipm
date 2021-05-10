def addToTen():
    result = 5 + 3 + 2
    return result

def substitute(operation, correct):
    parsed = operation.split()
    substitute = [1, -1, 0]
    potential_result = []

    # assuming operations is all + and is in correct format
    user_res = operation[2] + operation[4] + operation[6]

    for s in substitue:
        res.append(user_res + s)

    for value in res:
        if value == correct:
            return True

    return False
