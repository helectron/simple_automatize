#!/usr/bin/python3
import random

def guess_who_pld(holbie):
    if holbie == 1:
        return "Your turn Helena"

    elif holbie == 2:
        return "Your turn Two"

    elif holbie == 3:
        return "Your turn Three"

    elif holbie == 4:
        return "Your turn Four"

    elif holbie == 5:
        return "Your turn Five"

    elif holbie == 6:
        return "Your turn Six"

r = random.randint(1, 6)
fortune = guess_who_pld(r)
print(fortune)
