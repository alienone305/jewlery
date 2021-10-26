
from PIL import Image

def convertImage():
    img = Image.open("logo.png")
    img = img.convert("RGBA")

    datas = img.getdata()

    newData = []

    for items in datas:

        if items[0] == 38 and items[1] == 38 and items[2] == 38:
            newData.append((255, 255, 255, 0))

        else:
            newData.append(items)
    img.putdata(newData)
    img.save("New.png", "PNG")
    print("Successful")

convertImage()
