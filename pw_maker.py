from random import choice
from argparse import ArgumentParser

def pw_maker(length=None, main=False):
    if length == None:
        parser = ArgumentParser()
        parser.add_argument('length', nargs='?')
        args = parser.parse_args()
        length = int(args.length)

    possibles = ['1','2','3','4','5','6','7','8','9','0',
        'a','b','c','d','e','f','g','h','i','j','k','l','m',
        'n','o','p','q','r','s','t','u','v','w','x','y','z',
        'A','B','C','D','E','F','G','H','I','J','K','L','M',
        'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
    ]

    chosen = []
    for x in range(length):
        chosen.append(choice(possibles))
    
    pw = ''.join(chosen)
    
    if main:
        print(pw)
    else:
        return pw

if __name__ == '__main__':
    pw_maker(None, True)
