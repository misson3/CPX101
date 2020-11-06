# Oct02, 2020
# Sep25, 2020
# acceleration indicator

# ask python to bring following tools in his pocket
import adafruit_lis3dh
import board
import busio
import neopixel
import time
from digitalio import DigitalInOut, Direction, Pull
from simpleio import map_range

# === accelerometer via i2c communication ===
# create i2c connection
i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
# create accelerometer object.  give it a name, acc
acc = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19)
# limit max acceleration up to 2G
acc.range = adafruit_lis3dh.RANGE_2_G

# button A settings
ButtonA = DigitalInOut(board.BUTTON_A)
# we read button state (on or off).  direction should be input
ButtonA.direction = Direction.INPUT
# set the initial state (when it is not pressed) as low (DOWN)
ButtonA.pull = Pull.DOWN

# button B settings
ButtonB = DigitalInOut(board.BUTTON_B)
# we read button state (on or off).  direction should be input
ButtonB.direction = Direction.INPUT
# set the initial state (when it is not pressed) as low (DOWN)
ButtonB.pull = Pull.DOWN

# Neopixel settings.  looks familiar?
npx = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False)

# brightness control
a = 10  # will be toggled 10 <--> 1
# range control
b = 2  # will be toggled 2 <---> 1

# main loop
while True:
    # get acceleration reading
    z = acc.acceleration[2]

    # coloring neopixel
    # mapped_z = int(map_range(z, -19.6, 19.6, -20, 20))
    mapped_z = int(z*b)

    npx.fill((0, 0, 0))
    print(mapped_z)
    # z axis
    if mapped_z > 0 and 5 >= mapped_z:
        # npx 5, 6, 7, 8, 9
        # acc 1, 2, 3, 4, 5 m/s^2
        for i in range(mapped_z):
            npx[i+5] = (i*a, (4-i)*a, 0)
    elif mapped_z > 5:
        for i in range(5):
            npx[i+5] = (i*a, (4-i)*a, 0)
    elif mapped_z >= -5 and 0 > mapped_z:
        # npx  4,  3,  2,  1,  0
        # acc -1, -2, -3, -4, -5
        for i in range(mapped_z*(-1)):
            npx[4-i] = (i*a, 0, (4-i)*a)
    elif -5 > mapped_z:
        for i in range(5):
            npx[4-i] = (i*a, 0, (4-i)*a)

    if ButtonA.value:
        time.sleep(0.5)
        if a == 10:
            a = 1
        else:
            a = 10

    if ButtonB.value:
        time.sleep(0.5)
        if b == 2:
            b = 1
        else:
            b = 2

    npx.show()
