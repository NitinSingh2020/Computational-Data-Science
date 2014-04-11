def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) == 0:
        return float('NaN')
    stdDev = 0
    avgL = 0
    lenList = [len(string) for string in L]
    for a in lenList:
        avgL += a
    avgL = avgL/float(len(L))
    N = len(L)
    for string in L:
        stdDev += (len(string) - avgL)**2
    return (stdDev/float(N))**0.5
        


L = ['a', 'z', 'p']
print stdDevOfLengths(L) # 0
L = ['apples', 'oranges', 'kiwis', 'pineapples']
print stdDevOfLengths(L) # 1.8708

# ===============================================
def avg(L):
    """
    L: a list of numbers

    returns: float, the average of the numbers in the list,
    or NaN if L is empty
    """
    if len(L) == 0:
        return float('NaN')
    avgL = 0
    for a in L:
        avgL += a
    avgL = avgL/float(len(L))
    return avgL
    
def stdDev(L):
    """
    L: a list of numbers

    returns: float, the standard deviation of the numbers in the list,
    or NaN if L is empty
    """
    if len(L) == 0:
        return float('NaN')
    stdDev = 0
    avgL = avg(L)
    for a in L:
        stdDev += (a - avgL)**2
    return (stdDev/float(len(L)))**0.5
    
def coeffOfVar(L):
    avgL = avg(L)
    stdDevL = stdDev(L)
    return stdDevL/float(avgL)

print coeffOfVar([10, 4, 12, 15, 20, 5])

print coeffOfVar([1, 2, 3])
print coeffOfVar([11, 12, 13])
print coeffOfVar([0.1, 0.1, 0.1])
