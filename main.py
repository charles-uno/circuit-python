import adafruit_thermistor
import analogio
import array
import audiobusio
import board
import digitalio
import math
import neopixel
import pulseio
import time

# ======================================================================

NEOPIXEL = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.1, auto_write=False)

def cpe_neopixel_scale(n):
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
        NEOPIXEL[9 - i] = black if i > n else rainbow[i]
        NEOPIXEL.show()
    return

# ----------------------------------------------------------------------

def lin_to_ten(vmin, vmax, v):
    return 10*(v - vmin)/(vmax - vmin)

# ----------------------------------------------------------------------

def log_to_ten(vmin, vmax, v):
    vmin, vmax, v = [ max(1, x) for x in (vmin, vmax, v) ]
    return 10*math.log(v/vmin)/math.log(vmax/vmin)

# ======================================================================

MIC = audiobusio.PDMIn(board.MICROPHONE_CLOCK, board.MICROPHONE_DATA, sample_rate=16000, bit_depth=16)

def mic_rms(nsamples=200):
    # Use an array for memory efficiency.
    samples = array.array('H', [0] * nsamples)
    MIC.record(samples, len(samples))
    return rms(samples)

# ----------------------------------------------------------------------

def rms(vals):
    # Subtract DC offset
    offset = sum(vals)/len(vals)
    mean_square = sum( (x - offset)**2 for x in vals )/len(vals)
    return math.sqrt(mean_square)

# ----------------------------------------------------------------------

def cpe_mic_input():
    """Light up to show how loud it is."""
    # Calibrate. Assume it's quiet. Not really sure of the units.
    volume_min = mic_rms()
    volume_max = volume_min + 1000
    while True:
        # Grab a sample. Show its intensity via the neopixels.
        volume = mic_rms()
        print('VOLUME MIN, MAX, SAMPLE, SCALED:', volume_min, volume_max, volume, log_to_ten(volume_min, volume_max, volume))
        cpe_neopixel_scale( log_to_ten(volume_min, volume_max, volume) )
        time.sleep(0.05)

# ======================================================================

EYE = analogio.AnalogIn(board.LIGHT)

def cpe_light_input():
    """Light up to show how bright it is"""
    # Not sure of the units, but right up to a light bulb is 60k.
    while True:
        brightness = EYE.value
        print('%6f' % brightness, log_to_ten(500, 50000, brightness))
        cpe_neopixel_scale(log_to_ten(500, 50000, brightness))
        time.sleep(0.1)

# ======================================================================

THERMISTOR = thermistor = adafruit_thermistor.Thermistor(board.TEMPERATURE, 10000, 10000, 25, 3950)

def cpe_temp_input():
    """Light up to show how warm it is."""
    while True:
        temp = THERMISTOR.temperature
        print('Temperature:', temp)
        cpe_neopixel_scale(log_to_ten(20, 40, temp))
        time.sleep(0.1)

# ======================================================================

# cpe_mic_input()

# cpe_light_input()

cpe_temp_input()




# ######################################################################

# Scratch work below here...





def cpe_mouse():
    mouse = mouse.Mouse()

    analogin = analogio.AnalogIn(board.A0)

    while True:
        voltage = analogin.value * 3.3 / 65536
        print('voltage:', voltage)

        mouse.move(x=voltage)

        time.sleep(0.1)






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
