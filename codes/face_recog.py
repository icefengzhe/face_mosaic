import cv2
import numpy as np
import face_recognition
from pathlib import Path


def _face_recog(image, count):
    if count == 0:
        k = 0
        image_ = image
    elif count == 1:
        k = -1
        image_ = np.rot90(image, k).copy()
    elif count == 2:
        k = 1
        image_ = np.rot90(image, k).copy()
    elif count == 3:
        return None, 0
    face_locations = face_recognition.face_locations(image_)
    if not face_locations:
        return _face_recog(image, count + 1)
    else:
        return face_locations, k


def face_recog(fn):
    count = 0
    fn = Path(fn)
    try:
        image = face_recognition.load_image_file(fn)
        return _face_recog(image, count)
    except IOError:
        print(f'暂不支持{fn.suffix}数据格式')
        return None, 0


if __name__ == '__main__':
    fn = r'D:\fzworks\Desensitization_IDCard\data\1\0ec5d1dd-822d-49ba-b91e-068651ee1ac6-2020-07-26-09-07-46.jpg'
    a = face_recog(fn)
    print(a)
