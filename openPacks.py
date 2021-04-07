from pynput.keyboard import Key, Controller
import time


keyboard = Controller()

nPacks = int(input('number of packs: '))

print("tab back to hearthstone")

time.sleep(2)

t_end = time.time() + nPacks * 6


print("opening packs...")

while time.time() < t_end:
    time.sleep(0.2)
    keyboard.press(' ')
    keyboard.release(' ')

print(nPacks," packs opened")