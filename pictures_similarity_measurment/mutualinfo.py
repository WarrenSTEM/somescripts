from sklearn import metrics as mr
from imageio import imread
import numpy as np

image0 = imread('./pic/0.bmp')
image1 = imread('./pic/1.bmp')

image1 = np.resize(image1, (image0.shape[0], image0.shape[1], image0.shape[2]))

image0 = np.reshape(image0, -1)
image1 = np.reshape(image1, -1)

print(image0.shape)
print(image1.shape)

mutual_info = mr.mutual_info_score(image0, image1)

print(mutual_info)