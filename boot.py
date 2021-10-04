import sys
import machine
import sdcard
import uos
import time

print('Running Boot...')
print(sys.path)
cs = machine.Pin(9, machine.Pin.OUT)

# Intialize SPI peripheral (start with 1 MHz)
spi = machine.SPI(1,
                  baudrate=1000000,
                  polarity=0,
                  phase=0,
                  bits=8,
                  firstbit=machine.SPI.MSB,
                  sck=machine.Pin(14),
                  mosi=machine.Pin(15),
                  miso=machine.Pin(12))

# Initialize SD card
sd = sdcard.SDCard(spi, cs)

# Mount filesystem
vfs = uos.VfsFat(sd)
uos.mount(vfs, "/sd")
sys.path.append('sd')
print(sys.path)

import neopixel
neopixel.fade()
