from pynput.keyboard import Key, Controller
import time


def start():
    keyboard = Controller()

    nPacks = int(input("number of packs: "))

    print("tab back to hearthstone")

    time.sleep(2)

    t_end = time.time() + nPacks * 6


    print("opening packs...")

    while time.time() < t_end:
        time.sleep(0.2)
        keyboard.press(' ')
        keyboard.release(' ')

    print(nPacks," packs opened")
    while True:
        query = input("do you want to open more packs?").lower().strip()
        if query == '' or  not query[0] in ['y','n']:
            print("please answer with yes or no")
        else:
            break
    
    if query[0] == 'y':
        start()
    if query[0] == 'n':
        print("closing application")
        time.sleep(1.5)


start()