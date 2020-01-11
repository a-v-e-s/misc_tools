"""
fix_filenames.py

A module to replace non-word, non-dot characters in filenames.
Can optionally be applied to directory names as well.
Offers a command-line interface and an importable function of the same name.

Author: Jon David Tannehill
"""

import os, re, argparse


def fix_filenames(directory, recursive=False, subdirs=False):
    pattern = re.compile(r'[^a-zA-Z0-9_\.]')
    if recursive == True:
        for root, subs, items in os.walk(directory):
            for x in items:
                if re.search(pattern, x):
                    new_name = re.sub(pattern, '_', x)
                    os.rename(os.path.join(root, x), os.path.join(root, new_name))
            if subdirs == True:
                for y in subs:
                    if re.search(pattern, y):
                        new_name = re.sub(pattern, '_', y)
                        os.rename(os.path.join(root, y), os.path.join(root, new_name))
    else:
        for x in os.listdir(directory):
            if subdirs == True or os.path.isfile(os.path.join(directory, x)):
                if re.search(pattern, x):
                    new_name = re.sub(pattern, '_', x)
                    os.rename(os.path.join(directory, x), os.path.join(directory, new_name))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Enter absolute path for the directory whose filenames you want to fix.\n'
        'use the -d or --recursive option to fix filenames of all subdirectories too.'
    )
    parser.add_argument('directory', nargs='?', default=None)
    parser.add_argument('-r', '--recursive', nargs='?', type=bool, default=False)
    parser.add_argument('-d', '--subdirs', nargs='?', type=bool, default=False)
    args = parser.parse_args()
    #
    recursive = False
    subdirs = False
    if args.directory == None:
        directory = input(
            'Enter the full, absolute path of the directory with files whose names you want to fix:\n'
        )
        if not os.path.isdir(directory):
            raise TypeError(
                directory + ' is not a valid (absolute) directory path!\n'
                'Example: ' + os.getcwd()
            )
        if input('Enter "r" to fix filenames recursively in all subdirectories (be careful!):') == 'r':
            recursive = True
        if input('Enter "d" to fix the names of subdirectories (think carefully!):') == 'd':
            subdirs = True
    #
    else:
        directory = args.directory
        if args.recursive != False:
            recursive = True
        if args.subdirs != False:
            subdirs = True
    #
    fix_filenames(directory, recursive, subdirs)