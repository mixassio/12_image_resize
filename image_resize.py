import os
import re
import argparse
from PIL import Image



def create_parser ():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath')
    parser.add_argument('-w', '--width', nargs='?', type=int)
    parser.add_argument('-he', '--height', nargs='?', type=int)
    parser.add_argument('-s', '--scale', nargs='?', type=float)
    parser.add_argument('-o', '--output', nargs='?')
    return parser


def parse_filepath(namespace):
    filepath_in = os.path.abspath(namespace.filepath)
    dir_name, file_name = os.path.split(filepath_in)
    if namespace.output:
        if os.path.exists(namespace.output):
            filepath_out = os.path.abspath(namespace.output) + '/' + file_name
        else:
            filepath_out = filepath_in
    else:
        filepath_out = filepath_in
    return filepath_in, filepath_out


def pic_scale(width, height, scale):
    print(width, height, scale)
    return int(width*scale), int(height*scale)


def check_scale(width, height, new_width, new_height):
    scale_h = new_height / height
    scale_w = new_width / width
    if scale_h != scale_w:
        print('Scale is broken. The picture is saved with changed proportions')


def pic_resize(width, height, new_width, new_height):
    if new_width == 0:
        scale = new_height / height
        new_width, new_height = pic_scale(width, height, scale)
    elif new_height == 0:
        scale = new_width / width
        new_width, new_height = pic_scale(width, height, scale)
    return new_width, new_height


def filepath_save(filepath, width, heigth, format):
    filepath = os.path.abspath(filepath)
    dir_name, file_name = os.path.split(filepath)
    name_file = re.findall('(\w*)\.', os.path.basename(file_name))
    return dir_name + '/' + name_file[0] + '__' + str(width) + 'x' + str(heigth) +'.' + format


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()

    filepath_in, filepath_out = parse_filepath(namespace)
    pic = Image.open(filepath_in)

    print(pic.format, pic.size, pic.mode)

    if namespace.scale:
        new_width, new_height = pic_scale(pic.width, pic.height, namespace.scale)
    elif namespace.width and namespace.height:
        check_scale(pic.width, pic.height, namespace.width, namespace.height)
        new_width, new_height = namespace.width, namespace.height
    elif namespace.width:
        new_width, new_height = pic_resize(pic.width, pic.height, namespace.width, 0)
    elif namespace.height:
        new_width, new_height = pic_resize(pic.width, pic.height, 0, namespace.height)
    else:
        print('You did not enter anything. The program did nothing')

    new_im = pic.resize((new_width, new_height))
    save_filepath = filepath_save(filepath_out, new_im.width, new_im.height, pic.format)
    new_im.save(save_filepath, pic.format)


