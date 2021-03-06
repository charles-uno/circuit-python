
import board
import math
import neopixel

# ======================================================================

def cpe_log_show(vmin, vmax, v):
    return cpe_neopixel_scale( log_to_ten(vmin, vmax, v) )

# ----------------------------------------------------------------------

def cpe_lin_show(vmin, vmax, v):
    return cpe_neopixel_scale( lin_to_ten(vmin, vmax, v) )

# ----------------------------------------------------------------------

NEOPIXEL = None

def init_neopixel():
    global NEOPIXEL
    if NEOPIXEL is None:
        NEOPIXEL = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.1, auto_write=False)
    return

COLORS = [
    [0, 0, 255],
    [0, 64, 192],
    [0, 128, 128],
    [0, 192, 64],
    [0, 255, 0],
    [64, 192, 0],
    [128, 128, 0],
    [192, 64, 0],
    [255, 0, 0],
    [192, 0, 64],
]

BLACK = (0, 0, 0)

def cpe_neopixel_scale(n):
    """Accept a number from 0 to 10. Light up that many LEDs."""
    # Define this on use, not import, to avoid conflicts.
    init_neopixel()
    for i in range(10):
        # Gross, they're ordered counterclockwise.
        NEOPIXEL[9 - i] = BLACK if i >= int(n) else COLORS[i]
    return NEOPIXEL.show()

# ----------------------------------------------------------------------

def lin_to_ten(vmin, vmax, v):
    return 10*(v - vmin)/(vmax - vmin)

# ----------------------------------------------------------------------

def log_to_ten(vmin, vmax, v):
    vmin, vmax, v = [ max(1, x) for x in (vmin, vmax, v) ]
    return 10*math.log(v/vmin)/math.log(vmax/vmin)

# ======================================================================

CHASE_POS = [0, 0, 0]

def chase_advance(channel):
    global CHASE_POS
    init_neopixel()
    chase_clear(channel)
    tmp = list( NEOPIXEL[ CHASE_POS[channel] ] )
    tmp[channel] = 255
    NEOPIXEL[ CHASE_POS[channel] ] = tmp
    CHASE_POS[channel] = (CHASE_POS[channel] + 1) % 10
    return NEOPIXEL.show()

# ----------------------------------------------------------------------

def chase_clear(channel):
    init_neopixel()
    for i in range(10):
        tmp = list( NEOPIXEL[i] )
        tmp[channel] = 0
        NEOPIXEL[i] = tmp
    return NEOPIXEL.show()

# ======================================================================
