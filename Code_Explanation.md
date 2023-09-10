# Explanation of Raspy-Makey_MIDI Python Code

## Introduction
This Python code is designed to run on a Raspberry Pi Pico and transform it into a MIDI controller using an Adafruit MPR121 capacitive touch sensor. Below, I'll provide an explanation of each section of the code.

## Importing Libraries
```python
import board
import busio
import usb_midi
import adafruit_mpr121
```

These lines import the necessary libraries for the project:
board and busio are used for general board and bus I/O.
usb_midi is used for MIDI communication over USB.
adafruit_mpr121 is used to interact with the MPR121 capacitive touch sensor.

## Initializing I2C Interface
```python
i2c = busio.I2C(board.GP9, board.GP8)
```

This line initializes the I2C communication interface on the Raspberry Pi Pico using GPIO pins GP9 (SCL) and GP8 (SDA).

## Initialize MPR121 for Touch Sensing
```python
mpr121 = adafruit_mpr121.MPR121(i2c)
```
This line initializes the MPR121 capacitive touch sensor using the previously configured I2C interface.

## Defining MIDI Message Types and Parameters
```python
NOTE_ON = 0x90
NOTE_OFF = 0x80
MIDI_CHANNEL = 0
MIDI_PORT = usb_midi.ports[0]
```
These lines define constants for MIDI message types (NOTE_ON and NOTE_OFF), set the MIDI channel to 0, and configure the MIDI port to use the first available USB MIDI port.

## Defining MIDI Note Mappings
```python
note_mappings = {
    0: 60,
    1: 62,
    2: 64,
    3: 65,
    4: 67,
    5: 69,
    6: 71,
    7: 72,
    8: 74,
    9: 76,
    10: 77,
    11: 79,
}
```
This dictionary maps the 12 touch pads of the MPR121 to MIDI note numbers. For example, when touch pad 0 is touched, it corresponds to MIDI note 60 (C4).

## Loop to Read Touch Data and Send MIDI Messages
```python
while True:
    touch_data = mpr121.touched_pins
    for i in range(12):
        if touch_data & (1 << i):
            # Note on message
            midi_msg = [NOTE_ON | MIDI_CHANNEL, note_mappings[i], 127]
            MIDI_PORT.send_message(midi_msg)
        else:
            # Note off message
            midi_msg = [NOTE_OFF | MIDI_CHANNEL, note_mappings[i], 0]
            MIDI_PORT.send_message(midi_msg)
    time.sleep(0.01)
```
This is the main part of the code, which runs in an infinite loop. It continuously checks the touched pins on the MPR121 sensor. If a touch is detected on a specific pad, it sends a "Note On" MIDI message with the corresponding note number and velocity 127 (max velocity). When a touch is released, it sends a "Note Off" MIDI message with velocity 0 (note release). This loop runs with a 0.01-second delay between iterations.

#### The code effectively turns the Raspberry Pi Pico and MPR121 into a touch-sensitive MIDI controller, allowing you to trigger MIDI notes by touching different pads.
