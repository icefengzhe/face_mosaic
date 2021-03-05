import os

import click
from pathlib import Path
from codes.face_recog import face_recog
from codes.mask_face import do_mosaic
from codes.utils import save_img, rotate_img

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('path', type=click.Path(exists=True))
@click.option('-o', '--out_dir', type=click.Path(), default=None, show_default=True, help='结果保存路径，默认为./run')

def main(path, out_dir):
    """图片头像批量打码.

    \b
    path: 要打码的图片的路径
    """

    for root, dirs, files in os.walk(path):
        for file in files:
            fn = Path(root, file)
            face_locations, k = face_recog(fn)
            img, fn = rotate_img(fn, k)

            if face_locations:
                print('locations: ', face_locations)
                for face_location in face_locations:
                    do_mosaic(img, face_location)
            if not out_dir:
                out_dir = 'run'
            Path(out_dir, fn.parent).mkdir(parents=True, exist_ok=True)
            fn = Path(out_dir, fn.parent, fn.name)

            save_img(img, str(fn))


if __name__ == '__main__':
    main()
