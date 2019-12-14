import numpy
from matplotlib import pyplot


def gen2(p0, shape0, scale0, shape1, scale1):
    ah = numpy.random.binomial(n=1, p=p0, size=(10000,))
    pep0 = numpy.random.gamma(shape=shape0, scale=scale0, size=(10000,))
    pep1 = numpy.random.gamma(shape=shape1, scale=scale1, size=(10000,))
    pep0_ah = ah == 0
    pep1_ah = ah == 1
    res = numpy.concatenate((pep0[pep0_ah], pep1[pep1_ah]), axis=0)
    
    y,binEdges=numpy.histogram(res,bins=100,density=True)
    bincenters = 0.5*(binEdges[1:]+binEdges[:-1])    
    
    pyplot.plot(bincenters,y,'b-')
    
    return res
