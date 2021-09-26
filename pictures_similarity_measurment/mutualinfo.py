# 计算两张图片的互信息表征相似度
# 两张图片尺寸相同 一定程度上可以表征
# 当两幅图像相似度越高或重合部分越大时，其相关性也越大，联合熵越小，也即互信息越大
# https://blog.csdn.net/hujingshuang/article/details/47910949
from sklearn import metrics as mr
from imageio import imread
import numpy as np

from PIL import Image

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
print("The normalized information between two pictures:", norm_mutual_info)  # 1 -> the same

# img0 = Image.open('./pic/0.bmp')
# img1 = Image.open('./pic/1.bmp')
# # print(list(img0))
# img0 = np.array(img0.getdata())
# # array(img0) 120 * 120
# # array(img0.getdata()) 1 * 14400
# img1 = np.array(img1.getdata())
# print(len(img0))
# print(img0)
# print(mr.mutual_info_score(img0, img1))
# print(mr.normalized_mutual_info_score(img0, img1))  # same with above

# img0 = Image.open('./test/998.png').convert('L')
# img1 = Image.open('./test/999.png').convert('L')
# # print(list(img0))
# img0 = np.array(img0.getdata())
# # array(img0) 120 * 120
# # array(img0.getdata()) 1 * 14400
# img1 = np.array(img1.getdata())
# print(len(img0))
# print(img0)
# print(mr.mutual_info_score(img0, img1))
# print(mr.normalized_mutual_info_score(img0, img1))  # same with above

img0 = Image.open('./test/0.png').convert('L')
img1 = Image.open('./test/999.png').convert('L')
img0 = np.array(img0.getdata())
for i in range(1, 20):
    img1 = Image.open('./test/{}.png'.format(i)).convert('L')
    # print('./test/{}.png'.format(i))
    img1 = np.array(img1.getdata())
    print(mr.normalized_mutual_info_score(img0, img1), end=' ')

