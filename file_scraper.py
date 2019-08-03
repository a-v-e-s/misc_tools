"""
A basic internet file scraper.
Requires mechanicalsoup.
Does what I want it to do for now.
Likely to be upgraded in the future.
"""

import os, sys, re, functools, mechanicalsoup
import tkinter as tk
from tkinter.filedialog import askdirectory

Bowser = mechanicalsoup.StatefulBrowser()
pattern = re.compile('href=["|\'][^"\']*["|\']')


def main(ur, exts, dir):
    url, filetypes, directory = ur.get(), exts.get(), dir.get()
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

root = tk.Tk()
filetypes = tk.StringVar()
url = tk.StringVar()
directory = tk.StringVar()
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

tk.Button(root, text='Scrape!', command=functools.partial(main, url, filetypes, directory)).grid(row=7, column=1, columnspan=2)
root.bind(sequence='<Return>', func=(lambda x: main(url, filetypes, directory)))
if __name__ == '__main__':
    root.mainloop()