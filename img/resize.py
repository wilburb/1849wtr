from PIL import Image
import os, sys

path = ('.')

def resize():
    for item in os.listdir(path):
        if os.path.isfile(item):
            try:
                im = Image.open(item)
                f, e = os.path.splitext(item)
                imResize = im.resize((400,300), Image.ANTIALIAS)
                imResize.save(f + '-300x400.png', 'PNG', quality=90)
            except IOError:
                print item
resize()
