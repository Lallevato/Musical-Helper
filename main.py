##This program goes out any creatively blocked musicians in their musical endeavors. Godspeed --Luke


from functions import *

Chord1 = "C"
Chord2 = "G"
Chord3 = "Am"
Chord4 = "F"

while True:
    user = input("Press Enter to generate chord progression, or 'exit' to exit: ")

    if user == "exit":
        exit()
    else:
        Chord1 = createChord(Chord1)
        Chord2 = createChord(Chord2)
        Chord3 = createChord(Chord3)
        Chord4 = createChord(Chord4)

        print("\n" + Chord1, Chord2, Chord3, Chord4, "\n")