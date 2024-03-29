# This is really more of a rubric for an interactive
# python session to scrape the song and artist names
# from playlists on my Premium Pandora account
# because I have dozens of playlists and thousands of
# songs on them.


import os, time, random, pickle, re
from selenium import webdriver
from sys import exc_info
from selenium.webdriver.chrome.options import Options

def pandora():
    #
    SLEEP_LIMIT = 4
    PANDORA = 'https://www.pandora.com/'
    #
    browser = webdriver.Chrome()
    print('Pausing for discretion...')
    time.sleep(random.uniform(1, SLEEP_LIMIT))
    #
    browser.get(PANDORA)
    print('Pausing for discretion...')
    time.sleep(random.uniform(1, SLEEP_LIMIT))
    #
    browser.find_element_by_link_text('Log In').click()
    print('Pausing for discretion...')
    time.sleep(random.uniform(1, SLEEP_LIMIT))
    #
    email = input('Enter your login email:\n')
    browser.find_element_by_name('username').send_keys(email)
    print('Pausing for discretion...')
    time.sleep(random.uniform(1, SLEEP_LIMIT))
    #
    password = input('Enter your login password:\n')
    browser.find_element_by_name('password').send_keys(password)
    print('Pausing for discretion...')
    time.sleep(random.uniform(1, SLEEP_LIMIT))
    #
    browser.find_elements_by_tag_name('button')[3].click()
    print('Pausing for discretion...')
    time.sleep(random.uniform(1, SLEEP_LIMIT))
    #
    browser.find_element_by_link_text('Playlists').click()
    print('Pausing for discretion...')
    time.sleep(random.uniform(1, SLEEP_LIMIT))
    #
    master = {}
    playlist_name = input('Enter name of playlist to scrape, or "quit" to quit:\n')
    while playlist_name.lower() != 'quit': 
        #
        try:
            browser.find_element_by_link_text(playlist_name).click()
        except Exception:
            print("Couldn't find that one. Is it in view of the browser? Did you make a typo?")
            playlist_name = input('Enter name of playlist to scrape, or "quit" to quit:\n')
            continue
        #
        print('Pausing for discretion...')
        time.sleep(random.uniform(1, SLEEP_LIMIT))
        #
        #
        playlist = {}
        segment = {}
        old_segment = {}
        y = 0
        height = browser.get_window_size()['height']
        #
        while True:
            songs = [song.text for song in browser.find_elements_by_class_name('RowItemCenterColumn__mainText')]
            artists = [artist.text for artist in browser.find_elements_by_class_name('RowItemCenterColumn__secondText')]
            #
            try:
                assert len(songs) == len(artists)
            except AssertionError:
                print('Songs and artists mismatch:')
                print('len(songs):', len(songs))
                print('len(artists):', len(artists))
                break
            #
            segment = dict(zip(songs, artists))
            if segment == old_segment:
                break
            for key in segment.keys():
                if key not in playlist.keys():
                    playlist[key] = segment[key]
            old_segment = segment
            #
            y += 2*height
            js = 'window.scrollTo(0, ' + str(y) + ');'
            browser.execute_script(js)
            #
            print('Pausing for discretion...')
            time.sleep(random.uniform(1, SLEEP_LIMIT))
        #
        master[playlist_name] = playlist
        browser.back()
        playlist_name = input('Enter name of playlist to scrape, or "quit" to quit:\n')
    #
    fn = input('Enter full filepath of file to store data in:\n')
    with open(fn, 'wb') as f:
        pickle.dump(master, f)


def gaia():
    browser = webdriver.Chrome()
    browser.get('https://www.gaia.com/')

    print("Press <Enter> once you are logged in. I'll wait.")
    input()

    name = input('<Enter> the name of the person, as it appears in the url:\n')
    browser.get('https://www.gaia.com/person/' + name)

    print('Load scroll to bottom and load more until all are loaded,\nThen press <Enter>:\n')
    input()

    elems = browser.find_elements_by_xpath('//*[@href]')
    vids = [elem.get_attribute('href') for elem in elems if elem.get_attribute('href').endswith('fullplayer=feature')]

    output = input('<Enter> the full path to the output file here:\n')
    with open(output, 'w') as f:
        for vid in vids:
            f.write(vid + '\n')


def cc(url, target_dir, pause=3, index=0):

    browser = webdriver.Chrome()
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': target_dir}}
    browser.execute("send_command", params)

    browser.get(url)
    time.sleep(pause)
    input('Please scroll to the very bottom of the page, then press <Enter>')
    os.chdir(target_dir)

    pages = browser.find_elements_by_class_name('thumb')
    target_pattern = re.compile(r'^http.*(jpg|jpeg|png|gif|bmp|webm|webp|mp4)$', re.I)
    if index:
        pages = pages[index:]
    for page in pages:
        index += 1
        page.click()
        time.sleep(pause)

        new_dir = str(index).zfill(4)
        os.mkdir(new_dir); os.chdir(new_dir)

        browser.switch_to_window(browser.window_handles[1])
        time.sleep(pause)
        # thumbs lose their reference when the browser goes to
        # a new page and back so it needs to be this way
        # even though it's ugly and awkward:
        l = len(browser.find_elements_by_class_name('thumb'))
        for i in range(l):
            thumbs = browser.find_elements_by_class_name('thumb')
            thumbs[i].click()
            time.sleep(pause)
            target = browser.current_url
            if re.match(target_pattern, target):
                os.popen('wget ' + target)
                browser.back()
            else:
                try:
                    browser.back()
                except Exception:
                    print(exc_info())
                break
            time.sleep(pause)

        browser.close()
        time.sleep(pause)
        os.chdir('../')
        browser.switch_to_window(browser.window_handles[0])


def tulsi(url):
    pass


def inwo(target_dir):

    from selenium.common.exceptions import NoSuchElementException

    PAUSE = 4

    os.chdir(target_dir)

    browser = webdriver.Firefox()
    time.sleep(PAUSE)
    browser.get('https://www.inwocard.com/cards/')
    time.sleep(PAUSE+2)

    while True:
        imgs = browser.find_elements_by_tag_name('img')
        
        for img in range(len(imgs)):
            imgs[img].click()
            time.sleep(PAUSE)
            
            card = browser.find_element_by_tag_name('img')
            card.screenshot(browser.title+'.png')
            browser.back()
            time.sleep(PAUSE)
            
            imgs = browser.find_elements_by_tag_name('img')
        
        try:
            next_button = browser.find_element_by_link_text('Next')
            next_button.click()
            time.sleep(PAUSE)
        except NoSuchElementException:
            break



if __name__ == '__main__':
    print('this module is meant to be imported,')
    print('not run as __main__')
    exit(1)