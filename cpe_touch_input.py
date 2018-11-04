
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
            if touch.value:
                helpers.chase_advance(channel)
            else:
                helpers.chase_clear(channel)
        time.sleep(0.1)

# ======================================================================

cpe_touch_input()









def speaker_init():
    global SPEAKER
    speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
    speaker_enable.direction = digitalio.Direction.OUTPUT
    speaker_enable.value = True
    SPEAKER = audioio.AudioOut(board.A0)
    return

def get_wave(f, n=100):
    wave = array.array("H", [0] * 100)
    dt = 1./SAMPLE_RATE
    for i in range( len(wave) ):
        wave[i] += int(math.sin(2*math.pi*f*dt*i) * 2**15)
    return wave


def play_tone(waves, duration=0.1):
    if SPEAKER is None:
        speaker_init()
    wave_sum = waves.pop()
    while waves:
        for i, w in enumerate(waves.pop()):
            wave_sum[i] += w
    wave_sample = audioio.RawSample(wave_sum)
    SPEAKER.play(wave_sample, loop=True)
    time.sleep(duration)
    return SPEAKER.stop()




    omegas = [ 2*math.pi*x for x in freqs ]
    wave = array.array("H", [0] * 100)
    dt = 1./SAMPLE_RATE
    for w in omegas:
        for i in range( len(wave) ):
            wave[i] += int(math.sin(w*dt*i) * 2**15)
    wave_sample = audioio.RawSample(wave)
    SPEAKER.play(wave_sample, loop=True)
    time.sleep(duration)
    SPEAKER.stop()
    return

TOUCHES = [
    touchio.TouchIn(board.A1),
    touchio.TouchIn(board.A2),
    touchio.TouchIn(board.A3),
    touchio.TouchIn(board.A4),
]

FREQS = [
    get_wave(440),
    get_wave(580),
    get_wave(720),
    get_wave(860),
]


while True:
    freqs = []
    for touch, freq in zip(TOUCHES, FREQS):
        if touch.value:
            freqs.append(freq)
    if freqs:
        play_tone(freqs)
    time.sleep(0.1)











import adafruit_lis3dh
import adafruit_thermistor
import analogio
import audiobusio
import board
import busio
import digitalio
import math
import pulseio
import time





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
