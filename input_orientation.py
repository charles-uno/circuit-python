

import adafruit_lis3dh
import board
import busio
import math
import time

import helpers

# ======================================================================

I2C = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
ACCEL = adafruit_lis3dh.LIS3DH_I2C(I2C, address=0x19)

def sandbox():
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

#        helpers.cpe_pixel(n)

        print('Phi:', phi*180/math.pi, 'N:', n)

        time.sleep(0.1)



# ======================================================================

sandbox()







# ======================================================================



def cpe_mouse():
    mouse = mouse.Mouse()

    analogin = analogio.AnalogIn(board.A0)

    while True:
        voltage = analogin.value * 3.3 / 65536
        print('voltage:', voltage)

        mouse.move(x=voltage)

        time.sleep(1)






# ----------------------------------------------------------------------

def toggle_red_led(dt=0.5):
    red_led = digitalio.DigitalInOut(board.D13)
    red_led.direction = digitalio.Direction.OUTPUT
    red_led.value = True
    while True:
        red_led.value = not red_led.value
        time.sleep(dt)

# ----------------------------------------------------------------------

def oscillate_red_led(w=5):
    import pulseio
    led = pulseio.PWMOut(board.D13, frequency=5000, duty_cycle=0)
    t, dt = 0, 0.01
    while True:
        t += dt
        led.duty_cycle = int(0.5*(math.cos(w*t) + 1)*65535)
        print('setting to:', led.duty_cycle)
        time.sleep(0.01)

# ----------------------------------------------------------------------

def read_pot():
    # On the Trinket M0, A0 is marked "1~".
    analogin = analogio.AnalogIn(board.A0)
    while True:
        voltage = analogin.value * 3.3 / 65536
        print('voltage:', voltage)
        time.sleep(0.1)

# ----------------------------------------------------------------------

def pot_to_freq():
    # Get analog input from the potentiometer. Left to 3V, right to
    # Ground, middle to A0 (called 1~ on the Trinket M0).
    analogin = analogio.AnalogIn(board.A0)
    # Output via the little red LED next to the USB plugin.
    led = pulseio.PWMOut(board.D13, frequency=5000, duty_cycle=0)
    # Lock in the time step, but let's vary frequency.
    wt, dt = 0, 0.01
    while True:
#        print('.')
        voltage = analogin.value * 3.3 / 65536
        # "omega" scales with voltage. Turn the knob to change the speed
        # of the flashes.
        w = voltage*10
        wt += w*dt
        led.duty_cycle = int(0.5*(math.cos(wt) + 1)*65535)
        time.sleep(dt)


oscillate_red_led(w=5)
