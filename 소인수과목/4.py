import random as r

num1 = r.randint(0,10)
num2 = r.randint(0,10)
numList = []

for i in range(5):
    numList.append(num1 + i*num2)

ans = numList[3]
numList[3] = '?'
print(numList)

num = int(input("Input number ? "))

if num == ans:
    print('Correct')
else:
    print(f"Wrong, answer = {ans}")