import matplotlib.pyplot as plt
import csv

tempPath = 'temperature-anomaly.csv'
ghgPath = 'ghg-emissions-by-gas.csv'

#기온
with open(tempPath, 'r', encoding = 'utf-8') as f:
    data = csv.reader(f, delimiter = ',')

    next(data)
        
    averTemp = []
    years = []    
    baseline_temp = 14.0
        
        
    for row in data:
            
        temp = float(row[3])
        averTemp.append(temp)
        years.append(int(row[2]))

#온실가스
with open(ghgPath, 'r', encoding = 'cp949') as f:
    data = csv.reader(f, delimiter = ',')

    next(data)

    co2 = []
    nitrous = []
    methane = []
    
    for row in data:
        co2Value = float(row[5])
        nitrousValue = float(row[3])
        methaneValue = float(row[4])
        co2.append(co2Value/10000000000)
        nitrous.append(nitrousValue/1000000000)
        methane.append(methaneValue/10000000000)

#1을 1850으로 옮기기
newAverTemp = [0] * (1849 + len(averTemp))
newCo2 = [0] * (1849 + len(co2))
newNitrous = [0] * (1849 + len(nitrous))
newMethane = [0] * (1849 + len(methane))
newYears = [0] * (1849 + len(years))

for i in range(len(averTemp)):
    newAverTemp[i + 1849] = averTemp[i]
    newCo2[i + 1849] = co2[i]
    newNitrous[i + 1849] = nitrous[i]
    newMethane[i + 1849] = methane[i]
    newYears[i + 1849] = years[i]

averTemp = newAverTemp
co2 = newCo2
nitrous = newNitrous
methane = newMethane
years = newYears

# 그래프 그리기
plt.figure(figsize=(12, 8))
plt.rc('font', family='Malgun Gothic')
plt.grid()
plt.xlim(1850, 2022)

plt.plot(averTemp, color='blue', label='평균 기온 편차')
plt.plot(co2, color='red', label='평균 이산화탄소 배출량')
plt.plot(methane, color='orange', label='평균 메테인 배출량')
plt.plot(nitrous, color='yellow', label='평균 아산화질소 배출량')
plt.title('온실가스 농도에 따른 기온 배출량 1850 ~ 2023 (상대값)')
plt.xlabel('연도', loc = 'left', size = 20 )
plt.legend()

plt.show()
