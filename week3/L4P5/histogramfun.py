import pylab

# You may have to change this path
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    proportion = []
    for word in wordList:
        count = 0.
        wordLength = 0.
        for char in word:
            wordLength += 1
            if char in ['a', 'e', 'i', 'o', 'u']:
                count += 1
        proportion.append(count/wordLength)
        count = 0.
        wordLength = 0.
    pylab.hist(proportion, bins = numBins)
    xmin,xmax = pylab.xlim()
    ymin,ymax = pylab.ylim()
    pylab.title('Fraction of vowels in words')
    pylab.xlabel('Fraction of vowels in word')
    pylab.ylabel('Number of words')
    pylab.show()

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
