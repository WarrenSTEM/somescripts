# structural similarity
## 在实际应用中 利用滑动窗口将图像分块 令分块数为N
## 考虑到窗口形状对分块的影响 采用高斯加权计算每一个窗口的均值、方差及协方差
## 然后计算对应块的结构相似度SSIM 最后将平均值作为两图像的结构相似性度量

# from skimage.measure import compare_ssim
from skimage.metrics import structural_similarity
# from scipy.misc import imread
# https://blog.csdn.net/zz2230633069/article/details/82706120
from imageio import imread
import numpy as np

from PIL import Image
from SSIM_PIL import compare_ssim

# image read in the method of array: <class 'imageio.core.util.Array'>
# image0 = imread('./pic/0.bmp')
# image1 = imread('./pic/1.bmp')
#
image0 = imread('./test/0.png')[:, :, 0]
image1 = imread('./test/4.png')[:, :, 0]

# 0, 1, 2 same
# print(image1[:, :, 0])
# print(image1[:, :, 1])
# print(image1[:, :, 2])
# print(image1[:, :, 3])
# for debug
"""
print(type(image0))
"""

# image1 = np.resize(image1, (image0.shape[0], image0.shape[1], image0.shape[2]))  # guess for RGB

print(image0.shape)
print(image1.shape)

ssim = structural_similarity(image0, image1, multichannel=False)

print("The mean structural similarity: ", ssim)
# print(structural_similarity(image0, image1, multichannel=True))

# img0 = Image.open('./pic/0.bmp')
# img1 = Image.open('./pic/1.bmp')
img0 = Image.open('./test/0.png').convert('L')
img1 = Image.open('./test/2.png').convert('L')

print(compare_ssim(img0, img1))
img0 = Image.open('./test/0.png')
img1 = Image.open('./test/1.png')
print(compare_ssim(img0, img1))

# image0 = imread('./pic/0.bmp')
# image1 = imread('./pic/1.bmp')
