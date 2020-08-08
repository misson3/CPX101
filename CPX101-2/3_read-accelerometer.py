# Aug08, 2020
# 3_read-accelerometer.py

import time
from adafruit_circuitplayground.express import cpx

while True:
    x, y, z = cpx.acceleration
    print((x, y, z))
    time.sleep(0.1)
