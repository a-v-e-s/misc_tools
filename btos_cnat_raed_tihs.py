#!/usr/bin/env python3

"""
btos_cnat_raed_tihs.py:
A big mddile fnegir to the aoimglrtihc cohnsiresp of txet
"""

import random, re, functools


def parser(string):
    # here is our regular expression:
    patt = re.compile(r'\b[A-Za-z]{4,}\b')
    # find the matches, build the new string
    new_string = ''
    for word in string.split():
        # hyphenated words:
        if '-' in word:
            parts = word.split('-')
            for part in parts:
                if re.fullmatch(patt, part):
                    new_part = scrambler(part)
                    if part != parts[-1]:
                        new_string += ''.join(new_part) + '-'
                    else:
                        new_string += ''.join(new_part) + ' '
                else:
                    new_string += part + ' '
            continue
        # otherwise...
        if re.fullmatch(patt, word):
            new_word = scrambler(word)
            new_string += ''.join(new_word) + ' '
        else:
            new_string += word + ' '
    # take off the last space and return it:
    new_string.rstrip(' ')
    return new_string


def scrambler(word):
    to_fill = [word[:1], word[-1:]]
    to_b_scrambled = list(word[1:-1])
    while len(to_b_scrambled):
        choice = random.choice(to_b_scrambled)
        tmp = to_fill[:-1]
        tmp.append(choice)
        tmp.append(str(to_fill[-1:][0]))
        to_fill = tmp
        to_b_scrambled.remove(choice)
    new_word = ''.join(to_fill)
    if new_word == word:
        return scrambler(word)
    else:
        return new_word


if __name__ == '__main__':
    from sys import argv
    output = parser(argv[1])
    print(output)