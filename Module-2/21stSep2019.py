import numpy

def listToNDArray():
    list = [1,2,3,4]
    list2 = [1,2,3,4]
    list2 = numpy.array(list2)

    list = numpy.array(list)

    return list*list2

def arrayOfZeros():
     return numpy.zeros(1000)

def arrayOfOnes():
    return numpy.ones(3)

def arrayOfEmpty():
    return numpy.empty(10)

def numPyArange():
    return numpy.arange(10)

print(listToNDArray())
print(arrayOfZeros())
print(arrayOfOnes().shape)
print(arrayOfEmpty())
print(numPyArange())