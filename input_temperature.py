
import adafruit_thermistor
import board
import time

import helpers

# ======================================================================

THERMISTOR = thermistor = adafruit_thermistor.Thermistor(board.TEMPERATURE, 10000, 10000, 25, 3950)

def cpe_temp_input():
    """Light up to show how warm it is."""
    while True:
        temp = THERMISTOR.temperature
        print('Temperature:', temp)
        helpers.cpe_lin_show(20, 40, temp)
        time.sleep(0.1)

# ======================================================================

cpe_temp_input()
