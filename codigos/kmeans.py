import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("nina.jpg")

image1 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

pixel_values = image1.reshape((-1, 3))
pixel_values = np.float32(pixel_values)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)

k = 10
_, labels, (centers) = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

centers = np.uint8(centers)

labels = labels.flatten()

segmented_image = centers[labels.flatten()]

segmented_image = segmented_image.reshape(image1.shape)

plt.subplot(211),plt.imshow(image1)
plt.title('Image Original'), plt.xticks([]), plt.yticks([])
plt.subplot(212),plt.imshow(segmented_image)
plt.title('Image Segmentée'), plt.xticks([]), plt.yticks([])
plt.show()