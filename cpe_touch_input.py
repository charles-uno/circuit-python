
import touchio
import board
import time

import helpers

# ======================================================================

TOUCHES = [
    touchio.TouchIn(board.A1),
    touchio.TouchIn(board.A2),
    touchio.TouchIn(board.A3),
]

def cpe_touch_input():
    """Touch A1, A2, and A3 to make colors race."""
    while True:
        for channel, touch in enumerate(TOUCHES):
            # touchio.TouchIn(board.A1) is True if A1 is being touched,
            # False otherwise. 
            if touch.value:
                helpers.chase_advance(channel)
            else:
                helpers.chase_clear(channel)
        time.sleep(0.1)

# ======================================================================

cpe_touch_input()
