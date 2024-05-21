import argparse
from PIL import Image

class code :

    descStr = "This program converts an image into ASCII art."
    parser = argparse.ArgumentParser(description=descStr)
    parser.add_argument('--file', dest='filename', required=True)
    parser.add_argument('--width', dest='width', required=False)

    args = parser.parse_args()
    filename = args.filename

    new_width = 80
    if args.width:
        new_width = int(args.width)

    img = Image.open(filename)
    ASCII_CHARS = "@#S%?*+;:,."

    width, height = img.size
    ratio = height / width
    new_height = int(new_width * ratio)
    img = img.resize((new_width, new_height)).convert('L')

    txt = ""
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            gray = img.getpixel((x, y))
            txt += ASCII_CHARS[int(gray / 255 * (len(ASCII_CHARS)-1))]
        txt += '\n'
    print(txt)


if __name__ == '__main__':

    code()

