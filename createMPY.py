from addToTen import *
from applyCorrectionRules import *

res = substitute("v = 5 + 3 + 2")
res = ", ".join(res)
correction = "result = {" + res + "}"

print("def addToTen():")
print("    " + correction)
print("    return result")
print()
