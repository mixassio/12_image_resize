import os
import argparse
from PIL import Image



def create_parser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('filepath')
    parser.add_argument ('-w', '--width', nargs='?', type=int)
    parser.add_argument ('-h', '--height', nargs='?', type=int)
    parser.add_argument ('-s', '--scale', nargs='?', type=float)
    parser.add_argument ('-o', '--output', nargs='?')
    return parser


def parse_filepath(namespace):
    filepath_in = namespace.filepath
    if namespace.output:
        if os.path.exists(namespace.output):
            filepath_out = namespace.filepath
        else:
            filepath_out = filepath_in
    else:
        filepath_out = filepath_in
    return filepath_in, filepath_out


def pic_scale(width, height, scale):
    return int(width*scale), int(height*scale)


def check_scale(width, height, new_width, new_height):
    # TODO
    print('Scale is broken. The picture is saved with changed proportions')

def pic_resize(width, height, new_width=0, new_height=0):


    return new_width, new_height








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
        new_width, new_height = pic_resize(pic.width, pic.height, namespace.width)
    elif namespace.height:
        new_width, new_height = pic_resize(pic.width, pic.height, namespace.height)
    else:
        print('You did not enter anything. The program did nothing')

    new_im = pic.resize((new_width, new_height))
    new_im.save(filepath_out, pic.format)


