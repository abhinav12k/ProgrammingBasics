def parseToString(listParam) -> str:
    ans = ""
    for item in listParam:
        ans += str(item) + ", "
    return ans[:-2]

listInput = [1,"2","three","4",5.0]
print(parseToString(listInput))