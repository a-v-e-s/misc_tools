""" 
Sorting and managing files
Author: Jon David Tannehill
"""


import os
import pickle
import hashlib
import subprocess
import time
#from PIL import Image


HOME = os.getenv('HOME')
IGNORED = {'.git'}
MANAGED = {
    'Pictures',
    'Documents',
    'Music',
    'Videos',
    #'Smartphone',
}


def get_hash(filename, alg=hashlib.sha1):
    """ Return hexdigest of a given file's hash """

    hash_ = alg()
    with open(filename, 'rb') as f:
        while True:
            data = f.read(65536)
            if not data:
                break
            hash_.update(data)
    
    return hash_.hexdigest()


def display_img(fn):
    """ Display an image for the user. """

    viewer = subprocess.Popen(['vlc', fn])
    time.sleep(5)
    viewer.terminate()
    viewer.kill()


def load_pickles():
    """ Load dictionaries from pickle files in managed folders """

    dic = dict()

    for folder in MANAGED:
        filename = f'{HOME}/{folder}/file_db.pkl'
        if os.path.isfile(filename):
            dic[folder] = pickle.load(filename)
        else:
            pass

    return dic


def generate_pickle(folder):
    """ Create a pickle file with a dictionary of filehashes and relative paths """
    
    dic = dict()
    
    for root, _, files in os.walk(folder):
        if not os.path.split(root)[-1] in IGNORED:
            for file in files:
                filename = os.path.join(root, file)
                if os.path.isfile(filename):
                    filehash = get_hash(filename)
                    relpath = filename.lstrip(f'{folder}/')
                    dic[filehash] = relpath
    
    with open(f'{folder}/file_db.pkl', 'wb') as f:
        pickle.dump(dic, f)

    return dic


if __name__ == '__main__':
    pass