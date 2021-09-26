# 直方图描述图像中的颜色全局分布
# 只能捕捉颜色信息的相似性
from PIL import Image
from numpy import linalg, dot
import numpy as np
import matplotlib.pyplot as plt


def hist_similarity(lh, rh):
    assert len(lh) == len(rh)
    # zip to tuple
    # return sum(1 - float(abs(l - r)) / max(l, r) for l, r in zip(lh, rh)) / len(lh)
    return sum(1 - (0 if l == r else float(abs(l - r)) / max(l, r)) for l, r in zip(lh, rh)) / len(
        lh)  # the same with above


image0 = Image.open('./pic/0.bmp')
image1 = Image.open('./pic/1.bmp')
img0 = Image.open('./test/0.png')
img1 = Image.open('./test/1.png').convert('L')

# plt.figure("IMG0")
# al0 = np.array(image0).flatten()
# print(len(al0))
# plt.hist(al0, bins = 120, edgecolor = 'red', facecolor = 'red')
# plt.show()

# plt.figure("IMG")
# al0 = np.array(image0).flatten()
# print(al0[0:100])
#
# plt.hist(al0, bins=256, edgecolor = 'red', facecolor = 'red')
# plt.show()

r, g, b, a = img0.split()
plt.figure("IMG")
# al0 = np.array(img1).flatten()
# print(len(al0))
ar = np.array(r).flatten()
plt.hist(ar, bins=256, edgecolor='red', facecolor='red')
ag = np.array(g).flatten()
plt.hist(ag, bins=256, edgecolor='green', facecolor='green')
ab = np.array(b).flatten()
plt.hist(ab, bins=256, edgecolor='blue', facecolor='blue')
aa = np.array(a).flatten()
plt.hist(aa, bins=256, edgecolor='black', facecolor='black')
plt.show()
