#!/usr/bin/env python3

"""
number2.py: Number all the files in a directory
Much, much simpler and less buggy than the previous number.py

Usage: 
$ python3 number.py /path/to/directory
"""

import os
from sys import argv
from time import sleep


def number_these(directory):
    os.chdir(directory)
    os.chdir('..')
    tempdir = 'temp.' + str(os.getpid())
    os.mkdir(tempdir)
    for x in enumerate(os.listdir(directory)):
        new_name = str(x[0]) + '.' + x[1].split('.')[-1]
        os.popen('mv "' + directory.split('/')[-1] + '/' + x[1] + '" "' +
            os.path.join(tempdir, new_name) + '"'
        )
    sleep(0.1) # this is important for some reason...
    os.rmdir(directory)
    os.rename(tempdir, directory)


if __name__ == '__main__':
    number_these(argv[1])