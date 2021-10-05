from random import randint
from pathlib import Path

d_f = Path(__file__).resolve().parent


def randText(file):
    hi_file = d_f / file

    f = open(hi_file, encoding='utf-8')

    line = f.read()

    rand = line.split(';')

    return rand[randint(0, len(rand) - 1)]
