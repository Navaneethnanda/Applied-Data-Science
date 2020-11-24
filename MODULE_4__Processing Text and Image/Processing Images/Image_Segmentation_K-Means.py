# Color Image Segmentation with K-Means Algorithm & OpenCV

'''
K-Means Clustering in OpenCV
Goal : Learn to use cv2.kmeans() function in OpenCV for data clustering

Understanding Parameters

Input parameters
samples : It should be of np.float32 data type, and each feature should be put in a single column.
nclusters(K) : Number of clusters required at end

criteria : It is the iteration termination criteria. When this criteria is satisfied, algorithm iteration stops. Actually, it should be a tuple of 3 parameters. They are ( type, max_iter, epsilon ):
3.a - type of termination criteria : It has 3 flags as below:
cv2.TERM_CRITERIA_EPS - stop the algorithm iteration if specified accuracy, epsilon, is reached. cv2.TERM_CRITERIA_MAX_ITER - stop the algorithm after the specified number of iterations, max_iter. cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER - stop the iteration when any of the above condition is met.
3.b - max_iter - An integer specifying maximum number of iterations.
3.c - epsilon - Required accuracy
attempts : Flag to specify the number of times the algorithm is executed using different initial labellings. The algorithm returns the labels that yield the best compactness. This compactness is returned as output.

flags : This flag is used to specify how initial centers are taken. Normally two flags are used for this : cv2.KMEANS_PP_CENTERS and cv2.KMEANS_RANDOM_CENTERS.

Output parameters

compactness : It is the sum of squared distance from each point to their corresponding centers.
labels : This is the label array (same as ‘code’ in previous article) where each element marked ‘0’, ‘1’.....
centers : This is array of centers of clusters.

'''


import numpy as np
import cv2

# Select the input image
img = cv2.imread('HappyFish.jpg')
#img = cv2.imread('Lena.tiff')
#img = cv2.imread('Night.jpg')

Z = img.reshape((-1,3))

# Convert to np.float32
Z = np.float32(Z)

# Define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

# How many clusters?
K = 5

ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res = res.reshape((img.shape))


# Display Results
cv2.imshow('Original', img)
cv2.imshow('Result: k=12', res)

cv2.waitKey(0)
cv2.destroyAllWindows()

