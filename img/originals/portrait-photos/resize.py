from PIL import Image
import os, sys

path = ('.')

def resize():
    for item in os.listdir(path):
        if os.path.isfile(item):
            try:
                im = Image.open(item)
                f, e = os.path.splitext(item)
                imResize = im.resize((300,400), Image.ANTIALIAS)
                imResize.save(f + '-400x300.png', 'PNG', quality=90)
            except IOError:
                print item
resize()
