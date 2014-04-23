import random
def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    hits = 0
	for trial in range(numTrials):
	    draw = random.sample([1, 2, 3, 4, 5, 6], 3)
	    if max(draw) == 3 or min(draw) == 4:
	        hits += 1
	return float(hits)/numTrials


