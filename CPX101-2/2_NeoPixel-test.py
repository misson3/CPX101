# Aug08, 2020
# 2_NeoPixel-test.py

import time
import board
import neopixel

npx = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False)

for pp in range(10):
    npx[pp] = (25, 25, 25)
    npx.show()
    time.sleep(0.2)
