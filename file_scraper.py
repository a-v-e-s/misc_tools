"""
A basic internet file scraper.
Requires mechanicalsoup.
Does what I want it to do for now.
Likely to be upgraded in the future.
"""

import os, sys, re, functools, mechanicalsoup
import tkinter as tk
from tkinter.filedialog import askdirectory
import number

Bowser = mechanicalsoup.StatefulBrowser()
pattern = re.compile('href=["|\'][^"\']*["|\']')


def main(ur, exts, dir, num):
    url, filetypes, directory, numb = ur.get(), exts.get(), dir.get(), num.get()
    Bowser.open(url)

    extensions = filetypes.split()
    for x in Bowser.links():
        link = re.search(pattern, str(x)).group()[6:-1]
        for y in extensions:
            if link.endswith(y):
                print('Downloading: ' + link)
                try:
                    Bowser.download_link(link, os.path.join(directory, os.path.split(link)[1]))
                except Exception:
                    print(sys.exc_info())
                break

    if numb == 1:
        number.number(directory, filetypes)

root = tk.Tk()
filetypes = tk.StringVar()
url = tk.StringVar()
directory = tk.StringVar()
numb = tk.IntVar()
tk.Label(root, text='Enter URL here:').grid(row=1, column=1, columnspan=2)
ur = tk.Entry(root, width=80, textvariable=url)
ur.grid(row=2, column=1, columnspan=2)
tk.Label(root, text='Enter file extensions to download here:').grid(row=3, column=1, columnspan=2)
ext = tk.Entry(root, width=80, textvariable=filetypes)
ext.grid(row=4, column=1, columnspan=2)
tk.Label(root, text='Folder to save files in:').grid(row=5, column=1, columnspan=2)
dir = tk.Entry(root, width=80, textvariable=directory)
dir.grid(row=6, column=1)
tk.Button(root, text='Browse', command=(lambda x=dir:[x.delete(0, len(x.get())), x.insert(0, askdirectory())])).grid(row=6, column=2)
tk.Label(root, text='Number files with number.py?').grid(row=7, column=1, columnspan=2)
num = tk.Checkbutton(root, variable=numb, onvalue=1, offvalue=0)
num.grid(row=8, column=1, columnspan=2)
numb.set(0)

tk.Button(root, text='Scrape!', command=functools.partial(main, url, filetypes, directory, numb)).grid(row=9, column=1, columnspan=2)
root.bind(sequence='<Return>', func=(lambda x: main(url, filetypes, directory, numb)))

if __name__ == '__main__':
    root.mainloop()