# Aug08, 2020
# 4_tilt_mouse.py

import usb_hid
import time
from adafruit_circuitplayground.express import cpx
from adafruit_hid.mouse import Mouse

m = Mouse(usb_hid.devices)

while True:
    x, y, z = cpx.acceleration
    print((x, y, z))
    # move mouse cursor
    m.move(int(x), int(y))
    time.sleep(0.5)
