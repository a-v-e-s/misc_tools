"""
number.py: A crude script for numbering and renaming the files in one or more directories
Has bugs, and sometimes overwrites files. Still being developed.
Don't use on anything important.

Written by: Jon David Tannehill
"""

import os, sys, argparse


def zip_it(files_to_number):
    numbered = enumerate(files_to_number)
    zipper = zip(numbered, files_to_number)
    return numbered, zipper

def main(repeat=0):
    directory_list = []
    extensions = []

    if len(sys.argv) == 1 or repeat:
        directory_list = [x for x in input('\nEnter the directory or directories whose files you want to number separated by spaces:\n').split() if os.path.isdir(x)]
        extensions = [x for x in input('\nEnter a space-separated list of the extensions for the file types you wish to have numbered Leave blank to include all files:\n').split() if len(x) > 0]
    else:
        parser = argparse.ArgumentParser()
        parser.add_argument('directories', type=str, nargs='*', metavar='/path/to/directory1 /path/to/directory2', help='Enter a space-separated list of the full paths to directories whose files you wish to have numbered')
        parser.add_argument('-e', action='store', dest='e', nargs='*', help='Optionally, enter a space separated-list of the file extensions whose files you wish to have numbered.\nExample:\njpg wmv mp4 mp3 doc')

        args = parser.parse_args()
        for x in args.directories:
            if os.path.isdir(x):
                directory_list.append(x)
            else:
                print(x, 'is not a directory.')
        if args.e != None:
            for x in args.e:
                extensions.append(x)

    for x in directory_list:

        os.chdir(x)

        files_to_number = []
        if len(extensions) > 0:
            for y in os.listdir():
                for z in extensions:
                    if y.endswith(z):
                        files_to_number.append(y)
                        break
        else:
            files_to_number = os.listdir()

        numbered, zipper = zip_it(files_to_number)

        append = []
        for y in zipper:
            try:
                if int(str(y[1].split('.')[:-1]).strip('[').strip(']').strip("'")) in list(range(1, len(files_to_number) + 1)):
                    append.append(y[1])
            except ValueError:
                pass
        for z in append:
            files_to_number.remove(z)
        numbered, zipper = zip_it(files_to_number)

        clone = append.copy()
        fixed = [a[1] for a in sorted([tuple([int(a.split('.')[0]), a]) for a in clone])]
        starting_point = len(files_to_number) + len(fixed) - 1
        for b in reversed(fixed):
            new_name = str(starting_point) + '.' + str(b.split('.')[-1:]).strip('[').strip(']').strip("'")
            command = 'mv "' + b + '" ' + new_name
            print(command)
            os.popen(command)
            starting_point -= 1

        for c in zipper:
            old_name = str(c[1])		    
            new_name = (str(c[0][0]) + '.' + str(c[0][1].split('.')[-1:]).strip('[').strip(']').strip("'"))
            command = 'mv "' + old_name + '" ' + new_name
            print(command)
            os.popen(command)

    if input('\nGo again? [y/n]\n').lower() == 'y':
        main(repeat=1)


if __name__ == '__main__':
    main()
