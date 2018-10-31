import analogio
import board
# Is this safe? The memory on this thing is TINY.
import math
import pulseio
import time

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
    import analogio
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

# ----------------------------------------------------------------------

# read_pot()

# oscillate_red_led()

pot_to_freq()
