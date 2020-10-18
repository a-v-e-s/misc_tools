#!/usr/bin/env python3

"""
cyrillify.py

Turn English characters from the input string to Cyrillic look-alikes.

Usage:
$ ./cyrillify.py $string_to_change

Silly.
"""

import pickle, os, sys

#alphabet = [chr(x) for x in [y for y in range(65, 91)] + [z for z in range(97, 123)]]
#cyrillic = set([chr(x) for x in range(1024, 1280)])
#Cyrillic = {}


def reprint(alphabet):
    print()
    col = 1
    for c in alphabet:
        print(ord(c), c, end='\t')
        col += 1
        if col > 12:
            print()
            col = 0
    print()


def create_dict():
    english = [chr(x) for x in [y for y in range(65, 91)] + [z for z in range(97, 123)]]
    cyrillic = [chr(x) for x in range(1024, 1280)]
    Cyrillic = {}
    #
    reprint(cyrillic)
    for c in english:
        print()
        print(c)
        #
        try:
            n = int(input('Number of matching Cyrillic character:\t'))
        except ValueError:
            n = None
        #
        Cyrillic[c] = chr(n) if n else c
        #
        if input('Reprint? [y/n]\t').lower() == 'y':
            reprint(cyrillic)
    #
    return Cyrillic


def cyrillify(string, Cyrillic):
    index = 0
    lisp = [c for c in string]
    for c in lisp:
        try:
            lisp[index] = Cyrillic[c]
        except KeyError:
            pass
        index += 1
    return ''.join(lisp)


if __name__ == '__main__':
    if 'cyrillify.pkl' in os.listdir():
        with open('cyrillify.pkl', 'rb') as f:
            Cyrillic = pickle.load(f)
    else:
        if input('cyrillify.pkl does not exist! Create it now? [y/n]\n').lower() == 'y':
            with open('cyrillify.pkl', 'wb') as f:
                Cyrillic = create_dict()
                pickle.dump(Cyrillic, f)
        else:
            raise FileNotFoundError('Need to create dict and pickle it in "cyrillify.pkl"')
    #
    print(cyrillify(sys.argv[1], Cyrillic))