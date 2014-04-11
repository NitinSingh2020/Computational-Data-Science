import random, pylab

# Problem 1.6
randomList1 = []
randomList2 = []

for i in range(1000):
    randomList1.append(int(random.random() * 2))

for i in range(1000):
    randomList2.append(random.choice((0,1)))

print randomList1
print "Printing random list2"
print randomList2

def quizPlot(xList, yList):
    pylab.title('Distribution Plot')
    pylab.xlabel('number of ')
    pylab.ylabel('list')
    pylab.plot(xList, yList)

#quizPlot(range(1000), randomList1)
#quizPlot()
#pylab.show()

# Problem 3
import random, pylab
xVals = []
yVals = []
wVals = []
for i in range(1000):
    xVals.append(random.random())
    yVals.append(random.random())
    wVals.append(random.random())
xVals = pylab.array(xVals)
yVals = pylab.array(yVals)
wVals = pylab.array(wVals)
xVals = xVals + xVals
zVals = xVals + yVals
tVals = xVals + yVals + wVals

# 3.3
pylab.plot(xVals, yVals)
### 3.4
##pylab.plot(xVals, zVals)
### 3.5
##pylab.plot(sorted(xVals), yVals)
### 3.6
##pylab.plot(xVals, sorted(yVals))
### 3.7
##pylab.plot(sorted(xVals), sorted(yVals))
pylab.show()
