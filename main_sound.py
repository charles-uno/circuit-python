
import array
import audiobusio
import board
import math
import time

import helpers

# ======================================================================

MIC = audiobusio.PDMIn(board.MICROPHONE_CLOCK, board.MICROPHONE_DATA, sample_rate=16000, bit_depth=16)

def main():
    """Light up to show how loud it is."""
    # Calibrate. Assume it's quiet. Not really sure of the units.
    volume_min = mic_rms()
    volume_max = volume_min + 1000
    while True:
        # Grab a sample. Show its intensity via the neopixels.
        volume = mic_rms()
        print('Volume RMS:', volume)
        helpers.cpe_log_show(volume_min, volume_max, volume)
        time.sleep(0.05)

# ----------------------------------------------------------------------

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

# ======================================================================

main()
