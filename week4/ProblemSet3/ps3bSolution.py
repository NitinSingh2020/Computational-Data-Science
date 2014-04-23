# # Problem Set 3: Simulating the Spread of Disease and Virus Population Dynamics
#
import numpy
import random
import pylab
# from pudb import set_interrupt_handler; set_interrupt_handler()
from numpy import average
#random.seed(0)
'''
Begin helper code
'''
 
 
class NoChildException(Exception):
    pass
 
 
 
 
 
class SimpleVirus(object):
    """
   Representation of a simple virus (does not model drug effects/resistance).
   """
 
    def __init__(self, maxBirthProb, clearProb):
        """
       Initialize a SimpleVirus instance, saves all parameters as attributes
       of the instance.
       maxBirthProb: Maximum reproduction probability (a float between 0-1)
       clearProb: Maximum clearance probability (a float between 0-1).
       """
 
        self.max_birth_prob = maxBirthProb
        self.clear_prob = clearProb
    # set_interrupt_handler()
    def getMaxBirthProb(self):
        """
       Returns the max birth probability.
       """
        return self.max_birth_prob
 
    def getClearProb(self):
        """
       Returns the clear probability.
       """
        return self.clear_prob
 
    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
       patient's body at a time step.
       returns: True with probability self.getClearProb and otherwise returns
       False.
       """
        return self.getClearProb() > random.random()
 
 
    def reproduce(self, popDensity):
        """
       Stochastically determines whether this virus particle reproduces at a
       time step. Called by the update() method in the Patient and
       TreatedPatient classes. The virus particle reproduces with probability
       self.maxBirthProb * (1 - popDensity).
 
       If this virus particle reproduces, then reproduce() creates and returns
       the instance of the offspring SimpleVirus (which has the same
       maxBirthProb and clearProb values as its parent).
 
       popDensity: the population density (a float), defined as the current
       virus population divided by the maximum population.
 
       returns: a new instance of the SimpleVirus class representing the
       offspring of this virus particle. The child should have the same
       maxBirthProb and clearProb values as this virus. Raises a
       NoChildException if this virus particle does not reproduce.
       """
        if self.max_birth_prob * (1 - popDensity) > random.random():
            return SimpleVirus(self.max_birth_prob, self.clear_prob)
        raise NoChildException()
 
 
class Patient(object):
    """
   Representation of a simplified patient. The patient does not take any drugs
   and his/her virus populations have no drug resistance.
   """
 
    def __init__(self, viruses, maxPop):
        """
       Initialization function, saves the viruses and maxPop parameters as
       attributes.
 
       viruses: the list representing the virus population (a list of
       SimpleVirus instances)
 
       maxPop: the maximum virus population for this patient (an integer)
       """
 
        self.viruses = viruses
        self.max_pop = maxPop
 
    def getViruses(self):
        """
       Returns the viruses in this Patient.
       """
        return self.viruses
 
 
    def getMaxPop(self):
        """
       Returns the max population.
       """
        return self.max_pop
 
 
    def getTotalPop(self):
        """
       Gets the size of the current total virus population.
       returns: The total virus population (an integer)
       """
        return len(self.viruses)
 
 
    def update(self):
        """
       Update the state of the virus population in this patient for a single
       time step. update() should execute the following steps in this order:
 
       - Determine whether each virus particle survives and updates the list
       of virus particles accordingly.
 
       - The current population density is calculated. This population density
         value is used until the next call to update()
 
       - Based on this value of population density, determine whether each
         virus particle should reproduce and add offspring virus particles to
         the list of viruses in this patient.
 
       returns: The total virus population at the end of the update (an
       integer)
       """
        virus_copy = self.viruses[:]
        # if the virus clears,remove it form the list
        for virus in virus_copy:
            if virus.doesClear():
                self.viruses.remove(virus)
 
        final_virus_count = []
        for surviving_virus in self.viruses:
            final_virus_count.append(surviving_virus)
            try:
                # #only appends if it reproduces, exception passes silently otherwise
                pop_density = float(self.getTotalPop()) / float(self.max_pop)
                final_virus_count.append(surviving_virus.reproduce(pop_density))
            except NoChildException:pass
        self.viruses=final_virus_count
        return self.getTotalPop()
 
def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
   Run the simulation and plot the graph for problem 3 (no drugs are used,
   viruses do not have any drug resistance).
   For each of numTrials trial, instantiates a patient, runs a simulation
   for 300 timesteps, and plots the average virus population size as a
   function of time.
 
   numViruses: number of SimpleVirus to create for patient (an integer)
   maxPop: maximum virus population for patient (an integer)
   maxBirthProb: Maximum reproduction probability (a float between 0-1)
   clearProb: Maximum clearance probability (a float between 0-1)
   numTrials: number of simulation runs to execute (an integer)
   """
    total = []
    # each trial in specified amount
    for trial in range(numTrials):
        # create viruses based on numViruses
        viruses = [(SimpleVirus(maxBirthProb, clearProb)) for v in range(numViruses)]
        #init patient with viruses and max pop of viruses for a patient
        patient = Patient(viruses, maxPop)
        total = [[patient.update()] for tick in range(300)]
    total = [average(x) for x in total]
    pylab.plot(total, label="SimpleVirus")
    pylab.title("SimpleVirus simulation", color='red')
    pylab.xlabel("Time steps")
    pylab.ylabel("Average Virus Population", color='red')
    pylab.legend(loc="best")
    pylab.show()
 
#simulationWithoutDrug(1, 90, 0.8, 0.1, 1)
 
# PROBLEM 4
#
class ResistantVirus(SimpleVirus):
    """
   Representation of a virus which can have drug resistance.
   """
 
    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
           Initialize a ResistantVirus instance, saves all parameters as attributes
           of the instance.
 
           maxBirthProb: Maximum reproduction probability (a float between 0-1)
 
           clearProb: Maximum clearance probability (a float between 0-1).
 
           resistances: A dictionary of drug names (strings) mapping to the state
           of this virus particle's resistance (either True or False) to each drug.
           e.g. {'guttagonol':False, 'srinol':False}, means that this virus
           particle is resistant to neither guttagonol nor srinol.
 
           mutProb: Mutation probability for this virus particle (a float). This is
           the probability of the offspring acquiring or losing resistance to a drug.
           """
        SimpleVirus.__init__(self, clearProb,maxBirthProb)
        self.max_birth = maxBirthProb
        self.clear_prob = clearProb
        self.resistances = resistances
        self.mut_prob = mutProb
 
 
    def getResistances(self):
        """
       Returns the resistances for this virus.
       """
        return self.resistances
 
    def getMutProb(self):
        """
       Returns the mutation probability for this virus.
       """
        return self.mut_prob
 
    def isResistantTo(self, drug):
        """
       Get the state of this virus particle's resistance to a drug. This method
       is called by getResistPop() in TreatedPatient to determine how many virus
       particles have resistance to a drug.
 
       drug: The drug (a string)
 
       returns: True if this virus instance is resistant to the drug, False
       otherwise.
 
       """
 
        return self.resistances.get(drug,False)
       
 
 
 
    def reproduce(self, popDensity, activeDrugs):
        """
       Stochastically determines whether this virus particle reproduces at a
       time step. Called by the update() method in the TreatedPatient class.
 
       A virus particle will only reproduce if it is resistant to ALL the drugs
       in the activeDrugs list. For example, if there are 2 drugs in the
       activeDrugs list, and the virus particle is resistant to 1 or no drugs,
       then it will NOT reproduce.
 
       Hence, if the virus is resistant to all drugs
       in activeDrugs, then the virus reproduces with probability:
 
       self.maxBirthProb * (1 - popDensity).
 
       If this virus particle reproduces, then reproduce() creates and returns
       the instance of the offspring ResistantVirus (which has the same
       maxBirthProb and clearProb values as its parent). The offspring virus
       will have the same maxBirthProb, clearProb, and mutProb as the parent.
 
       For each drug resistance trait of the virus (i.e. each key of
       self.resistances), the offspring has probability 1-mutProb of
       inheriting that resistance trait from the parent, and probability
       mutProb of switching that resistance trait in the offspring.
 
       For example, if a virus particle is resistant to guttagonol but not
       srinol, and self.mutProb is 0.1, then there is a 10% chance that
       that the offspring will lose resistance to guttagonol and a 90%
       chance that the offspring will be resistant to guttagonol.
       There is also a 10% chance that the offspring will gain resistance to
       srinol and a 90% chance that the offspring will not be resistant to
       srinol.
 
       popDensity: the population density (a float), defined as the current
       virus population divided by the maximum population
 
       activeDrugs: a list of the drug names acting on this virus particle
       (a list of strings).
 
       returns: a new instance of the ResistantVirus class representing the
       offspring of this virus particle. The child should have the same
       maxBirthProb and clearProb values as this virus. Raises a
       NoChildException if this virus particle does not reproduce.
       """
        # if it is not resistant to any drug raise no child exception as it does not reproduce
        for drug in activeDrugs:
            if not self.isResistantTo(drug):
                raise NoChildException()
        if (self.max_birth * (1 - popDensity)) > random.random():
            child_resistances = {}
            for drugs in self.resistances:
                if self.mut_prob > random.random():
                #  if a virus particle is resistant to guttagonol but not
                #srinol, and self.mutProb is 0.1, then there is a 10% chance that
                #that the offspring will lose resistance to guttagonol and a 90%
                #chance that the offspring will be resistant to guttagonol.
                    child_resistances[drugs] = not self.getResistances()[drugs]
                else:
                    child_resistances[drugs] = self.getResistances()[drugs]
                        # return instance with new resistances
            return ResistantVirus(self.max_birth, self.clear_prob, child_resistances, self.mut_prob)
        raise NoChildException()
 
 
 
class TreatedPatient(Patient):
    """
   Representation of a patient. The patient is able to take drugs and his/her
   virus population can acquire resistance to the drugs he/she takes.
   """
 
    def __init__(self, viruses, maxPop):
        """
           Initialization function, saves the viruses and maxPop parameters as
           attributes. Also initializes the list of drugs being administered
           (which should initially include no drugs).
 
           viruses: The list representing the virus population (a list of
           virus instances)
 
           maxPop: The  maximum virus population for this patient (an integer)
           """
        Patient.__init__(self,viruses, maxPop)
        self.drug_list = []
        self.viruses = viruses
        self.max_pop = maxPop
 
    def addPrescription(self, newDrug):
        """
       Administer a drug to this patient. After a prescription is added, the
       drug acts on the virus population for all subsequent time steps. If the
       newDrug is already prescribed to this patient, the method has no effect.
 
       newDrug: The name of the drug to administer to the patient (a string).
 
       postcondition: The list of drugs being administered to a patient is updated
       """
 
        if newDrug not in self.drug_list:
            self.drug_list.append(newDrug)
 
    def getPrescriptions(self):
        """
       Returns the drugs that are being administered to this patient.
 
       returns: The list of drug names (strings) being administered to this
       patient.
       """
 
        return self.drug_list
 
 
    def getResistPop(self, drugResist):
        """
       Get the population of virus particles resistant to the drugs listed in
       drugResist.
 
       drugResist: Which drug resistances to include in the population (a list
       of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])
 
       returns: The population of viruses (an integer) with resistances to all
       drugs in the drugResist list.
       """
        count = 0
        for virus in self.viruses:
            # viruses need to be resistant to all drugs to be truly resistant
            if all(virus.isResistantTo(drug) for drug in drugResist):
                count += 1
        return count
 
 
 
    def update(self):
        """
       Update the state of the virus population in this patient for a single
       time step. update() should execute these actions in order:
 
       - Determine whether each virus particle survives and update the list of
         virus particles accordingly
 
       - The current population density is calculated. This population density
         value is used until the next call to update().
 
       - Based on this value of population density, determine whether each
         virus particle should reproduce and add offspring virus particles to
         the list of viruses in this patient.
         The list of drugs being administered should be accounted for in the
         determination of whether each virus particle reproduces.
 
       returns: The total virus population at the end of the update (an
       integer)
       """
 
        virus_copy = self.viruses[:]
        # if the virus clears,remove it form the list
        for virus in virus_copy:
            if virus.doesClear():
                self.viruses.remove(virus)
        final_virus_count = self.viruses[:]
        for surviving_virus in final_virus_count:
            try:
                pop_density = float(self.getTotalPop()) / self.max_pop
                #only appends if it reproduces, exception passes silently otherwise
                self.viruses.append(surviving_virus.reproduce(pop_density,self.drug_list))
            except NoChildException:pass
        return self.getTotalPop()
 
 
def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
 
    """
   Runs simulations and plots graphs for problem 5.
 
   For each of numTrials trials, instantiates a patient, runs a simulation for
   150 timesteps, adds guttagonol, and runs the simulation for an additional
   150 timesteps.  At the end plots the average virus population size
   (for both the total virus population and the guttagonol-resistant virus
   population) as a function of time.
 
   numViruses: number of ResistantVirus to create for patient (an integer)
   maxPop: maximum virus population for patient (an integer)
   maxBirthProb: Maximum reproduction probability (a float between 0-1)
   clearProb: maximum clearance probability (a float between 0-1)
   resistances: a dictionary of drugs that each ResistantVirus is resistant to
                (e.g., {'guttagonol': False})
   mutProb: mutation probability for each ResistantVirus particle
            (a float between 0-1).
   numTrials: number of simulation runs to execute (an integer)
 
   """
    total = [0. for x in xrange(300)]
    medicated = [0. for x in xrange(300)]
    for trial in range(numTrials):
        viruses = [ResistantVirus(maxBirthProb,clearProb,resistances,
                mutProb) for i in range(numViruses)]
        patient = TreatedPatient(viruses,maxPop)
        for sim in range(300):
            if sim > 149:
                patient.addPrescription('guttagonol')
            total[sim] += (patient.update())
            medicated[sim] += (float(patient.getResistPop(['guttagonol'])))
    total  =  [x /numTrials for x in total]
    medicated=[y /numTrials for y in medicated]
    #print(total,medicated)
    pylab.title("Treated patient simulation", color='red')
    pylab.xlabel("Time steps")
    pylab.ylabel("Average Virus Population", color='red')
    pylab.legend(loc="best")
    pylab.plot(total, color = 'black')
    pylab.plot(medicated)
    pylab.show()
 
 
simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol':False}, 0.005, 100)