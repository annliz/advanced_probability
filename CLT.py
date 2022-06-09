# LINK TO DOC: https://docs.google.com/document/d/1f4ljPEMx-4P9lj5icFPetLsAn30AIrGosCVnljBIbTQ/edit?usp=sharing

import random
from matplotlib import pyplot as plt
import statistics
import math

N_SAMPLES = 300 # N in the problem
N_MEANS = 10000

def getUniformRandomNumber():
    return random.random()

def getExponentialRandomNumber():
    return random.expovariate(2)

def getBernoulliRandomNumber():
    return random.randint(0,1)

def getBetaRandomNumber():
    return random.betavariate(0.5,0.5)

def getSampleMean(N):
    sample = []
    for i in range(N):
        #sample.append(getUniformRandomNumber())
        #sample.append(getExponentialRandomNumber())
        #sample.append(getBernoulliRandomNumber())
        sample.append(getBetaRandomNumber())
    return sum(sample)/N

def printStats(l):
    print("Standard Deviation: " + str(statistics.stdev(l)))
    print("Variance: " + str(statistics.variance(l)))

def plotMeans(n):
    means = []
    for i in range(n):
        means.append(getSampleMean(N_SAMPLES))
    printStats(means)
    plt.hist(means, bins=100)
    plt.show()

plotMeans(N_MEANS)