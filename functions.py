from modifiers import *
from chordlist import *
import random

def createChord(x):
    x = random.choice(chords)
    if "m" in x:
        x += random.choice(minorMods)
    else:
        x += random.choice(majorMods)

    rand = random.random() * 10

    if rand > 7:
        x += random.choice(bassnotes)

    return x
