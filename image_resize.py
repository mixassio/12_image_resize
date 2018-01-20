import os
import re
import argparse
from PIL import Image
import glob


def create_parser ():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath')
    parser.add_argument('-w', '--width', nargs='?', type=int)
    parser.add_argument('-he', '--height', nargs='?', type=int)
    parser.add_argument('-s', '--scale', nargs='?', type=float)
    parser.add_argument('-o', '--output', nargs='?')
    return parser


def parse_filepath(namespace):
    """
    Создание списка входящих файлов и имен (с директориями) под которыми нужно сохранить файлы
    :param namespace: аргументы коммандной строки
    :return: список кортежей filepath_in, filepath_out
    """
    my_path = os.path.abspath(namespace.filepath)
    # создаем список файлов для обработки
    if os.path.isdir(my_path):
        l = glob.glob('./*.*')  # список всех файлов в дирректории
        f = ['PNG', 'png', 'JPG', 'jpg', 'JPEG', 'jpeg']  # список расширений файлов, которые мы обрабатываем
        filepath_in = list(map( lambda x: os.path.join(os.path.abspath(x[1])), filter(lambda x: x[0] in f, map(lambda x: [re.findall('.+\.(\w+)', x)[0], x], l))))
    else:
        filepath_in = [my_path, ]
    # создаем список выходных названий файлов с путями
    if namespace.output:
        if os.path.exists(namespace.output) and os.path.isdir(namespace.output):
            filepath_out = []
            for file in filepath_in:
                dir_name, file_name = os.path.split(file)
                filepath_out.append(os.path.join(os.path.abspath(namespace.output), file_name))
        else:
            filepath_out = filepath_in
            print('no directory, files vill be save in current directory')
    else:
        filepath_out = filepath_in
    return list(zip(filepath_in, filepath_out))


def pic_scale(width, height, scale):
    return int(width*scale), int(height*scale)


def check_scale(width, height, new_width, new_height):
    """
    Проверяет введенные длинну и ширину на правильность пропорций
    :param width:
    :param height:
    :param new_width:
    :param new_height:
    :return: вывод в коммандную строку предупреждения
    """
    scale_h = new_height / height
    scale_w = new_width / width
    if scale_h != scale_w:
        print('Scale is broken. The picture is saved with changed proportions')


def pic_resize(width, height, new_width, new_height):
    """
    является вспомогательной функцией для new_proporcion(namespace, pic)
    Преобразует размеры картинки
    :param width:
    :param height:
    :param new_width:
    :param new_height:
    :return: новые размеры картинки
    """
    if new_width == 0:
        scale = new_height / height
    elif new_height == 0:
        scale = new_width / width
    new_width, new_height = pic_scale(width, height, scale)
    return new_width, new_height


def filepath_save(filepath, width, heigth, format):
    """
    Генерирует новое имя файла
    :param filepath:
    :param width:
    :param heigth:
    :param format:
    :return:
    """
    filepath = os.path.abspath(filepath)
    dir_name, file_name = os.path.split(filepath)
    name_file = re.findall('(\w*)\.', os.path.basename(file_name))
    return '{}/{}__{}x{}.{}'.format(dir_name, name_file[0], str(width), str(heigth), format)

def new_proporcion(namespace, pic):
    """
    Рассчитывает необходимые новые длину и ширину, распарсивая коммандную строку
    Переводчик коммандной строки
    :param namespace:
    :param pic:
    :return:
    """
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
    return new_width, new_height

if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    my_path = parse_filepath(namespace)
    for filepath_in, filepath_out in my_path:
        pic = Image.open(filepath_in)
        exif = pic.info['exif']
        new_width, new_height = new_proporcion(namespace, pic)
        new_im = pic.resize((new_width, new_height))
        save_filepath = filepath_save(filepath_out, new_im.width, new_im.height, pic.format)
        new_im.save(save_filepath, pic.format, exif=exif)
