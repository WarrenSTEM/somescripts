import os
from imageio import imread
import numpy as np


def cosine(path0, path1):
    # img0 = imread(path0).reshape(1, -1)  # [[...]]
    # img1 = imread(path1)
    # img1 = np.reshape(img1, -1)  # [...]
    # print(img0)
    # print(img1)
    img0 = np.reshape(imread(path0), -1)
    img1 = np.reshape(imread(path1), -1)

    img0_len = np.linalg.norm(img0, 2)
    img1_len = np.linalg.norm(img1, 2)

    return np.dot(img0, img1) / (img0_len * img1_len)

def ssim(path0, path1):
    return 1.0

def hist(path0, path1):
    return 1.0

def mulinfo(path0, path1):
    return 1.0

pic_path = "./pic"
# print(os.listdir(path))
pictures = os.listdir(pic_path)
# print(pictures[0])
# print(type(pictures[0]))
# print(len(pictures))
cosine_similarity = []
for i in range(len(pictures) - 1):
    former_path = os.path.join(pic_path, pictures[i])
    later_path = os.path.join(pic_path, pictures[i + 1])
    temp_cosine = cosine(former_path, later_path)
    cosine_similarity.append(temp_cosine)


# for file in os.listdir(path):
    #  此文件下要求全为图片文件
