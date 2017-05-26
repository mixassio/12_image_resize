# Image resize

The script is designed to resize the image. With the help of the script you will be able to:
1. Zoom the picture (zoom in or out)
2. Change the length or width while saving the scaling.
3. Change the length and width with the loss of scaling
The file is saved in the same folder (by default) or by specifying the -o flag in the selected folder
The name of the final file will be pic__200x400.jpg where pic is the name of the source file and 200x400 is the total size.

# How use

Example of script launch on Linux, Python 3.5:

usage: image_resize.py [-height int] [-width int] [-scale int] [-output 'filepath_new'] filepath

```#!bash

$ python image_resize.py ./foto.jpeg -w 400

#
```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
