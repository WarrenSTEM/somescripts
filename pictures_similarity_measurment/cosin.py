from PIL import Image
from numpy import average, linalg, dot
import os


def get_thumbnail(image, size=(120, 120), greyscale=False):
    image = image.resize(size, Image.ANTIALIAS)
    if greyscale:
        image = image.convert('L')
    return image


def image_similarity_vectors_via_numpy(image0, image1):
    image0 = get_thumbnail(image0)
    image1 = get_thumbnail(image1)
    images = [image0, image1]
    vectors = []
    norms = []
    for image in images:
        vector = []
        for pixel_tuple in image.getdata():
            vector.append(average(pixel_tuple))
        vectors.append(vector)
        norms.append(linalg.norm(vector, 2))

    a, b = vectors
    a_norm, b_norm = norms
    return dot(a / a_norm, b / b_norm)


path0 = './pic/0.bmp'
path1 = './pic/1.bmp'
files1 = os.listdir(path1)

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
