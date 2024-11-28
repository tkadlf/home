def isDivisor(m, n):
    if m % n == 0:
        return True
    else:
        return False
    
f = open('result.txt', 'w')

num = int(input("input number ? "))
sum = 0

for i in range(1, num + 1):

    if isDivisor(num, i) == True:

        if i != num:
            print(f"{i} + ", end = '')
            f.write(f"{str(i)} + ")

        else:
            print(f"{i} = ", end = '')
            f.write(f"{str(i)} = ")

        sum += i

print(sum)
f.write(str(sum))

f.close()