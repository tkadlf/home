import random as rd

'''
numList = []

while len(numList) < 6:
    num = rd.randint(1,45)

    if num not in numList:
        numList.append(num)
    
print(numList)
'''

'''
operate = ['+', '-', '*']

while True:
    num1 = rd.randint(1,10)
    num2 = rd.randint(1,10)
    op = rd.choice(operate)

    #print(num1, num2, op)
    
    if op == '+':
        num = int(input(f"{num1} + {num2} = "))

        if num == num1 + num2:
            print("right")
        else:
            print(f"wrong ({num1 + num2})")
            
    if op == '-':
        num = int(input(f"{num1} - {num2} = "))

        if num == num1 - num2:
            print("right")
        else:
            print(f"wrong ({num1 - num2})")

    if op == '*':
        num = int(input(f"{num1} x {num2} = "))

        if num == num1 * num2:
            print("right")
        else:
            print(f"wrong ({num1 * num2})")
'''

num = rd.randint(1,100)
minNum = 1
maxNum = 100
#print(num)

while True:
    
    myNum = int(input(f"Guess Number ({minNum}, {maxNum}) ? "))

    if num > myNum:
        print("Up")
        minNum = myNum
    elif num < myNum:
        print("Down")
        maxNum = myNum
    else:
        print("Correct")
        break
