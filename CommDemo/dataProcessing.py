from datetime import datetime
import numpy as np
import statistics

# This makes fake data!
f = open('data.txt', 'w')
i = 0

print('Running...')

while i < 100:
	time = datetime.now()
	data = np.random.randint(1,30)
	line = str(time) + '|' + str(data) + '\n'
	f.write(line)
	i += 1

print('Done!')
f.close()

# Data processing stuff
f = open('data.txt', 'r')
dataList = []
#lineNum = 0
for line in f:
	dataPoint = line.split("|")
	data = dataPoint[1][:-1]
	#print(data)
	dataList.append(float(data))
f.close()

# Line writing stuff
time = dataPoint[0]
average = statistics.mean(dataList)
line = time + ',' + str(average)
print(line)
f = open('dataAverage.txt', 'w')
f.write(line)
f.close()
	#print(str(lineNum) + ', ' + line)
	#lineNum += 1
