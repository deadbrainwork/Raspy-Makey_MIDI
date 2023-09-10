# Raspy-Makey_MIDI
A Super Simple Raspberry Pi Pico based Makey Makey Clone/MIDI Controller

![Raspy-Makey](raspy-makey-logo.png)

Raspy-Makey is a super simple Raspberry Pi Pico-based Makey Makey clone that doubles as a MIDI controller while adding 6 more inputs than the original without the need of EARTH/GND connector. With Raspy-Makey, you can turn everyday objects into touch-sensitive input devices and use them to trigger MIDI notes, allowing you to create music in a unique and interactive way. It uses a Raspberry Pi Pico along with an Adafruit MPR121 capacitive touch sensor to create a MIDI controller. The script reads touch data from the MPR121 and sends MIDI messages accordingly.

Fun Fact-I originally made this as a fun project for my 5 yr old nephew to play and learn music with back in July 2022.

## Prerequisites
Before running this script, make sure you have the following hardware and software prerequisites:
- Raspberry Pi (any model with GPIO pins should work).
- Adafruit MPR121 capacitive touch sensor.
- Appropriate connections between Raspberry Pi and MPR121 using Jumper cables or breadboard or using the custom toner transfer PCB file included with this.
- Python 3 or newer installed on your computer.
- Thonny to upload the code.
- Adafruit Blinka library installed.
- Adafruit CircuitPython MPR121 library installed.
- Adafruit CircuitPython MIDI library installed.

## Installation

1. Connect your Raspberry Pi Pico to your computer using a USB cable.

2. Open Thonny IDE or your preferred Python development environment.

3. Create a new Python script and copy the provided code into the script.

4. Run the script by clicking the "Run" button in Thonny to check if your device is working as expected.

5. Save the script with a `.py` extension (e.g., `raspy_makey.py`) on your Raspberry Pi Pico to make it a plug and play device.

## Usage

1. Connect your conductive materials (such as alligator clips) to the MPR121’s pins, ensuring they correspond to the touch pads defined in the `note_mappings` dictionary in the code.

2. When you touch any of the connected conductive materials, Raspy-Makey will send MIDI note messages to your computer. You can use these MIDI notes in your favorite digital audio workstation (DAW) or music software to create/play music.

3. Customize the `note_mappings` dictionary to assign different MIDI notes to each touch pad as desired.

## Troubleshooting

- If the Raspy-Makey does not respond when you touch the conductive materials, double-check your connections and ensure that you have correctly assigned the pins in the `note_mappings` dictionary or reconnect the device.

- Make sure you have the necessary Python libraries (e.g., `adafruit_mpr121`, `usb_midi`) installed on your Raspberry Pi Pico. You can use the [Adafruit CircuitPython library manager](https://circuitpython.org/libraries) to install missing libraries.

- Ensure that your computer recognizes the Raspberry Pi Pico as a MIDI device. You may need to configure your DAW or MIDI software to use the Raspberry Pi Pico as a MIDI input.

## License

This project is licensed under the CC License - see the [LICENSE](LICENSE) file for details.

## Credits

This project was inspired by the original Makey Makey.

Happy hacking and music-making with Raspy-Makey!


