
import analogio
import board
import time

import helpers

# ======================================================================

A0_VOLTAGE = analogio.AnalogIn(board.A0)

def main():
    """Light up to show the position of the pot."""
    # On the Trinket M0, A0 is marked "1~". That's the middle output of
    # the pot. The other ones go to ground and 3.3V.
    while True:
        voltage = A0_VOLTAGE.value*3.3/65536
        print('A0 Voltage:', voltage)
        helpers.cpe_lin_show(0, 3, voltage)
        time.sleep(0.1)

# ======================================================================

main()
