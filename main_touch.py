
import touchio
import board
import time

import helpers

# ======================================================================

TOUCHES = [
    # touchio.TouchIn(whatever).value is true if it's being touched.
    touchio.TouchIn(board.A1),
    touchio.TouchIn(board.A2),
    touchio.TouchIn(board.A3),
]

def main():
    """Touch A1, A2, and A3 to make colors race."""
    while True:
        for channel, touch in enumerate(TOUCHES):
            if touch.value:
                helpers.chase_advance(channel)
            else:
                helpers.chase_clear(channel)
        time.sleep(0.1)

# ======================================================================

main()
