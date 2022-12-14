import random

MAX_ROOM = 10000
MAX_DOOR = 50
ROOM_GOOD_RESULT_CHANCE = 1
CORRECT_PASSWORD_CHANCE = 5
CLOSED_DOOR_CHANCE = 3
EXIT_CHANCE = 100
NO_DOOR_CHANCE = 100


class RoomAction:

    def __init__(self, action, goodResult, badResult):
        self.action = action
        self.goodResult = goodResult
        self.badResult = badResult

    def Act(self):
        if (random.randint(0, ROOM_GOOD_RESULT_CHANCE) == 0):
            print(self.goodResult)
        else:
            print(self.badResult)

roomEvents = [
    "В этой комнате очень темно",
    "В этой комнате сидит троль",
    "В этой комнате нет пола",
    "В этой комнате много тыкв",
    "Вы не знаете, что в этой комнате",
    "В этой комнате ничего нет",
    "Зловещая Темнота насмехается над вами",
    "Посередине комнаты лежит крокодил, кажется, что он спит",
    "Вы находитесь на поляне со стенами",
    "Стены комнаты медленно движутся",
    "Потолок комнаты постоянно падает вам на голову и вам уже это надоело",
    "Мимо вас пронёсся грозный суслик",
    "Четыре камня стоят по углам комнаты",
    "В этой комнате пожар",
    "Вы нашли ключ, но решили его не брать, чтобы не будить Злых Духов",
    "Вы встретили самого себя. Оказалось, это было просто зеркало",
    "Часы пробили полночь, но возможно, полдень",
    "Часы пробили стену, вы решили держаться от них подальше",
    "Вы увидели НЛО, но оно не увидело вас",
    "Вы нашли ежа, а ёж нашел вас",
    "С потолка комнаты свисает лоза",
    "В углу комнаты сидит паук",
    "В соседней комнате что-то очень громко хлопнуло",
    "Посередине комнаты стоит памятник вам. \033[2mХорошее же у вас воображение, ведь там просто камень\033[0m",
    "На полу лежит карта лабиринта, но вы, как истиный искатель приключений, даже не взглянули на неё",
    "На стене висит карта этой комнаты, вы поняли, что это комната имеет форму квадрата",
    "Вы вспомнили, что забыли выключить чайник, но это вас не остановило",
    "Вы вспомнили, что забыли выключить утюг, но это вас не остановило",
    "Вы встретили своего друга, но это оказался мираж",
    "Вы в пустыне. Это оказались фото-обои, вы в комнате",
    "Зазвенел будильник и вы проснулись у себя дома. Это оказался сон, вы всё ещё в лабиринте",
    "Эта комната заминирована",
    "В этой комнате работает бригада бобров",
    "Вся комната увешана часами",
    "Посередине комнаты глубокая яма",
    "По комнате летает Неизвестный Дух",
    # "",
]

roomActions = [
    RoomAction("Надеть шапку-невидимку", "Шапка-невидимка вам очень помогла", "Шапка-невидимка не сработала!"),
    RoomAction("Поднять меч", "Это был очень мощный меч, теперь всё хорошо", "Вы подняли меч, но он сломался, не повезло"),
    RoomAction("Съесть яблоко", "Теперь вы сыты и довольны", "Яблоко оказалось очень кислым, из-за чего вы упали в обморок на 3 часа"),
    RoomAction("Спрятаться", "В ближайшем кусте вы спокойно переждали все беды", "Вы не нашли куда спрятаться"),
    RoomAction("Притвориться тенью", "Теперь вас точно никто не заметит", "Не повезло, тень притворилась вами"),
    RoomAction("Прилечь поспать", "Сон прибавил вам сил", "Пока вы спали, на вас стали падать камни, вы еле-еле спаслись"),
    RoomAction("Крикнуть как можно громче", "Все проблемы испугались так, что исчезли", "Вы остолбенели от эха вашего крика"),
    RoomAction("Кинуть камень", "Вы попали прямо в цель!", "Вы промахнулись"),
    RoomAction("В бешенстве топнуть ногой", "Все, кто вас видел, разбежались в испуге", "Теперь у вас очень сильно болит нога."),
    RoomAction("Воспользоваться луком", "Вы выстрелили из лука и попали", "Лук оказался горький, теперь вы хотите пить"),
    RoomAction("Побежать как можно быстрее", "Вы убежали от проблем", "Вы прибежали неизвестно куда"),
    RoomAction("Нажать большую красную кнопку", "Прилетели спасатели и переместили вас в соседнюю комнату", "Вы услышали обратный отсчёт"),
    RoomAction("Взять огнетушитель", "Вы потушили всю комнату, теперь она тушеная", "Вы не знаете, как пользоваться огнетушителем"),
    RoomAction("Позвонить спасателем", "Спасатели скоро прибудут. \033[2m(Когда пройдут этот лабиринт)\033[0m", "Здесь нет связи"),
    RoomAction("Заказать пиццу", "Вы сели за стол и стали наслаждаться пиццей", "К сожалению, курьер заблудился в этом лабиринте"),
    RoomAction("Отобедать как цивилизованный человек", "Вы накрыли стол и начали приём пищи", "К сожалению, вы не нашли свечи"),
    RoomAction("Вызвать НЛО", "НЛО прилетело и воодушевило вас", "Вы получили такой ответ от НЛО: \033[35m$%3@#*&_+fge%5#@\033[0m"),
    RoomAction("Посмотреть на компас", "Стрелка на компасе постоянно крутится", "Вы не нашли компас в своих карманах"),
    RoomAction("Позвонить в поддержку", "Вас поддержали", "Все операторы заняты"),
    RoomAction("Сообщить об ошибке", "\033[2mСпасибо за отзыв, мы обязательно учтём ваши пожелания\033[0m", "Вы отправили сообщение об ошибке"),
    RoomAction("Наколдовать выход", "Вы забыли, как это делать", "Вы забыли, что не умеете колдовать"),
    RoomAction("Попросить подсказку", "Вы получили подсказку", "Вы получили бесполезную подсказку"),
    RoomAction("Сделать привал", "Вы в полном здравии, можете продолжать путь", "Вы уснули и пропустили обед"),
    RoomAction("Попросить помощь у друга", "Друг вас морально поддержал", "Теперь ваш друг тоже ходит по этому лабиринту"),
    RoomAction("Войти в портал к выходу", "Вы оказались у выхода предыдущей комнаты", "Вы оказались у входа в эту комнату"),
    RoomAction("Снять доспехи", "Сняв доспехи, вы почувствовали лёгкость во всём теле", "Вы стали делать движения, похожие на то, что вы снимаете доспехи \033[2mВы выглядите очень смешно\033[0m"),
    RoomAction("Съесть банан", "Теперь вы можете идти дальше", "Вы подскользулись на шкурке от этого банана"),
    RoomAction("Биться об стену", "Стена пожалела вас и немного отодвинулась", "Обеспокоенный \033[2mНадсмоторщик\033[0m Лабиринта вколол вам успокоительное"),
    RoomAction("Использовать чит-код", "Вы были полностью исцелены", "Вас ударило по голове"),
    RoomAction("Выстрелить", "Вы подошли к пушке и зарядили её, очнувшись, вы решили, что всё хорошо", "Вы подошли к пушке, но не нашли ядра"),
    RoomAction("Ткнуть пальцем в небо", "Вы почувствовали слабый ветерок", "На вас упал кусочек облака"),
    RoomAction("Ткнуть пальцем в небо", "Теперь в небе дырка", "Пошел дождь"),
    RoomAction("Взять мега-меч", "Теперь в одном из ваших карманов лежит мега-меч \033[2mВряд ли вы его там найдёте\033[0m", "Вы не смогли его поднять"),
    RoomAction("Включить свет", "Теперь всё стало хорошо видно", "Вы не нашлы выключатель"),
    RoomAction("Позвать на помощь", "К вам прилетел Блуждающий Дух", "Никто не отозвался"),
    RoomAction("Нагнать ужаса", "Все вокруг теперь в ужасе", "Теперь вы в ужасе"),
    RoomAction("Взять с пола ключ", "На ключе написанно, что он не подходит ни к одной двери. Вы выбросили ключ", "Ключ оказался приклеен к полу"),
    RoomAction("Применить воображение", "Вы вообразили проход в другую комнату и прошли через него", "Вы вообразили двери"),
    RoomAction("Спрыгнуть с обрыва", "Вы попали в другую комнату", "Неведомая Сила подняла вас обратно"),
    RoomAction("Съесть таблетку", "Вы уснули на 2 часа, но теперь вы полны сил", "Теперь вы видите Невидимых Духов"),
    RoomAction("Выпить зелье", "Ваша сила увеличена на две минуты", "Вы замедлены на две минуты"),
    RoomAction("Применить супер-силу", "\033[2mЭто действие не предусмотрено\033[0m", "У вас нет супер-силы"),
    RoomAction("Воскликнуть 'Ура!' три раза", "Теперь у вас хорошее настроение", "Стены стали косо смотреть на вас"),
    RoomAction("Сдаться", "Вы сдались, но игра продолжается", "\033[2mВаше действие отменено\033[0m"),
    # RoomAction("", "", ""),
]


def ToNextRoom():
    doors = random.randint(2, MAX_DOOR)
    print("Количество дверей перед вами:", doors)
    print("Введите номер двери, в которую вы хотите войти")
    doorOpen = 0
    while doorOpen == 0:
        door = int(input())
        while door < 1 or door > doors:
            print("Вы ввели номер двери которой не существует")
            print("Введите номер двери от 1 до", doors)
            door = int(input())
        doorOpen = random.randint(0, CLOSED_DOOR_CHANCE)
        if (doorOpen == 0):
            print("Эта дверь оказалась заперта, а ключа у вас нет, попробуйте другую")
        elif (doorOpen == 1):
            PasswordDoor()

    print("Вы вошли в дверь №", door)

def PasswordDoor():
    print("На двери оказался кодовый замок")
    doorOpened = False
    print("Введите пароль")
    attemptCount = 0
    while not doorOpened:
        attemptCount += 1
        input()
        doorOpened = random.randint(0, CORRECT_PASSWORD_CHANCE) == 0
        if (not doorOpened):
            print("Вы ввели неправильный пароль")
            if (attemptCount >= 3):
                print("Подсказка: пароль содержит 15 разных цифр 5 разных букв и 2 знака препинания")
            if (attemptCount >= 5 and attemptCount < 8):
                print("Вы должны вводить пароль настойчивей!")
            elif (attemptCount >= 8 and attemptCount < 10):
                print("Даже у Великих ДвереОткрывателей не всегда получается с первого раза!")
            elif (attemptCount == 10):
                print("Попробуйте свой пароль от холодильника")
            elif (attemptCount >= 11):
                print("Подсказка: зар ёще етйуборпоП")
            print("Попробуйте ещё раз")


def ClearRow():
    print("\33[1F                                                                                                         \33[1F")
    # print("\33[2F                                                                                                         ")
    # print("\33[2F")

def InTheRoom():
    event = roomEvents[random.randint(0, len(roomEvents) - 1)]
    # event = roomEvents[len(roomEvents) - 1]
    actions = []
    for i in range(3):
        action = roomActions[random.randint(0, len(roomActions) - 1)]
        actions.append(action)
    # actions[2] = roomActions[len(roomActions) - 1]
    print(event)
    print("Вы можете:")

    for i in range(3):
        print(str(i + 1) + ":", actions[i].action)
    action = -1
    print("Что будете делать? Введите номер действия")
    while action != 0 and action != 1 and action != 2:
        action = int(input()) - 1
        ClearRow()
    print(action + 1)

    actions[action].Act()



print("Вы в лабиринте")
room = random.randint(1, EXIT_CHANCE)

while room > 0:
    print()
    roomNumber = random.randint(1, MAX_ROOM)
    print("Вы в комнате №", roomNumber)

    InTheRoom()

    room = random.randint(0, EXIT_CHANCE)
    noDoors = random.randint(0, NO_DOOR_CHANCE)
    if (noDoors == 0):
        room = -1
    else:
        ToNextRoom()

if (room == 0):
    print("Поздравляю, вы вышли из лабиринта!")
else:
    print("Вы попали в комнату без дверей и погибли там с голоду.")

# seed = (8253729 * seed + 2396403)
# rnd = int((seed % 32768) / 32768)
