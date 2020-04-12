from PIL import Image, ImageDraw
import sys

indirectory = '/Users/subhayan/Projects/python/orig/'
outdirectory = '/Users/subhayan/Projects/python/edited/'

origImag = indirectory + "Screenshot.png"

RED = "#ff0000"

def main():
    try:
        im = Image.open(origImag)
        filenamecounter = 1
        outImage = ''

        x1 = 580
        y1 = 1000
        x3 = 960

        for i in range(x1, x3, 40):
            draw = ImageDraw.Draw(im)
            x4 = x1 + filenamecounter*40
            draw.line([x1, y1, x4, y1], width=10, fill=RED)
            outImage = outdirectory + "Image" + '{:03d}'.format(filenamecounter) + ".png"
            # im.show()
            im.save(outImage)
            filenamecounter += 1

        x1 = 1020
        y1 = 1000
        x3 = 1400
        anothercounter = 1
        im = Image.open(outImage)

        for i in range(x1, x3, 40):
            draw = ImageDraw.Draw(im)
            x4 = x1 + anothercounter*40
            draw.line([x1, y1, x4, y1], width=10, fill=RED)
            outImage = outdirectory + "Image" + '{:03d}'.format(filenamecounter) + ".png"
            # im.show()
            im.save(outImage)
            filenamecounter += 1
            anothercounter += 1

        x1 = 1480
        y1 = 1000
        x3 = 1840
        anothercounter = 1
        im = Image.open(outImage)

        for i in range(x1, x3, 40):
            draw = ImageDraw.Draw(im)
            x4 = x1 + anothercounter*40
            draw.line([x1, y1, x4, y1], width=10, fill=RED)
            outImage = outdirectory + "Image" + '{:03d}'.format(filenamecounter) + ".png"
            # im.show()
            im.save(outImage)
            filenamecounter += 1
            anothercounter += 1

        x1 = 1940
        y1 = 1000
        x3 = 2260
        anothercounter = 1
        im = Image.open(outImage)

        for i in range(x1, x3, 40):
            draw = ImageDraw.Draw(im)
            x4 = x1 + anothercounter*40
            draw.line([x1, y1, x4, y1], width=10, fill=RED)
            outImage = outdirectory + "Image" + '{:03d}'.format(filenamecounter) + ".png"
            # im.show()
            im.save(outImage)
            filenamecounter += 1
            anothercounter += 1

        x1 = 580
        y1 = 1550
        x3 = 960
        anothercounter = 1
        im = Image.open(outImage)

        for i in range(x1, x3, 40):
            draw = ImageDraw.Draw(im)
            x4 = x1 + anothercounter*40
            draw.line([x1, y1, x4, y1], width=10, fill=RED)
            outImage = outdirectory + "Image" + '{:03d}'.format(filenamecounter) + ".png"
            # im.show()
            im.save(outImage)
            filenamecounter += 1
            anothercounter += 1

        x1 = 1020
        y1 = 1550
        x3 = 1400
        anothercounter = 1
        im = Image.open(outImage)

        for i in range(x1, x3, 40):
            draw = ImageDraw.Draw(im)
            x4 = x1 + anothercounter*40
            draw.line([x1, y1, x4, y1], width=10, fill=RED)
            outImage = outdirectory + "Image" + '{:03d}'.format(filenamecounter) + ".png"
            # im.show()
            im.save(outImage)
            filenamecounter += 1
            anothercounter += 1

        x1 = 1480
        y1 = 1550
        x3 = 1840
        anothercounter = 1
        im = Image.open(outImage)

        for i in range(x1, x3, 40):
            draw = ImageDraw.Draw(im)
            x4 = x1 + anothercounter*40
            draw.line([x1, y1, x4, y1], width=10, fill=RED)
            outImage = outdirectory + "Image" + '{:03d}'.format(filenamecounter) + ".png"
            # im.show()
            im.save(outImage)
            filenamecounter += 1
            anothercounter += 1

        x1 = 1940
        y1 = 1550
        x3 = 2260 
        anothercounter = 1
        im = Image.open(outImage)

        for i in range(x1, x3, 40):
            draw = ImageDraw.Draw(im)
            x4 = x1 + anothercounter*40
            draw.line([x1, y1, x4, y1], width=10, fill=RED)
            outImage = outdirectory + "Image" + '{:03d}'.format(filenamecounter) + ".png"
            # im.show()
            im.save(outImage)
            filenamecounter += 1
            anothercounter += 1

    except IOError as e:
        print("IO Error ")
        print(e)
        pass


if __name__ == "__main__":
    main() 
