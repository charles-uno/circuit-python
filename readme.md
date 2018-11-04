# Circuit Python

Playing with the **Circuit Playground Express**! No guarantee that anything here will work with any other model.

The file system on these things can be a bit flaky. Seems safer to work locally then copy files over. That also makes it easy to swap around `main.py` without losing the old one.

## Mu and the REPL

The REPL is basically a shell on the board. It shows output, and allows you to interrupt (and get a prompt) via Ctrl-C.

The recommended editor is Mu. You can install it on Ubuntu with:

```
pip3.6 install -y mu-editor
```

Note that CircuitPython is exclusively for Python 3, and the Mu editor in particular doesn't get along with Python 3.5 (the default on Ubuntu 16). Mu has a built-in shell that'll connect to the REPL. To use this feature, you must run Mu with `sudo`.

Mu uses large font, and the REPL takes up a lot of the screen, so it's not great on laptops. Instead, I prefer to use Atom, then connect to the REPL directly from the shell. To do so, do `ls /dev/tty*` and look for `ttyACM0` or similar. Then connect to that via:

```
sudo screen /dev/ttyACM0 115200
```

The number `115200` is a bit rate, and is the same for all CircuitPython boards.

## Running Code

When you plug in the board, it should look like a thumb drive containing the file `main.py`. You can modify or replace that file. As soon as `main.py` changes, the board will automatically reload it and start running the new one.

Output is printed to the REPL. If something goes wrong, that's where you'll get a traceback.

## Flashing the Boot Loader

If something goes wrong, or if you want to update your firmware, double-press the (physical) reset button on the board. It's small, right in the middle. The lights will change color, and you'll see a USB device with some `.uf2` files on it.

Download the new `.uf2` file you want from [here](https://github.com/adafruit/circuitpython/releases), then drag it into the USB drive. It'll automatically flash itself and restart. If it comes back in bootloader mode again, something didn't work -- maybe you grabbed the wrong version.

## Libraries

Libraries go in a folder named `lib`. If it doesn't exist, you can create it yourself. You'll need to track down libraries for some advanced functionality, such as keyboard and mouse emulation. Get them [here](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/tag/20181030).

## Links

- [CircuitPython Documentation](https://learn.adafruit.com/adafruit-circuit-playground-express/circuitpython-analog-out-2)
