
from adafruit_hid import mouse
import board
import time
import touchio

# ======================================================================

MOUSE = mouse.Mouse()

# For simplicity, let's just map capacitive touches to mouse directions.
TOUCH_1 = touchio.TouchIn(board.A1)
TOUCH_2 = touchio.TouchIn(board.A2)
TOUCH_3 = touchio.TouchIn(board.A3)
TOUCH_4 = touchio.TouchIn(board.A4)
TOUCH_5 = touchio.TouchIn(board.A5)
TOUCH_6 = touchio.TouchIn(board.A6)

def touch_mouse():
    """Control the mouse using capacitive touch."""
    while True:
        if TOUCH_1.value:
            print('Touched 1')
            MOUSE.move(x=1)
        if TOUCH_2.value:
            print('Touched 2')
            MOUSE.move(x=-1)
        if TOUCH_3.value:
            print('Touched 3')
            MOUSE.move(y=1)
        if TOUCH_4.value:
            print('Touched 4')
            MOUSE.move(y=-1)
        if TOUCH_5.value:
            print('Touched 5')
            MOUSE.click(mouse.Mouse.LEFT_BUTTON)
        if TOUCH_6.value:
            print('Touched 6')
            MOUSE.click(mouse.Mouse.RIGHT_BUTTON)
        time.sleep(0.2)

# ======================================================================

mouse_touch()
