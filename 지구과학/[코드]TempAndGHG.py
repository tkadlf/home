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

#그래프
plt.figure(figsize=(12, 6))
plt.rc('font', family='Malgun Gothic')
plt.plot(averTemp, color='blue', label='평균 기온')
plt.plot(co2, color='red', label='평균 이산화탄소 농도')
plt.plot(methane, color='orange', label='평균 메탄 농도')
plt.plot(nitrous, color='yellow', label='평균 아산화질소 농도')
plt.title('온실가스 농도에 따른 기온 변화 (상대값)')
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()
