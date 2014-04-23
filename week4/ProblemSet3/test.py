import ps3b
#import ps3bTest

def test1():
	virus = ps3b.ResistantVirus(0.0, 1.0, {"drug1":True, "drug2":False}, 0.0)
	print "\n+++++++++++++++++++"
	print "Running test1 ... "
	print "+++++++++++++++++++"
	print "Should be False, is ", virus.isResistantTo('drug2'), "\n"

def test2():
	print "\n+++++++++++++++++++"
	print "Running test2 ... "
	print "+++++++++++++++++++"
	ps3b.simulationWithoutDrug(100, 1000, 0.1, 0.05, 100)

def test3():
	print "\n+++++++++++++++++++"
	print "Running test3 ... "
	print "+++++++++++++++++++"
	virus = ps3b.ResistantVirus(1.0, 0.0, 
		{'drug1':True, 'drug2': True, 'drug3': True, 'drug4': True, 'drug5': True, 'drug6': True}, 0.5)

def test4():
	print "\n+++++++++++++++++++"
	print "Running test4 ... "
	print "+++++++++++++++++++"
	virus = ps3b.ResistantVirus(1.0, 0.0, {}, 0.0)
	patient = TreatedPatient([virus], 100)

def test5():
	print "\n+++++++++++++++++++"
	print "Running test5 ... "
	print "+++++++++++++++++++"
	numViruses = 1000
	maxPop = 1000
	maxBirthProb = 0.1 
	clearProb = 0.05
	resistances = {'guttagonol': False}
	mutProb = 0.005
	numTrials = 100

	ps3b.simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, 
		resistances, mutProb, numTrials)

def test6():
	virus = ps3b.ResistantVirus(1.0, 0.0, 
		{'drug1':True, 'drug2': True, 'drug3': True, 'drug4': True, 'drug5': True, 'drug6': True}, 0.5)
	for i in range(10):
		print "============================"
		print "Loop %s" % i
		childVirus = virus.reproduce(0, [])
		print "Before method"
		myAttrList = [method for method in dir(childVirus) if callable(getattr(childVirus, method))]
		print myAttrList
		print "After method"
		print "Child Virus : %s\n" %i, childVirus.resistances



if __name__ == '__main__':
	# test1()
	# test2()
	# test3()
	# test4()
	test5()
	# test6()