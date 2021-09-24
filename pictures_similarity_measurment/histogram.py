# 直方图描述图像中的颜色全局分布
# 只能捕捉颜色信息的相似性
from PIL import Image
from numpy import linalg, dot
import numpy as np


def make_regular_image(image, size=(120, 120)):
    return image.resize(size).convert('RGB')


def hist_similarity(lh, rh):
    assert len(lh) == len(rh)
    # zip to tuple
    # return sum(1 - float(abs(l - r)) / max(l, r) for l, r in zip(lh, rh)) / len(lh)
    return sum(1 - (0 if l == r else float(abs(l - r)) / max(l, r)) for l, r in zip(lh, rh)) / len(lh)  # the same with above

# 需要归一化
def hist_l1_similarity(h0, h1):
    return linalg.norm(np.array(h0) - np.array(h1), 1)

def hist_l2_similarity(h0, h1):
    return linalg.norm(np.array(h0) - np.array(h1), 2)

def hist_cosine_similarity(h0, h1):
    ah0 = np.array(h0)
    ah1 = np.array(h1)
    len0 = linalg.norm(ah0, 2)
    len1 = linalg.norm(ah1, 2)
    return dot(ah0, ah1) / (len0 * len1)



def calc_similarity(li, ri):
    return hist_similarity(li.histogram(), ri.histogram())


# for RGB
# image0 = make_regular_image(Image.open('./pic/0.bmp'))
# image1 = make_regular_image(Image.open('./pic/1.bmp'))

# image0 = Image.open('./pic/0.bmp')
# image1 = Image.open('./pic/1.bmp')
image0 = Image.open('./test_bmp/0.bmp').convert('L')
image1 = Image.open('./test_bmp/1.bmp').convert('L')
# image1.show()
hist = calc_similarity(image0, image1)

# for debug
"""
print(type(image0))
print(image0)
print(image0.histogram())
print(len(image0.histogram()))
print(type(image0.histogram()))
# img_RGB = image0.convert('RGB')
# img_RGB.show()
h0 = image0.histogram()
h1 = image1.histogram()
print(hist_l1_similarity(h0, h1))
print(hist_cosine_similarity(h0, h1))
"""

print("The histogram similarity: ", hist)
