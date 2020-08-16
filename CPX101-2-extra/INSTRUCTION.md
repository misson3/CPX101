## memo for running extra codes
Last updated: Aug16, 2020

## installing required library files

If you did not copy entire library bundle into CPX, some library files may be missing to run the extra codes.

##### FAQ: How do I know whether I have required library files?

Open "Serial" on Mu editor and run your code.  If required library is missing, you will get something like followings.

```python
Traceback (most recent call last):
  File "main.py", line 15, in <module>
ImportError: no module named 'simpleio'
```

It says 'simpleio' is missing.  Copy it from the bundle to lib folder on CPX.



### step 1: check circuit python version

Connect CPX to PC.  CIRCUITPY will be mounted.

In CIRCUITPY, there is `boot_out.txt` file.  Open the file.  In my case, I see,

```
Adafruit CircuitPython 5.3.1 on 2020-07-13; Adafruit CircuitPlayground Express with samd21g18
```

"5.3.1" is the version of my CircutPython.

### step 2: download circuitpython library bundle

If you already have downloaded the bundle before, look for the folder.  If you cannot find it, download it from [here](https://circuitpython.org/libraries).  Make sure to match the version.  If you have Circuitpython version 5, select something like `adafruit-circuitpython-bundle-5.x-mpy-yyyymmdd.zip`.  Unzip the file.

### step 3: copy the files to CPX

Open the bundle folder and look for the file of your interest.  Copy it to `lib` folder on your CPX.



## ir-remote-pulses.py

Make sure that you have `adafruit_irremote.mpy` in CPX library folder (CIRCUITPY/lib).



## tilt-arpeggiator.py

This requires `simpleio.mpy` in CPX library folder (CIRCUITPY/lib).

