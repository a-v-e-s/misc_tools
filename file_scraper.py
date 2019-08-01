"""
A basic internet file scraper.
Requires mechanicalsoup.
Does what I want it to do for now.
Likely to be upgraded in the future.
"""

import os, sys, re, mechanicalsoup

Bowser = mechanicalsoup.StatefulBrowser()
pattern = re.compile('href=["|\'][^"\']*["|\']')


def main():
    url = input('\nEnter the url you wish to scrape linked files from:\n')
    filetypes = input('\nEnter a space separated list of the extensions for all filetypes you wish to scrape:\n').split(' ')
    
    while True:
        directory = input('\nEnter the full path to the directory you would like to save the downloads to:\n')
        if os.path.isdir(directory):
            os.chdir(directory)
            break
        elif os.path.isdir(os.path.split(directory)[0]):
            os.chdir(os.path.split(directory)[0])
            print('\nCreating directory ' + os.path.split(directory)[1])
            os.mkdir(os.path.split(directory)[1])
            os.chdir(os.path.split(directory)[1])
            break
        else:
            print('\nInvalid directory path. Try again!\n')
    
    Bowser.open(url)

    for x in Bowser.links():
        link = re.search(pattern, str(x)).group()[6:-1]
        for y in filetypes:
            if link.endswith(y):
                print('Downloading: ' + link)
                try:
                    Bowser.download_link(link, os.path.join(os.getcwd(), os.path.split(link)[1]))
                except Exception:
                    print(sys.exc_info())
                break

    if input('\nGo again? [y/n]\n').lower() == 'y':
        main()


if __name__ == '__main__':
    main()