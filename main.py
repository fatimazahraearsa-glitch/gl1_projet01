import random
import string

lettres=string.ascii_letters
c=""
while c!="w":
    c=random.choice(lettres)
    print(f"la lettre choisie est {c}")
    