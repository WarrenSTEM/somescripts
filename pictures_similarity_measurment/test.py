# for (120, 120, 4)-png
# firstly, convert to ('L')
from PIL import Image
from numpy import average, linalg, dot
import os
import numpy as np


def cosine(image0_list, image0_norm, image1_list, image1_norm):
    return dot(image0_list, image1_list) / (image0_norm * image1_norm)


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


if __name__ == "__main__":
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
