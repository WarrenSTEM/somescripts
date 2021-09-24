from PIL import Image

def make_regular_image(image, size = (120, 120)):
    return image.resize(size).convert('RGB')

def hist_similarity(lh, rh):
    assert len(lh) == len(rh)
    return sum(1 - float(abs(l - r)) / max(l, r) for l, r in zip(lh, rh)) / len(lh)

def calc_similarity(li, ri):
    return hist_similarity(li.histogram(), ri.histogram())

image0 = make_regular_image(Image.open('./pic/0.bmp'))
image1 = make_regular_image(Image.open('./pic/1.bmp'))
print(calc_similarity(image0, image1))