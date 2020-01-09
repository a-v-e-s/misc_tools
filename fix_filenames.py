import os, re, argparse


def fix_filenames(directory, deep=False):
    pattern = re.compile(r'[^a-zA-Z0-9_\.]')
    if deep != False:
        for root, subs, items in os.walk(directory):
            for x in items:
                if re.search(pattern, x):
                    os.rename(x, re.sub(pattern, '_', x))
    else:
        for x in os.listdir(directory):
            if re.search(pattern, x):
                os.rename(x, re.sub(pattern, '_', x))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Enter absolute path for the directory whose filenames you want to fix.\n'
        'use the -d or --deep option to fix filenames of all subdirectories too.'
    )
    parser.add_argument('directory', nargs='?', default=None)
    parser.add_argument('-d', '--deep', nargs='?', type=bool, default=False)
    args = parser.parse_args()
    #
    if args.directory == None:
        directory = input(
            'Enter the full, absolute path of the directory with files whose names you want to fix:\n'
        )
        if not os.path.isdir(directory):
            raise TypeError(
                directory + ' is not a valid (absolute) directory path!\n'
                'Example: ' + os.getcwd()
            )
        if input('Enter "d" to fix the filenames of *ALL* subdirectories (think carefully!):') == 'd':
            deep = True
    #
    fix_filenames(directory, deep)