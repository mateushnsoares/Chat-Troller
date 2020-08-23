# Made by Ilan_M on 8/15/2020

import time
import pyautogui as pa


def pressKey(key):
    pa.keyDown(key)
    pa.keyUp(key)


# the following coordinates were tested fullscreen on a 1920x1080(aka. 'Full HD') display. You may change this if you have other resolution
ChromeSearchBar = [500,   60]
WhatsAppTypeInput = [1050, 990]
WhatsAppSearchBar = [250,  205]
WhatsAppGroupTitle = [250,  370]

# you must change before running the program. Read the README.md for more info.
chatName = 'somebody once told me'

pressKey('winleft')

# change this if you use other web browser
pa.write('Chrome')

pressKey('enter')

# you should change the 7 to a higher number if you have a slow computer
# or put a lower one if you have a fast computer
time.sleep(7)

pa.click(ChromeSearchBar)

pa.write('https://web.whatsapp.com/')

pressKey('enter')

time.sleep(10)  # wait fot WhatsApp web to open|

pa.click(WhatsAppSearchBar)
pa.write(chatName)

time.sleep(1)

pa.click(WhatsAppGroupTitle)

time.sleep(0.5)

pa.click(WhatsAppTypeInput)

# change this to the file you want to use, either a custom one or an included on this project is ok
file1 = open('no.txt')

# reading each line, then send every word separately
for line in file1:
    for word in line.split():
        pa.typewrite(word)
        pressKey('enter')
        # putting 'time.sleep(0.5)' here is optional

file1.close()
