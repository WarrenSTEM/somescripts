# 计算两张图片的互信息表征相似度
# 两张图片尺寸相同 一定程度上可以表征
# 当两幅图像相似度越高或重合部分越大时，其相关性也越大，联合熵越小，也即互信息越大
# https://blog.csdn.net/hujingshuang/article/details/47910949
from sklearn import metrics as mr
from imageio import imread
import numpy as np

image0 = imread('./pic/0.bmp')
image1 = imread('./pic/1.bmp')

# print(mr.mutual_info_score(image0, image1))  # wrong

# for RGB
# image1 = np.resize(image1, (image0.shape[0], image0.shape[1], image0.shape[2]))  # 调成一样的尺寸会让很多原来的信息丢失 难以把握

# (120, 120) -> (1, 14400)
# print(image0)
image0 = np.reshape(image0, -1)
image1 = np.reshape(image1, -1)
# print(image0)

# print(image0.shape)
# print(image1.shape)

mutual_info = mr.mutual_info_score(image0, image1)
norm_mutual_info = mr.normalized_mutual_info_score(image0, image1)

print("The mutual information between two pictures: ", mutual_info)
print("The normalized information between two pictures:", norm_mutual_info)