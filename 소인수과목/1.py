def isPrime(num):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    return prime

num = int(input('Input number ? '))

primeList = []
for i in range(num):
    if isPrime(i) == True:
        primeList.append(i)
print(f'Maximum prime number = {primeList[-1]}')