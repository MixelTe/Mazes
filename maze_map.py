import time


class Level:

    def __init__(self, width, height, level):
        self.width = width
        self.height = height
        self.level = level
        self.useMap = False
        self.mapFullyOpen = False

    def Print(self):
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                row += self.level[y * self.height + x]
                row += " "
            print(row)

    def PrintWithCoords(self, character):
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                if (x == character.x and y == character.y):
                    row += "+"
                else:
                    row += self.level[y * self.height + x]
                row += " "
            print(row)

    def PrintWithDirections(self):
        afterLines = [
            "/-----------------------------\\",
            "| * - старт                   |",
            "| _ - стена или пропасть      |",
            "| # - комната                 |",
            "| $ - комната, разрушаемая    |",
            "| & - ключ                    |",
            "| ^ - хороший выход           |",
            "| % - плохой выход            |",
            "| @ - закрытая дверь          |",
            "\\-----------------------------/",
        ]
        shift = self.width - 3
        print("       " + shift * " " + "север" + shift * " ")
        for y in range(self.height):
            row = "       "
            if (y == self.height // 2):
                row = "запад  "
            for x in range(self.width):
                row += self.level[y * self.height + x]
                row += " "
            if (y == self.height // 2):
                row += "  восток"
                if (y < len(afterLines)):
                    row += "  " + afterLines[y]
            elif (y < len(afterLines)):
                row += "          " + afterLines[y]
            print(row)
        print("        " + shift * " " + "юг" + shift * " ")

    def PrintWithDirectionsAndCoords(self, character):
        afterLines = [
            "/-----------------------------\\",
            "| + - вы тут                  |",
            "| _ - стена или пропасть      |",
            "| # - комната                 |",
            "| $ - комната, разрушаемая    |",
            "| & - ключ                    |",
            "| ^ - хороший выход           |",
            "| % - плохой выход            |",
            "| @ - закрытая дверь          |",
            "\\-----------------------------/",
        ]
        shift = self.width - 3
        print("       " + shift * " " + "север" + shift * " ")
        for y in range(self.height):
            row = "       "
            if (y == self.height // 2):
                row = "запад  "
            for x in range(self.width):
                if (x == character.x and y == character.y):
                    row += "+"
                else:
                    row += self.level[y * self.height + x]
                row += " "
            if (y == self.height // 2):
                row += "  восток"
                if (y < len(afterLines)):
                    row += "  " + afterLines[y]
            elif (y < len(afterLines)):
                row += "          " + afterLines[y]
            print(row)
        print("        " + shift * " " + "юг" + shift * " ")

    def PrintMarks(self):
        print("* - старт")
        print("_ - стена")
        print("# - комната")
        print("$ - комната, разрушается после выходе из неё")
        print("& - ключ")
        print("^ - хороший выход")
        print("% - плохой выход")
        print("@ - закрытая дверь")


class Room:
    def __init__(self, x, y, level, character):
        self.x = x
        self.y = y
        self.level = level
        self.character = character

    def Action(self):
        room = level.level[self.y * level.height + self.x]
        if (room == "*" or room == "#" or room == "$" or room == "@"):
            print("Вы вошли в комнату и внимательно её осмотрели...")
            print("...")
            time.sleep(1.5)
            print("В этой комнате вы не нашли ничего интересного")
        elif (room == "&"):
            self.character.keys += 1
            print("Вы вошли в комнату и внимательно её осмотрели...")
            print("...")
            time.sleep(2)
            print("Вы нашли Ключ!")
            print("Теперь у вас ключей:", self.character.keys)
        elif (room == "^"):
            print("Как только вы вошли в комнату, \
вы увидели яркий свет, вы подходите ближе...")
            print("...")
            time.sleep(3)
            print("Это выход!")
            print("Но как только вы подошли ближе...")
            time.sleep(3)
            print("На вас стали падать золотые монеты!")
            print("Вы взяли мешок и стали собрать монеты...")
            print("...")
            time.sleep(4)
            print("Собрав целый мешок вы вышли из лабиринта!")
            self.character.finished = True
        elif (room == "%"):
            print("Как только вы вошли в комнату, \
вы увидели яркий свет, вы подходите ближе...")
            print("...")
            time.sleep(3)
            print("Это выход!")
            print("Но как только вы подошли ближе...")
            time.sleep(3)
            print("На вас стали падать золотые монеты!")
            print("Вы взяли мешок и стали собрать монеты...")
            print("...")
            time.sleep(4)
            print("Собрав целый мешок вы направились к выходу...")
            time.sleep(2)
            print("Но внезапно пол обрушился и вы упали в бездну.")
            self.character.finished = True
        else:
            print("К сожалению, \
духи этого места не захотели, чтобы вы вышли из лабиринта")
            print("Вы оказались на островке посередине бездонной ямы")
            self.character.finished = True

        if (not self.character.finished):
            self.ToNextRoom()

    def ToNextRoom(self):
        I_room_up = (self.y - 1) * level.height + self.x
        I_room_down = (self.y + 1) * level.height + self.x
        I_room_left = self.y * level.height + self.x - 1
        I_room_right = self.y * level.height + self.x + 1
        room_up = "_"
        room_down = "_"
        room_left = "_"
        room_right = "_"
        directions = []
        if (self.y > 0):
            room_up = level.level[I_room_up]
        if (self.y < level.height - 1):
            room_down = level.level[I_room_down]
        if (self.x > 0):
            room_left = level.level[I_room_left]
        if (self.x < level.width - 1):
            room_right = level.level[I_room_right]

        if (self.CheckRoom(room_up)):
            directions.append("север")
            if (self.character.map.map[I_room_up] == "_"):
                self.character.map.map[I_room_up] = "?"
        if (self.CheckRoom(room_down)):
            directions.append("юг")
            if (self.character.map.map[I_room_down] == "_"):
                self.character.map.map[I_room_down] = "?"
        if (self.CheckRoom(room_left)):
            directions.append("запад")
            if (self.character.map.map[I_room_left] == "_"):
                self.character.map.map[I_room_left] = "?"
        if (self.CheckRoom(room_right)):
            directions.append("восток")
            if (self.character.map.map[I_room_right] == "_"):
                self.character.map.map[I_room_right] = "?"

        closedDoors = []
        if (room_up == "@"):
            closedDoors.append("север")
            self.character.map.map[I_room_up] = level.level[I_room_up]
        if (room_down == "@"):
            closedDoors.append("юг")
            self.character.map.map[I_room_down] = level.level[I_room_down]
        if (room_left == "@"):
            closedDoors.append("запад")
            self.character.map.map[I_room_left] = level.level[I_room_left]
        if (room_right == "@"):
            closedDoors.append("восток")
            self.character.map.map[I_room_right] = level.level[I_room_right]

        if (len(closedDoors) > 0):
            doorsCount = len(closedDoors)
            if (doorsCount == 1):
                print("В этой комнате один путь загораживает дверь")
            else:
                print("В этой комнате несколько путей загораживают двери")
            if (len(closedDoors) == 1):
                print("Перед вами закрытая \
дверь в направлении:", '"' + closedDoors[0] + '"')
            else:
                d = ""
                for door in closedDoors:
                    d += '"' + door + '" '
                print("Перед вами закрытые двери в направлениях:", d)
            print("У вас ключей:", self.character.keys)

        self.MoveToNextRoom(directions)

    def CheckRoom(self, room):
        if (room == "*" or room == "#" or
           room == "$" or room == "&" or room == "^" or room == "%"):
            return True
        if (room == "@" and self.character.keys > 0):
            return True
        return False

    def MoveToNextRoom(self, directions):
        self.PrintMessageForMoving(directions)
        userInput = input()
        for _ in range(20):
            print()
        while userInput not in directions:
            if (userInput == "ключи"):
                print("У вас ключей:", self.character.keys)
            elif (self.level.useMap and userInput == "карта"):
                if (self.level.mapFullyOpen):
                    level.PrintWithDirectionsAndCoords(self.character)
                else:
                    self.character.PrintMap()
            else:
                print("Вы ввели что-то не то...")
            self.PrintMessageForMoving(directions)
            userInput = input()
            for _ in range(20):
                print()

        if (userInput == "север"):
            self.character.y -= 1
        elif (userInput == "юг"):
            self.character.y += 1
        elif (userInput == "запад"):
            self.character.x -= 1
        elif (userInput == "восток"):
            self.character.x += 1

        print("Вы переместились в направлении:", userInput)
        self.PastRoomAction()

    def PrintMessageForMoving(self, directions):
        d = ""
        for direction in directions:
            d += '"' + direction + '" '
        print()
        print("------------------------------")
        print("Вы можете пойти в направлениях:", d)
        print('Введете одно из слов в кавычках, \
чтобы перейти в этом направлении')
        print('Также вы можете ввести "ключи" \
для проверки количества ваших ключей')
        if (self.level.useMap):
            print('Для просмотра карты введите "карта"')

    def PastRoomAction(self):
        roomIndex = self.y * level.height + self.x
        room = level.level[roomIndex]
        if (room == "$"):
            print("Только вы вышли из комнаты и вдруг...")
            time.sleep(1)
            print("Началось сильное землятресение и эта комната обрушилась!")
            time.sleep(2)
            print("Вы успели перейти в следующею комнату!")
            level.level[roomIndex] = "_"
        elif (room == "&" or room == "*"):
            level.level[roomIndex] = "#"
        elif (room == "@"):
            level.level[roomIndex] = "#"
            self.character.keys -= 1

        self.character.map.map[roomIndex] = level.level[roomIndex]


class CharacterMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = ["_" for x in range(height * width)]

    def Print(self, character):
        afterLines = [
            "/-----------------------------\\",
            "| + - вы тут                  |",
            "| ? - неисследованная комната |",
            "| _ - стена или пропасть      |",
            "| # - комната                 |",
            "| @ - закрытая дверь          |",
            "\\----------------------------/",
        ]
        shift = self.width - 3
        print("       " + shift * " " + "север" + shift * " ")
        for y in range(self.height):
            row = "       "
            if (y == self.height // 2):
                row = "запад  "
            for x in range(self.width):
                if (x == character.x and y == character.y):
                    row += "+"
                else:
                    row += self.map[y * self.height + x]
                row += " "
            if (y == self.height // 2):
                row += "  восток"
                if (y < len(afterLines)):
                    row += "  " + afterLines[y]
            elif (y < len(afterLines)):
                row += "          " + afterLines[y]
            print(row)
        print("        " + shift * " " + "юг" + shift * " ")


class Character:
    def __init__(self, level):
        self.level = level
        self.finished = False
        self.keys = 0
        startPoint = level.level.index("*")
        self.x = startPoint % level.width
        self.y = (startPoint - self.x) // level.height
        self.map = CharacterMap(level.width, level.height)

    def NextTurn(self):
        room = Room(self.x, self.y, self.level, self)
        room.Action()

    def PrintMap(self):
        self.map.Print(self)


# * - start
# _ - wall
# # - room
# $ - room, destroy after exit
# & - key
# ^ - good exit
# % - bad exit
# @ - close door

level = Level(10, 10, [
    "#", "#", "#", "^", "_", "_", "_", "&", "_", "_",
    "@", "_", "#", "_", "&", "_", "_", "#", "_", "$",
    "#", "#", "$", "_", "#", "_", "#", "#", "#", "@",
    "#", "_", "_", "_", "#", "#", "#", "_", "#", "_",
    "#", "$", "_", "&", "#", "_", "#", "_", "#", "_",
    "#", "_", "_", "_", "#", "_", "#", "$", "#", "#",
    "@", "_", "#", "#", "#", "_", "&", "_", "_", "@",
    "#", "_", "#", "_", "#", "_", "_", "&", "#", "#",
    "#", "#", "#", "_", "#", "_", "%", "_", "_", "#",
    "_", "_", "$", "_", "*", "_", "#", "@", "#", "#",
])
character = Character(level)
# level.PrintMarks()
# level.Print()

printMapAfterTurn = False

print("Несколько настроек перед игрой:")
mapMode = ""
while mapMode != "1" and mapMode != "2" and mapMode != "3":
    print("Как вы хотите видеть карту лабиринта:")
    print("1: Я буду рисовать карту на бумажке (для любителей лабиринтов)")
    print("2: Пусть карта будет рисоваться сама (для обычных людей)")
    print("3: Я хочу видеть карту полностью с самого начала \
(не рекомендуется для первого раза)")
    print("Введете номер ответа (1, 2 или 3)")
    mapMode = input()
if (mapMode == "2"):
    level.useMap = True
elif (mapMode == "3"):
    level.useMap = True
    level.mapFullyOpen = True
if (level.useMap):
    printMap = ""
    while printMap != "да" and printMap != "нет":
        print("Выводить ли карту на экран после каждого хода:")
        print("да: Я хочу всегда знать, где я")
        print('нет: Я буду пользоваться командой "карта"')
        print("Введете вариант ответа (да или нет)")
        printMap = input()
    if (printMap == "да"):
        printMapAfterTurn = True

print("Для комфортной игры в экран должна влезать эта фигура:")
print("/----\\")
for _ in range(32):
    print("|    |")
print("\\----/")
print("Для комфортной игры в экран должна влезать эта фигура")
print("Введите что-либо для продолжения")
input()
for _ in range(32):
    print()

print("Игра начинается")
print()
print("------------------------------")
print("Вы находитесь в лабиринте")
print("Ваша цель выбраться из него")
if (level.mapFullyOpen):
    print("Карта лабиринта:")
    level.PrintWithDirections()

while (not character.finished):
    print()
    print("------------------------------")
    print()
    character.NextTurn()
    if (printMapAfterTurn):
        if (level.mapFullyOpen):
            level.PrintWithDirectionsAndCoords(character)
        else:
            character.PrintMap()

print()
print("------------------------------")
print()
print("Конец игры.")
