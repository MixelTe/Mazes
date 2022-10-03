from PIL import Image, ImageDraw
CellSize = 30


def drawMap(filePath, imagePath):
    w, h, level = readMap(filePath)
    im = Image.new("RGB", (w * CellSize, h * CellSize), (0, 0, 0))
    drawer = ImageDraw.Draw(im)
    for y in range(h):
        for x in range(w):
            i = y * w + x
            cell = level[i]
            drawCell(x * CellSize, y * CellSize, cell, drawer)
    im.save(imagePath)


def drawCell(x, y, cell, drawer):
    if (cell == "#"):
        drawer.rectangle(((x, y), (x + CellSize, y + CellSize)), (255, 255, 255))
    elif (cell == "*"):
        drawer.rectangle(((x, y), (x + CellSize, y + CellSize)), (255, 255, 0))
    elif (cell == "$"):
        drawer.rectangle(((x, y), (x + CellSize, y + CellSize)), (150, 150, 150))
    elif (cell == "&"):
        drawer.rectangle(((x, y), (x + CellSize, y + CellSize)), (255, 0, 255))
    elif (cell == "^"):
        drawer.rectangle(((x, y), (x + CellSize, y + CellSize)), (0, 255, 0))
    elif (cell == "%"):
        drawer.rectangle(((x, y), (x + CellSize, y + CellSize)), (255, 0, 0))
    elif (cell == "@"):
        drawer.rectangle(((x, y), (x + CellSize, y + CellSize)), (0, 0  , 255))

def readMap(filePath):
    f = open(filePath, encoding="UTF-8")
    w, h = [int(n) for n in f.readline().split()]
    level = list(f.readline())
    f.close()
    return w, h, level


drawMap(r"D:\Users\Lux\Desktop\python\mazes\mazeForAnswer\maps\map2.txt", r"D:\Users\Lux\Desktop\python\mazes\mazeForAnswer\maps\map2.png")