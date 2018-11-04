
import adafruit_lis3dh
import board
import busio
import math
import time

import helpers

# ======================================================================

I2C = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
ACCEL = adafruit_lis3dh.LIS3DH_I2C(I2C, address=0x19)

def main():
    """Light up to show which neopixel points up."""
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
        # Let's also scale to 0 to 360.
        if phi < 0:
            phi += 2*math.pi
        # We want 0 to be at pixel 2.
        n = int(round(5*phi/math.pi, 0) + 2) % 10
        helpers.cpe_lin_show(0, 10, 10 - n)
        print('Phi:', phi*180/math.pi, 'N:', n)
        time.sleep(0.1)

# ======================================================================

main()
