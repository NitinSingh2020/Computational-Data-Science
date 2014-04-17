# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    # TODO
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False}
    mutProb = 0.005
    

    time_steps = [300, 150, 75, 0]
    firstPar = time_steps[3]
    secondPar = firstPar + 150


    total = [0. for x in xrange(numTrials)]
    #medicated = [0. for x in xrange(secondPar)]

    # total = [0. for x in xrange(300)]
    # medicated = [0. for x in xrange(300)]

    for trial in range(numTrials):
        viruses = [ResistantVirus(maxBirthProb,clearProb,resistances, mutProb) for i in range(numViruses)]
        patient = TreatedPatient(viruses,maxPop)

        for sim in range(secondPar):
            if sim > (firstPar - 1) :
                patient.addPrescription('guttagonol')
            patient.update()


        total[trial] = (float(patient.getResistPop(['guttagonol'])))
        # medicated[trial] = (float(patient.getResistPop(['guttagonol'])))

    # total  =  [x /numTrials for x in total]
    # medicated=[y /numTrials for y in medicated]
    #print(total,medicated)

    pylab.title("Treated patient simulation", color='red')
    pylab.xlabel("Average Virus Population", color='red') 
    pylab.ylabel("Number of patients", color='red')
    # pylab.legend(loc="best")
    # pylab.plot(total)
    # pylab.plot(medicated)

    pylab.hist(total, bins = 10)
    pylab.show()



# simulationDelayedTreatment(200)


#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False, 'grimpex': False}
    mutProb = 0.005
    

    time_steps = [300, 150, 75, 0]
    firstPar = time_steps[3]
    secondPar = firstPar + 300


    total = [0. for x in xrange(numTrials)]
    # medicated = [0. for x in xrange(secondPar)]

    # total = [0. for x in xrange(300)]
    # medicated = [0. for x in xrange(300)]

    for trial in range(numTrials):
        viruses = [ResistantVirus(maxBirthProb,clearProb,resistances, mutProb) for i in range(numViruses)]
        patient = TreatedPatient(viruses,maxPop)

        for sim in range(secondPar):
            if sim > 149 and sim < (150 + firstPar):
                patient.addPrescription('guttagonol')
            elif sim > (149 + firstPar):
                patient.addPrescription('grimpex')
            patient.update()


        total[trial] = (float(patient.getResistPop(['guttagonol'])))
        # medicated[trial] = (float(patient.getResistPop(['guttagonol'])))

    # total  =  [x /numTrials for x in total]
    # medicated=[y /numTrials for y in medicated]
    #print(total,medicated)

    pylab.title("Treated patient simulation", color='red')
    pylab.xlabel("Average Virus Population", color='red') 
    pylab.ylabel("Number of patients", color='red')
    # pylab.legend(loc="best")
    # pylab.plot(total)
    # pylab.plot(medicated)

    pylab.hist(total, bins = 10)
    pylab.show()

simulationTwoDrugsDelayedTreatment(200)