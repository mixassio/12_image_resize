"""PIL.Image.open(fp, mode='r')
Opens and identifies the given image file.
This is a lazy operation; this function identifies the file, 
but the file remains open and the actual image data is not read from the file until you try to process the data 
(or call the load() method). See new().
Parameters:	
fp – A filename (string), pathlib.Path object or a file object. 
The file object must implement read(), seek(), and tell() methods, and be opened in binary mode.
mode – The mode. If given, this argument must be “r”.
Returns:	
An Image object.
Raises:	
IOError – If the file cannot be found, or the image cannot be opened and identified."""

from PIL import Image


"""Image.putdata(data, scale=1.0, offset=0.0)
Copies pixel data to this image. 
This method copies data from a sequence object into the image, 
starting at the upper left corner (0, 0), and continuing until either the image or the sequence ends. 
The scale and offset values are used to adjust the sequence values: pixel = value*scale + offset.
Parameters:	
data – A sequence object.
scale – An optional scale value. The default is 1.0.
offset – An optional offset value. The default is 0.0.
Returns:	
An Image object.

Image.resize(size, resample=0)
Returns a resized copy of this image.
Parameters:	
size – The requested size in pixels, as a 2-tuple: (width, height).
resample – An optional resampling filter. This can be one of PIL.Image.NEAREST, PIL.Image.BOX, PIL.Image.BILINEAR, PIL.Image.HAMMING, PIL.Image.BICUBIC or PIL.Image.LANCZOS. If omitted, or if the image has mode “1” or “P”, it is set PIL.Image.NEAREST. See: Filters.
Returns:	
An Image object.


Image.save(fp, format=None, **params)
Saves this image under the given filename. 
If no format is specified, the format to use is determined from the filename extension, if possible.
Keyword options can be used to provide additional instructions to the writer. 
If a writer doesn’t recognise an option, it is silently ignored. 
The available options are described in the image format documentation for each writer.
You can use a file object instead of a filename. 
In this case, you must always specify the format. 
The file object must implement the seek, tell, and write methods, and be opened in binary mode.
Parameters:	
fp – A filename (string), pathlib.Path object or file object.
format – Optional format override. If omitted, the format to use is determined from the filename extension. If a file object was used instead of a filename, this parameter should always be used.
options – Extra parameters to the image writer.
Returns:	
None

Raises:	
KeyError – If the output format could not be determined from the file name. Use the format option to solve this.
IOError – If the file could not be written. The file may have been created, and may contain partial data.
def resize_image(path_to_original, path_to_result):
    pass"""


if __name__ == '__main__':
    im = Image.open("./foto1.jpg")
    print(im.format, im.size, im.mode)
    im.show()

