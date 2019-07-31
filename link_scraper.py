"""
A basic image scraper.
Does what I need it to for now.
Likely to be upgraded in the future.
"""

import os, re, mechanicalsoup


def main():
    url = input('\nEnter the url you wish to scrape linked files from:\n')
    filetypes = input('\nEnter a space separated list of the extensions for all filetypes you wish to scrape:\n').split(' ')
    while True:
        directory = input('\nEnter the full path to the directory you would like to save the downloads to:\n')
        if os.path.isdir(directory):
            os.chdir(directory)
            break
        else:
            print('\nInvalid directory path. Try again!\n')

    Bowser = mechanicalsoup.StatefulBrowser()
    Bowser.open(url)

    pattern = re.compile()

    for x in Bowser.links():
        # do something 

    if input('\nGo again? [y/n]\n').lower() == 'y':
        main()


if __name__ == '__main__':
    main()