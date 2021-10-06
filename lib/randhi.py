from random import randint
from pathlib import Path

d_f = Path(__file__).resolve().parent

def randHi():

    hi_file = d_f / "hi.txt"

    f = open(hi_file, encoding='utf-8')

    line = f.read()

    rand = line.split(';')

    return rand[randint(0, len(rand)-1)]


def randBingus():

    bing_file = d_f / "bingus.txt"

    f = open(bing_file, encoding='utf-8')

    line = f.read()

    rand = line.split(', ')

    return rand[randint(0, len(rand) - 1)]

