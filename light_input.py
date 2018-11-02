
import analogio
import board
import time

import helpers

# ======================================================================

EYE = analogio.AnalogIn(board.LIGHT)

def cpe_light_input():
    """Light up to show how bright it is"""
    # Not sure of the units, but right up to a light bulb is 60k.
    while True:
        brightness = EYE.value
        print('Brightness:', brightness)
        helpers.cpe_log_show(500, 50000, brightness)
        time.sleep(0.1)

# ======================================================================

cpe_light_input()
