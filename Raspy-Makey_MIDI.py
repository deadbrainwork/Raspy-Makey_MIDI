# Importing the required libraries
import time
import board
import busio
import usb_midi
import adafruit_mpr121

# Initializing I2C interface
i2c = busio.I2C(board.GP9, board.GP8)

# Initialize MPR121 for touch sensing
mpr121 = adafruit_mpr121.MPR121(i2c)

# Defining MIDI message types
NOTE_ON = 0x90
NOTE_OFF = 0x80

# Defining MIDI message parameters
MIDI_CHANNEL = 0
MIDI_PORT = usb_midi.ports[0]

# Defining MIDI note mappings for each touch pad,these can be customized as per your needs
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

# Loop to read touch data and send MIDI messages
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

