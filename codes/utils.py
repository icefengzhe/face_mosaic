import cv2
from PIL import Image
import numpy as np


def save_img(img, fn):
    # print(fn)
    try:
        cv2.imwrite(fn, img)
    except cv2.error as e:
        print("处理失败: ", str(fn), e)


def motify_ext(fn, ext_s, ext_d):
    if fn.suffix == ext_s:
        fn_m = fn.with_suffix(ext_d)
        fn.rename(fn_m)
        return fn_m
    else:
        return fn


def rotate_img(fn, k):
    img, fn = load_img(fn)
    if k:
        img = np.rot90(img, k).copy()
    return img, fn


def load_img(fn):
    try:
        if fn.suffix == '.gif':
            img = Image.open(str(fn))
            img = np.array(img.convert('RGB'))
            fn = fn.with_suffix('.jpg')
        else:
            img = cv2.imread(str(fn))
    except IOError:
        print(f'暂不支持{fn.suffix}格式数据')
    return img, fn