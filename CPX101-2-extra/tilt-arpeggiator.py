# Aug16, 2020, ms
# tilt-arpeggiator.py
# ref: 初心者のためのCircuitPythonの本１、p90-より　を改変

# ask python to bring following tools in his pocket
import adafruit_lis3dh
import array
import audioio
import board
import busio
import math
import neopixel
import time
from digitalio import DigitalInOut, Direction, Pull
from simpleio import map_range


# sine wave generator
def s_wave(freq):
    vol = 0.8
    sample_rate = 8000
    length = sample_rate // freq
    sine_wave = array.array("H", [0] * length)
    for i in range(length):
        sine_wave[i] = int((1 + math.sin(2 * math.pi * i / length)) * (2 ** 15) * vol)
    return sine_wave


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

# speaker settings
speaker_enable = DigitalInOut(board.SPEAKER_ENABLE)
# yes, speaker is an output device
speaker_enable.direction = Direction.OUTPUT
speaker_enable.value = True
audio = audioio.AudioOut(board.A0)  # speaker is connected to A0 pin

# Neopixel settings.  looks familiar?
npx = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False)

# main loop
while True:
    # get acceleration reading
    x = acc.acceleration[0]  # we use only x axis reading
    # check readings
    print('x acc value:')
    print((x,))  # this is for plotting

    # coloring neopixel
    x_to_npx = int(map_range(x, 6, -6, 0, 9))
    npx.fill((0, 0, 0))
    for i in range(x_to_npx + 1):
        npx[i] = (10-i, i, 0)
    npx.show()

    if ButtonA.value:
        # convert x acceleration to a frequency
        x_to_freq = map_range(x, 6, -6, 220, 440)
        # generate sine waves(tones)
        sw_sample1 = audioio.RawSample(s_wave(int(x_to_freq)))
        sw_sample2 = audioio.RawSample(s_wave(int(x_to_freq * 1.0594 ** 4)))
        sw_sample3 = audioio.RawSample(s_wave(int(x_to_freq * 1.0594 ** 7)))
        sw_sample4 = audioio.RawSample(s_wave(int(x_to_freq * 1.0594 ** 12)))
        sw_sample5 = audioio.RawSample(s_wave(int(x_to_freq * 1.0594 ** 16)))
        # pack the waves into a list
        five_tones = [sw_sample1, sw_sample2, sw_sample3, sw_sample4, sw_sample5]

        speed = abs(20 - abs(x - 10))
        print('speed:', speed)
        for k in range(5):
            audio.play(five_tones[k], loop=True)
            time.sleep(0.03 * speed)
        for k in reversed(range(1, 4)):
            audio.play(five_tones[k], loop=True)
            time.sleep(0.03 * speed)
        audio.stop()

