#============== Problem 1 ================
def isAlphabeticalWord(word, wordList = None):
    if (len(word) > 0):
        curr = word[0]
    for letter in word:
        if (curr > letter):
            return False
        else:
            curr = letter
    if wordList is None:
        return True
    return word in wordList

print ('Problem 1')
print isAlphabeticalWord('abcd') # true
print isAlphabeticalWord('zoo')  # false

#============= Problem 2.1 =================
def lotsOfParameters1(a,b,c,d,e):
    print a
    print b
    print c
    print d
    print e

print ('Problem 2.1')
#print lotsOfParameters1()
#print lotsOfParameters1(1,2)
print lotsOfParameters1(1,e=5,d=4,c=3,b=2)
print lotsOfParameters1(e=5,a=1,d=4,b=2,c=3)
#print lotsOfParameters1(a=5,b=1,c=4,d=2,3)

#======= Problem 2.2 ==============
def lotsOfParameters2(a=1,b=2,c=3,d=4,e=5):
    print a
    print b
    print c
    print d
    print e

print ('Problem 2.2')
lotsOfParameters2()
lotsOfParameters2(1, 2)
lotsOfParameters2(1, c=2)
##lotsOfParameters2(1, c=2,3)
lotsOfParameters2(1,e=20,b=3)
##lotsOfParameters2(1,e=20,b=3,a=10)

#============= Problem 2.3 =================
def lotsOfParameters3(a,b,c=3,d=4,e=5):
    print a
    print b
    print c
    print d
    print e
    
print ('Problem 2.3')
##lotsOfParameters3()
lotsOfParameters3(1,2)
##lotsOfParameters3(1,c=2)
##lotsOfParameters3(1,c=2,3)
lotsOfParameters3(1,c=2,b=3)

inFile = open("julyTemps.txt", 'r')
list1 = []
list2 = []
line = inFile.readline()
print line

