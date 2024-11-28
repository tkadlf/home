num = int(input('Input amount (maximum = 9999) ? '))
korList = ['','일','이','삼','사','오','육','칠','팔','구']
unitList = ['','십', '백', '천','']

if num > 9999:
    print('Out of range')

else:
    strNum = str(num)  # 숫자를 문자열로 변환
    print(f"Input number: {strNum}")

    numList = [int(digit) for digit in strNum]  # 숫자를 자릿수별로 나눈 리스트
    print(f"Digit list: {numList}")

    # 자릿수에 맞춰 한글로 변환
    result = ""
    for i, digit in enumerate(numList):
        if digit != 0:  # 0인 경우 생략
            result += korList[digit] + unitList[len(numList) - i - 1]

    print(result)

        
    