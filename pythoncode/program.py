limit = 60000
avgNum = 5

f = open("pimil.txt")

pi = f.read()
pi = pi.replace("\n", "")
pi = pi.replace(" ", "")

f2 = open("output.txt", "r+")

avg = 0.0

for i in range(0, limit, avgNum):
	substr = pi[i:i+avgNum]
	for j in range(avgNum):
		avg += int(substr[j])
	avg = avg / avgNum
	f2.write(str(avg) + "\n")
	avg = 0.0