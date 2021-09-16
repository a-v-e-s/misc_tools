from multiprocessing import Process, cpu_count
from threading import Thread
from time import sleep


def weaver(targets, args_list, simultaneous_bots=3, separate=True):
    assert len(targets) == len(args_list)

    # create bots:
    zipp = zip(targets, args_list)
    sleeping_bots = []
    for z in zipp:
        if separate:
            bot = Process(target=z[0], args=z[1])
        else:
            bot = Thread(target=z[0], args=z[1])
        sleeping_bots.append(bot)

    # start the appropriate number of bots:
    running_bots = []
    for x in range(simultaneous_bots):
        try:
            sleeping_bots[x].start()
            running_bots.append(sleeping_bots[x])
            sleep(30)
        except IndexError:
            break
    for x in range(simultaneous_bots):
        try:
            sleeping_bots.remove(sleeping_bots[0])
        except IndexError:
            break

    # cycle through running_bots,
    # removing them as the finish and starting new ones:
    while sleeping_bots:
        sleep(0.5)
        for bot in running_bots:
            if not bot.is_alive():
                running_bots.remove(bot)
                sleeping_bots[0].start()
                running_bots.append(sleeping_bots[0])
                sleeping_bots.remove(sleeping_bots[0])
                sleep(10)
                break

    # wait for everything to finish:
    for bot in running_bots:
        bot.join()