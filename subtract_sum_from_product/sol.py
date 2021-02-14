test = 234
toStr = str(test)
print(toStr)
digits = []
length = len(toStr)
print(length)
count = length - 1

for i in range(length):
    temp = toStr[count]
    print(temp)
    digits.append(int(temp))
    count = count - 1
    # print("count " + count)

print(digits)