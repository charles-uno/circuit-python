
from adafruit_hid import mouse
import adafruit_lis3dh
import board
import busio
import math
import time

# ======================================================================

MOUSE = mouse.Mouse()

I2C = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
ACCEL = adafruit_lis3dh.LIS3DH_I2C(I2C, address=0x19)

def main():
    """Use the board like a joystick to move the mouse."""
    while True:
        ax, ay, az = ACCEL.acceleration
        atotal = math.sqrt( ax**2 + ay**2 + az**2 )
        # We can get theta unambigiously since it's just 0 to 180.
        theta = math.acos(az/atotal)
        # Outside the range -90 to 90, there are ambiguities in phi.
        if ax == 0:
            ax = 0.000001
        phi = math.atan(ay/ax)
        if ax > 0:
            phi = phi + math.pi
        # The severity of the angle controls how fast we move the mouse.
        speed = 10*math.sin(theta)
        # The direction we hold the board is the direction we want the
        # mouse to move.
        dx = int(speed*math.sin(phi))
        dy = int(speed*math.cos(phi))
        print('dx:', dx, 'dy:', dy)
        # To line up with the screen, the board should be aligned with
        # the USB plugin on the right.
        MOUSE.move(x=dx, y=dy)
        time.sleep(0.1)

# ======================================================================

main()
