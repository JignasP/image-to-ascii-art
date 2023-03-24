# https://www.geeksforgeeks.org/converting-image-ascii-image-python/

import sys, random, argparse
import numpy as np
import math
from PIL import Image

class code :

    def __init__(self):
        pass

    global img
    global ASCII_CHARS

    filename = "tux.png"
    orgimg = Image.open(filename)
    img = Image.open(filename).convert('L')
    img.show()
    ASCII_CHARS = "@#S%?*+;:,."


    im = np.array(img)
    w, h = im.shape
    getAverageL= im.reshape(w * h)




    W, H = img.size[0], img.size[1]
    print("input image dims: %d x %d" % (W, H))
    scale = 1
    cols = 10
    w = W / cols
    h = w / scale
    rows = int(H / h)
    print("cols: %d, rows: %d" % (cols, rows))
    print("tile dims: %d x %d" % (w, h))

    if cols > W or rows > H:
        print("Image too small.")
        exit()

    aimg = []
    for j in range(rows):
        y1 = int(j * h)
        y2 = int((j + 1) * h)

        if j == rows - 1:
            y2 = H

        aimg.append("")

        for i in range(cols):
            x1 = int(i * w)
            x2 = int((i + 1) * w)
            if i == cols - 1:
                x2 = W

            image = img.crop((x1, y1, x2, y2))
            avg = int(getAverageL[i])
            print(j,i)
            print (avg)
            gsval = ASCII_CHARS[int((avg * 11) / 255)]

        #       for f in range(aimg.index(aimg[-1]) + 1):
        #           print(aimg[f])
            aimg[j] += gsval
    for f in range (j):
        print (aimg[f])


if __name__ == '__main__':

    code()
