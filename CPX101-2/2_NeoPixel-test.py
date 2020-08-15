# Aug08, 15, 2020
# 2_NeoPixel-test.py

import time
import board
import neopixel

npx = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False)

while True:
    for pp in range(10):
        npx[pp] = (25, 25, 25)
        npx.show()
        time.sleep(0.2)
    for pp in range(10):
        npx[pp] = (0, 0, 0)
        npx.show()
