
import board
import math
import neopixel

# ======================================================================

def cpe_log_show(vmin, vmax, v):
    return cpe_neopixel_show( log_to_ten(vmin, vmax, v) )

# ----------------------------------------------------------------------

def cpe_lin_show(vmin, vmax, v):
    return cpe_neopixel_show( lin_to_ten(vmin, vmax, v) )

# ----------------------------------------------------------------------

NEOPIXEL = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.1, auto_write=False)

def cpe_neopixel_show(n):
    """Accept a number from 0 to 10. Light up that many LEDs."""
    black = (0, 0, 0)
    rainbow = [
        (0, 0, 255),
        (0, 64, 192),
        (0, 128, 128),
        (0, 192, 64),
        (0, 255, 0),
        (64, 192, 0),
        (128, 128, 0),
        (192, 64, 0),
        (255, 0, 0),
        (192, 0, 64),
    ]
    for i in range(10):
        # Gross, they're ordered counterclockwise.
        NEOPIXEL[9 - i] = black if i >= int(n) else rainbow[i]
        NEOPIXEL.show()
    return

# ----------------------------------------------------------------------

def lin_to_ten(vmin, vmax, v):
    return 10*(v - vmin)/(vmax - vmin)

# ----------------------------------------------------------------------

def log_to_ten(vmin, vmax, v):
    vmin, vmax, v = [ max(1, x) for x in (vmin, vmax, v) ]
    return 10*math.log(v/vmin)/math.log(vmax/vmin)
