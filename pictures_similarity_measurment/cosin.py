# 将图片表示成一个向量 通过计算向量之间的余弦距离表征相似度
from PIL import Image
from numpy import average, linalg, dot
import os

# 缩放并转换为灰度图
def get_thumbnail(image, size=(120, 120), greyscale=True):
    # image = image.resize(size, Image.ANTIALIAS)  # 带ANTIALIAS滤镜高质量缩放
    if greyscale:
        image = image.convert('L')  # 转换为灰度图像 0为黑 255为白
    return image


def image_similarity_vectors_via_numpy(image0, image1):
    image0 = get_thumbnail(image0)
    image1 = get_thumbnail(image1)
    # print("1")
    # print(len(image1.getdata()))

    images = [image0, image1]
    vectors = []
    norms = []
    for image in images:
        vector = []
        num = 0
        for pixel_tuple in image.getdata():
            if pixel_tuple > 10:
                # print(pixel_tuple)
                num += 1
            vector.append(average(pixel_tuple))  # guess for RGB tuple
        vectors.append(vector)
        norms.append(linalg.norm(vector, 2))  # 向量2范数

    a, b = vectors  # a = v1, b = v2
    a_norm, b_norm = norms  # a_norm = ||v1|| b_norm = ||v2|| 向量长度
    # print(num)
    return dot(a / a_norm, b / b_norm)


# path0 = './pic/0.bmp'
# path1 = './pic/1.bmp'
path0 = './test/0.png'
path1 = './test/1.png'

# "path" should be the dictionary path
"""
files1 = os.listdir(path1)  # list all files in the dictionary
# find the most similar picture
lst_data = []
for root, dirs, files in os.walk(path0):
    for file in files:
        image0 = Image.open(os.path.join(root, file))
        for f in files1:
            image1 = Image.open(os.path.join(path1, f))
            cosin = image_similarity_vectors_via_numpy(image0, image1)
            lst_data.append(cosin)

print(lst_data)
print(min(lst_data))
print(max(lst_data))
"""

image0 = Image.open(path0)
image1 = Image.open(path1)

# for debug
"""
print(len(image0.getdata()))  # 120 * 120
pixel_vec = []
pixel_avg = []
for pixel in image0.getdata():
    # print(type(pixel), ":", pixel)
    pixel_vec.append(pixel)
    pixel_avg.append(average(pixel))
print(pixel_vec)
print(pixel_avg)
"""
cosine = image_similarity_vectors_via_numpy(image0, image1)
print("The cosine similarity: ", cosine)

pic_path = './test'
pictures = os.listdir(pic_path)
pictures.sort(key=lambda x:int(x.split('.')[0]))
print(pictures)
cosine_similarity = []
for i in range(99):
    former_path = os.path.join(pic_path, pictures[2])
    later_path = os.path.join(pic_path, pictures[i + 1])
    # print(former_path)
    # print(later_path)
    img0 = Image.open(former_path)
    img1 = Image.open(later_path)
    temp_cosine = image_similarity_vectors_via_numpy(img0, img1)
    # print(temp_cosine)
    cosine_similarity.append(temp_cosine)
print(cosine_similarity)
