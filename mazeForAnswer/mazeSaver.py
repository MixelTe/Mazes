from random import choice
letters = [
    "А", "Б", "В", "Г", "Д", "Е", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р",
    "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я", "а", "б",
    "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т",
    "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", "A", "B", "C", "D",
    "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
    "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
    "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3",
    "4", "5", "6", "7", "8", "9", "0"]


def SaveMap(fin, fout):
    fileIn = open(fin, encoding="UTF-8")
    fileOut = open(fout, "x", encoding="UTF-8")
    size = fileIn.readline()
    fileOut.write(size)
    _, h = [int(n) for n in size.split()]
    for _ in range(h):
        fileOut.write("".join(fileIn.readline().split()))
    fileOut.write("\n")
    answer = fileIn.readline().strip()
    answerEnc = EncodeAnswer(answer)
    fileOut.writelines([answerEnc])
    fileIn.close()
    fileOut.close()


def EncodeAnswer(answer):
    newAnswer = ""
    for ch in answer:
        newAnswer += ch
        newAnswer += choice(letters)
    newAnswer2 = ""
    for ch in newAnswer:
        newAnswer2 += ch
        newAnswer2 += choice(letters)
    newAnswer3 = newAnswer2[::-1]
    return newAnswer3


SaveMap(r"D:\Users\Lux\Desktop\python\mazes\mazeForAnswer\maps\mapRaw_2.txt", r"D:\Users\Lux\Desktop\python\mazes\mazeForAnswer\maps\map2.txt")