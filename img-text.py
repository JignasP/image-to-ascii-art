
from PIL import Image

class code :


    filename = "sad.jpg"

    img = Image.open(filename)
    ASCII_CHARS = "@#S%?*+;:,."
    new_width=120
    width, height = img.size
    ratio = height / width
    new_height = int(new_width * ratio)
    img = img.resize((new_width, new_height)).convert('L')



    txt = ""
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            gray = img.getpixel((x, y))
            txt += ASCII_CHARS[int(gray / 255 * 10)]
        txt += '\n'
    print(txt)


if __name__ == '__main__':

    code()

