
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
    """Light up to indicate total acceleration."""
    # Note: sitting still, the device should feel one "gee", or 1x
    # gravity. To feel more gees, accelerate it by shaking it around. To
    # feel zero gees, let it free fall, for example by holding it in
    # your hand and jumping!
    while True:
        gees = math.sqrt( sum( x**2 for x in ACCEL.acceleration ) )/9.8
        print('Gs:', gees)
        helpers.cpe_lin_show(0, 5, gees)
        time.sleep(0.01)

# ======================================================================

main()
