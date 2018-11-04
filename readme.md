# Circuit Python

Playing with the **Circuit Playground Express**! No guarantee that anything here will work with any other model.

The file system on these things can be a bit flaky. Seems safer to work locally then copy files over. That also makes it easy to swap around `main.py` without losing the old one.

## Quick Start

Plug in the board via USB. It should appear like a thumb drive. Copy `helpers.py` onto it. Also choose one of the `main_whatever.py`, rename it `main.py`, and copy it over.

Take a peek inside `main.py` to see what it does. Usually they're pretty self-explanatory. For example:

- `main_sound.py` lights up to show how loud it is.
- `main_temperature.py` lights up to show how warm it is.
- `main_orientation.py` lights up to show which way is up.

## Libraries

Some of the examples, for example any that do mouse emulation, require CircuitPython libraries. Download the bundle [here](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/). Extract the ZIP file and copy the `lib` folder onto the board.

The library version needs to match the firmware version. To see what firmware version you're running, connect a shell to the board (see below) and hit Ctrl-C to enter the REPL:

```
Press any key to enter the REPL. Use CTRL-D to reload.
Adafruit CircuitPython 4.0.0-alpha.2 on 2018-10-16; Adafruit CircuitPlayground Express with Crickit libraries with samd21g18
>>>
```

The version above is `4.0.0-alpha.2`, so it would work with the `4.x` library bundle.

## The REPL

The REPL is basically a shell on the board. It shows output, including error tracebacks, and allows you to interrupt (and get a prompt) via Ctrl-C. On Linux, you can connect to the shell via your terminal. First, do `ls /dev/tty*` and look for `/dev/ttyACM0` or similar. Then connect to that via:

```
sudo screen /dev/ttyACM0 115200
```

Above, 115200 is a bit rate, which is the same for all CircuitPython boards.

You can also connect to the REPL via Mu, the recommended code editor for CircuitPython. On Linux, you can install Mu using Pip:

```
pip3.6 install -y mu-editor
```

Note that CircuitPython works only with Python 3, and Mu in particular doesn't get along with Python 3.5 (the default on Ubuntu 16).

To open the REPL from within Mu, click the "Serial" button. Note that the REPL will only work if you're running Mu as an administrator (or using `sudo`).

## Firmware and Troubleshooting

If you plug in your Circuit Playground Express and don't see a `main.py`, it's probably running firmware for C arduino code or something. To switch it to CircuitPython, you'll want to update the firmware. You can also update the firmware to try to get rid of any weird problems you're having (freezes, filesystem issues, etc).

Double-press the (physical) reset button on the board. It's small, right in the middle. The lights will change color, and you'll see a USB device with some `.uf2` files on it.

Download the new `.uf2` file you want from [here](https://github.com/adafruit/circuitpython/releases), then drag it into the USB drive. It'll automatically flash itself and restart. If it comes back in bootloader mode again, something didn't work -- maybe you grabbed the wrong version.

## Links

- [CircuitPython Documentation](https://learn.adafruit.com/adafruit-circuit-playground-express)
- [CircuitPython Guides](https://learn.adafruit.com/category/circuit-playground)


---

## TODO

- IR blaster. This can apparently also be a proximity sensor?
- Keyboard emulation
- Sound output
- Use slide switch and buttons
