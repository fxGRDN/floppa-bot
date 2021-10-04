from random import randint


def randHi():
    f = open("hi.txt", encoding='utf-8')

    line = f.read()

    rand = line.split(';')

    return rand[randint(0, len(rand)-1)]


def randBingus():
    f = open("bingus.txt", encoding='utf-8')

    line = f.read()

    rand = line.split(', ')

    return rand[randint(0, len(rand) - 1)]
