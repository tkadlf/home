def isPrime(num):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    return prime

def getFac(num):
    fac = 1
    for i in range(1, num + 1):
        fac *= i
    return fac


num1 = int(input("input number 1 ? "))
num2 = int(input("input number 2 ? "))
primeList = []
sumValue = 0

f = open("Sample.txt", "w")

# 5! + 7! + 11! + 13! = 6266942760

for i in range(num1, num2 + 1):
    if isPrime(i) == True:
        sumValue += getFac(i)
        primeList.append(i)

for i in range(len(primeList)):
    if i == len(primeList) - 1:
        print(f"{primeList[i]}! =", end = " ")
        f.write(f"{primeList[i]}! = ")
    else:
        print(f"{primeList[i]}! +", end = " ")
        f.write(f"{primeList[i]}! + ")
print(sumValue)
f.write(str(sumValue))



f = open("input.txt", "r")
data = f.read()
splitList = data.split(",")
for num in splitList:
    print(num, end = ' ')

f.close()



f = open("time.txt", "w")

for i in range (1, 10):
    for j in range(1,10):
            f.write(f"{j}x{i}={i * j :2} ")
    f.write('\n')

f.close()

f = open("time.txt", "r")
while True:
     ch = f.read(1)
     if not ch:
          break
     if ch == '5' or ch == '3':
          print("*", end = '')
     else:
          print(ch, end = '')

f.close()