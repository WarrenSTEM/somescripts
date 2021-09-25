# for (120, 120, 4)-png
# firstly, convert to ('L')
from PIL import Image
from numpy import average, linalg, dot
import os
import numpy as np


def cosine(image0_list, image0_norm, image1_list, image1_norm):
    return dot(image0_list, image1_list) / (image0_norm * image1_norm)


def histogram(hist0, hist1):
    assert len(hist0) == len(hist1)
    return sum(1 - (0 if l == r else float(abs(l - r)) / max(l, r)) for l, r in zip(hist0, hist1)) / len(hist0)


def file_batch4cosine(pictures_path, pictures_files, idx0, idx1):
    former_path = os.path.join(pictures_path, pictures_files[idx0])
    later_path = os.path.join(pictures_path, pictures_files[idx1])
    img0 = Image.open(former_path).convert('L')
    img1 = Image.open(later_path).convert('L')
    img0_list = list(img0.getdata())
    img1_list = list(img1.getdata())
    img0_norm = linalg.norm(img0_list, 2)
    img1_norm = linalg.norm(img1_list, 2)
    temp_cosine = cosine(img0_list, img0_norm, img1_list, img1_norm)
    # cosine_similarity.append(temp_cosine)
    # print(cosine_similarity)
    return temp_cosine


def file_batch4hist(pictures_path, pictures_files, idx0, idx1):
    former_path = os.path.join(pictures_path, pictures_files[idx0])
    later_path = os.path.join(pictures_path, pictures_files[idx1])
    img0 = Image.open(former_path).convert('L')
    img1 = Image.open(later_path).convert('L')
    h0 = img0.histogram()
    h1 = img1.histogram()
    temp_histogram = histogram(h0, h1)
    return temp_histogram


def image_similarity_vectors_via_numpy(image0, image1):
    # print("1")
    # print(len(image1.getdata()))

    images = [image0.convert('L'), image1.convert('L')]
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


def for_debug():
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
    pictures.sort(key=lambda x: int(x.split('.')[0]))
    print(pictures)
    cosine_similarity = []
    for i in range(2):
        former_path = os.path.join(pic_path, pictures[i])
        later_path = os.path.join(pic_path, pictures[i + 1])
        # print(former_path)
        # print(later_path)
        img0 = Image.open(former_path)
        img1 = Image.open(later_path)
        temp_cosine = image_similarity_vectors_via_numpy(img0, img1)
        # print(temp_cosine)
        cosine_similarity.append(temp_cosine)
    print(cosine_similarity)


if __name__ == "__main__":
    """
    path0 = './test/0.png'
    path1 = './test/1.png'
    image0 = Image.open(path0).convert('L')
    image1 = Image.open(path1)
    print(image0)  # RGBA
    print(type(image0))
    print(image0.getdata()[0])  # (2, 2, 2, 255)
    print(len(image0.getdata()))  # 120 * 120
    # image0 = image0.convert('L')
    image1 = image1.convert('L')
    print(image0)
    print(type(image0))
    print(image0.getdata()[0])  # 2
    print(len(image0.getdata()))  # 14400
    # 每一张图都和第一张比较 i.e. img0 始终为 0.png
    img_list = list(image0.getdata())
    print(img_list)
    print(max(img_list))  # 255

    img0_list = list(image0.getdata())
    img1_list = list(image1.getdata())
    print(dot(img0_list, img1_list))
    img0_norm = linalg.norm(img0_list, 2)
    img1_norm = linalg.norm(img1_list, 2)
    print(dot(img0_list, img1_list) / (img0_norm * img1_norm))  # a little difference with consin.py (just precision）
    print(dot(np.array(img1_list), np.array(img0_list)) / (img0_norm * img1_norm))  # the same with above
    for_debug()

    pic_path = './test'
    pictures = os.listdir(pic_path)
    pictures.sort(key=lambda x: int(x.split('.')[0]))
    cosine_similarity = []
    mode = 0
    final_point = 1000  # 比较图片数目
    # mode = 0: 任意指定两张图比较
    # mode = 1: 每一张图都和第一张比较 i.e. img0 始终为 0.png
    # mode = 2: 每一张图和前一张比较
    img_idx0 = 0
    img_idx1 = 1

    if mode == 0:
        # former_path = os.path.join(pic_path, pictures[img_idx0])
        # later_path = os.path.join(pic_path, pictures[img_idx1])
        # img0 = Image.open(former_path).convert('L')
        # img1 = Image.open(later_path).convert('L')
        # img0_list = list(img0.getdata())
        # img1_list = list(img1.getdata())
        # img0_norm = linalg.norm(img0_list, 2)
        # img1_norm = linalg.norm(img1_list, 2)
        # temp_cosine = cosine(img0_list, img0_norm, img1_list, img1_norm)
        # cosine_similarity.append(temp_cosine)
        # print(cosine_similarity)
        element_cosine = file_batch4cosine(pic_path, pictures, img_idx0, img_idx1)
        cosine_similarity.append(element_cosine)
        print(cosine_similarity)
    elif mode == 1:
        for i in range(final_point - 1):
            element_cosine = file_batch4cosine(pic_path, pictures, 0, i + 1)
            cosine_similarity.append(element_cosine)
            print(cosine_similarity)
    else:
        # mode == 2
        for i in range(final_point - 1):
            element_cosine = file_batch4cosine(pic_path, pictures, i, i + 1)
            cosine_similarity.append(element_cosine)
            print(cosine_similarity)
    """
    img0 = Image.open('./test/0.png').convert('L')
    img1 = Image.open('./test/8.png').convert('L')
    #img0.show()
    #img0 = Image.open('./test/0.png')
    #img1 = Image.open('./test/1.png')
    # img0.show()
    h0 = img0.histogram()
    h1 = img1.histogram()
    print(h0)
    # print(type(h0))  # list
    print(h1)
    print(len(h0))
    print(len(h1))
    temp_histogram = histogram(h0, h1)
    print(temp_histogram)
    image0 = Image.open('./pic/0.bmp')
    # image0.show()
    image1 = Image.open('./pic/1.bmp')
    H0 = image0.histogram()
    H1 = image1.histogram()
    print(H0)
    print(H1)
    print(len(H0))
    print(len(H1))
    print(histogram(H0, H1))

