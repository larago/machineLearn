# encoding=utf8

from numpy import *
import operator 

def createDataSet():
    group = array([[1.0, 2.0], [1.2, 0.1], [0.1, 1.4], [0.3, 3.5]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def classify(input, dataSet, label, k):
    dataSize = dataSet.shape[0]
    diff = tile(input, (dataSize, 1)) - dataSet
    sqDiff = diff ** 2
    squareDist = sum(sqDiff, axis = 1)
    dist = squareDist ** 0.5
    sortedDistIndex = argsort(dist)
    
    classCount = dict()
    for i in range(k):
        voteLabel = label[sortedDistIndex[i]]
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1
    
    maxCount = 0
    for key, val in classCount.items():
        if val > maxCount:
            maxCount = val
            classes = key

    return classes


if __name__ == '__main__':
    group, labels = createDataSet()
    print classify([1.1, 0.3], group, labels, 3)