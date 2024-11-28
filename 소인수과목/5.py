def aver(x, y, z):
    average = (x + y + z)/3
    return round(average, 2)

def grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'
    

f = open('input.txt', 'r')
data = f.read()

scoreList = []

for row in data.split('\n'):
    scoreList.append(row.split(','))

f.close()

print(len(scoreList))
averList = []
gradeList = []

for i in range(len(scoreList)):
    x = int(scoreList[i][1])
    y = int(scoreList[i][2])
    z = int(scoreList[i][3])

    average = aver(x, y, z)
    averList.append(average)
    gradeList.append(grade(average))

print(averList)

for i in range(len(scoreList)):
    print(scoreList[i][0], end = ' ')
    print(f"{scoreList[i][0]} {scoreList[i][1]} {scoreList[i][2]} {scoreList[i][3]} {averList[i]} {gradeList[i]}")

f = open('output.txt', 'w')

for i in range(len(scoreList)):
        f.write(f"{scoreList[i][0]} {scoreList[i][1]} {scoreList[i][2]} {scoreList[i][3]} {averList[i]} {gradeList[i]}\n")