def getFac(num):
    fac = 1
    for i in range(1, num + 1):
        fac *= i
    return fac
def isEven(num):
    if num % 2 == 0:
        return True
    return False
def isPrime(num):
    isPrime = True
    for i in range(2, num):
        if num % i == 0:
            isPrime = False
            break
    return isPrime
def printNum(num):
    if num < 0:
        return
    printNum(num - 1)
    print(num, end = ' ')
def getFactorial(num):
    if num < 2:
        return 1
    return num * getFactorial(num - 1)
def fibo(num):
    if num == 1 or num == 2:
        return 1
    return fibo(num - 1) + fibo(num - 2)

num = int(input("input number ? "))

#팩토리얼 더하기
sum = 0
for i in range(1, num + 1):
    sum += getFac(i)
    if i == num:
        print(f"{i}! =", end = " ")
    else:
        print(f"{i}! +", end = " ")
print(sum)

#소수 더하기
primeList = []

for i in range(2, num + 1):
    if isPrime(i) == True:
        sum += i
        primeList.append(i)

for i in range(len(primeList)):
    if i == len(primeList) - 1:
        print(f"{primeList[i]} =", end = " ")
    else:
        print(f"{primeList[i]} +", end = " ")
print(sum)

#printNum(num)
#print(getFactorial(num))
#print(fibo(num))

# 소수 최대값 뽑기
primeList = []

for i in range(2, num + 1):
    if isPrime(i) == True:
        primeList.append(i)
maxPrime = primeList[len(primeList) - 1]
print(f'max prime number = {maxPrime}')


maxPrime = 1
for i in range(2, num + 1):
    if isPrime(i) == True:
        maxPrime = i
print(f'max prime number = {maxPrime}')