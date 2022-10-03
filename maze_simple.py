seed = 4541
MAX_ROOM = 10000
MAX_DOOR = 50
EXIT_CHANCE = 20
CLOSED_DOOR_CHANCE = 4
NO_DOOR_CHANCE = 20

print("Вы в лабиринте")

seed = (8253729 * seed + 2396403)
room = int((seed % 32768) / 32768 * EXIT_CHANCE)

while room > 0:
    print()
    seed = (8253729 * seed + 2396403)
    roomNumber = int((seed % 32768) / 32768 * MAX_ROOM)

    print("Вы в комнате №", roomNumber)

    seed = (8253729 * seed + 2396403)
    room = int((seed % 32768) / 32768 * EXIT_CHANCE)

    seed = (8253729 * seed + 2396403)
    noDoors = int((seed % 32768) / 32768 * NO_DOOR_CHANCE)
    if (noDoors == 0):
        room = -1
    else:
        seed = (8253729 * seed + 2396403)
        doors = int((seed % 32768) / 32768 * MAX_DOOR) + 2
        print("Количество дверей перед вами:", doors)
        print("Введите номер двери, в которую вы хотите войти")

        doorOpen = 0
        while doorOpen == 0:
            door = int(input())
            while door < 1 or door > doors:
                print("Вы ввели номер двери которой не существует")
                print("Введите номер двери от 1 до", doors)
                door = int(input())
            seed = (8253729 * seed + 2396403)
            doorOpen = int((seed % 32768) / 32768 * CLOSED_DOOR_CHANCE)
            if (doorOpen == 0):
                print("Эта дверь оказалась заперта, а ключа у вас нет, попробуйте другую")
        print("Вы вошли в дверь №", door)


if (room == 0):
    print("Поздравляю, вы вышли из лабиринта!")
else:
    print("Вы попали в комнату без дверей и погибли там с голоду.")

# seed = (8253729 * seed + 2396403)
# rnd = int((seed % 32768) / 32768)
