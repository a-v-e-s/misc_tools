# This is really more of a rubric for an interactive
# python session to scrape the song and artist names
# from playlists on my Premium Pandora account
# because I have dozens of playlists and thousands of
# songs on them.


import time, random, pickle
from selenium import webdriver

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


if __name__ == '__main__':
    print('yer doin it wrong')
    exit(1)