def isPrime(num):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    return prime

num1 = int(input("Input min number ? "))
num2 = int(input("Input max number ? "))

primeList = []
for i in range(num1, num2):
    if isPrime(i) == True:
        primeList.append(i)
print(f'Total prime number = {len(primeList)}')