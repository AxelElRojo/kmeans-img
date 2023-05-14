#!/bin/python
import numpy as np
import matplotlib.pyplot as plt
import cv2, sys
if len(sys.argv) != 4:
	print("Usage: \"{} <clusters> <image> <output>\"".format(sys.argv[0]))
else:
	image = cv2.cvtColor(cv2.imread(sys.argv[2]), cv2.COLOR_BGR2RGB)
	pixVals = np.float32(image.reshape((-1,3)))
	criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.85)
	retval, labels, centers = cv2.kmeans(pixVals, int(sys.argv[1]), None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
	centers = np.uint8(centers)
	segData = centers[labels.flatten()]
	segImg = segData.reshape((image.shape))
	plt.axis('off')
	plt.imshow(segImg)
	plt.imsave(sys.argv[3], segImg)