# Aug16, 2020, ms
# ir-remote-pulses.py

# this is to see pulse patterns(on-off durations) from
# ir remote controllers

# ask python to bring his tool boxes
import pulseio
import board
import adafruit_irremote

# create an object to handle pulse input.  name it as pulsein
pulsein = pulseio.PulseIn(board.IR_RX, maxlen=120, idle_state=True)
# create a decoder
decoder = adafruit_irremote.GenericDecode()

# main loop
while True:
    # this is how you read ir signals from your ir remote
    pulses = decoder.read_pulses(pulsein)
    print(pulses)

