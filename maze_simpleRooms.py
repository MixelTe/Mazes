roomCount = 10
ansCount = 0

print("Вы находитесь в пещере")
while roomCount > 0:
    roomCount -= 1
    if ansCount % 2 == 0:
        print('Вы находитесь на развилке. Вы можете пойти "налево" или "направо". \
Введите одно из слов в кавычках для выбора.')
        ans = input()

        # beginning of changes
        while (ans != "налево" and ans != "направо"):
            print('Вы ввели что-то не то. \
Пожалуйста введите ещё раз. Вы можете ввести: "налево" или "направо"')
            ans = input()
        # end of changes

        if ans == "налево":
            print("Вы направились налево")
            ansCount += 1
        elif ans == "направо":
            print("Вы направились направо")
            ansCount += 2
        else:
            print("Error!")
            roomCount = -1
    else:
        print('Вы находитесь на развилке. Вы можете пойти "налево", "направо" или "прямо". \
Введите одно из слов в кавычках для выбора.')
        ans = input()

        # beginning of changes
        while (ans != "налево" and ans != "направо" and ans != "прямо"):
            print('Вы ввели что-то не то. \
Пожалуйста введите ещё раз. Вы можете ввести: "налево", "направо" или "прямо"')
            ans = input()
        # end of changes

        if ans == "налево":
            print("Вы направились налево")
            ansCount += 1
        elif ans == "направо":
            print("Вы направились направо")
            ansCount += 2
        elif ans == "прямо":
            print("Вы направились прямо")
            ansCount += 3
        else:
            print("Error!")
            roomCount = -1
if roomCount != -1:
    print("Вы смело прошли все развилки.")

    if ansCount % 2 == 0:
        print("Но за ней вас подстерегала гигантская подземная жаба, \
которая проглотила вас целиком!")
    else:
        print("И нашли огромный сундук с сокровищами!")
