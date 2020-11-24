'''
OpenCV comes with a data file, letter-recognition.data

If you open it, you will see 20000 lines which may, on first sight, look like garbage.
Actually, in each row, first column is an alphabet which is our label.
Next 16 numbers following it are its different features.
These features are obtained from UCI Machine Learning Repository. 

There are 20000 samples available, so we take first 10000 data as training samples
and remaining 10000 as test samples.
We should change the alphabets to ascii characters because we can’t work with alphabets directly.

'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the data, converters convert the letter to a number
data= np.loadtxt('letter-recognition.data', dtype= 'float32', delimiter = ',',
                    converters= {0: lambda ch: ord(ch)-ord('A')})

# split the data to two, 10000 each for train and test
train, test = np.vsplit(data,2)

# split trainData and testData to features and responses
responses, trainData = np.hsplit(train,[1])
labels, testData = np.hsplit(test,[1])

# Initiate the kNN, classify, measure accuracy.
knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE, responses)

# Test
ret, result, neighbours, dist = knn.findNearest(testData, k=5)

correct = np.count_nonzero(result == labels)
accuracy = correct*100.0/10000
print (accuracy)


