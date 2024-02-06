# Author: Renzo Mischianti
# Website: www.mischianti.org
#
# Description:
# This script initializes the E32 LoRa module with CircuitPython, retrieves the current configuration, and prints it to the console.
# The code demonstrates how to use the LoRaE32 library to interact with the module and read its configuration.
#
# Note: This code was written and tested using CircuitPython on an ESP32 board.
#       It works with other boards, but you may need to change the UART pins.


import board
import busio
from microcontroller import Pin

from lora_e32 import LoRaE32, print_configuration
from lora_e32_operation_constant import ResponseStatusCode

# Create a UART object to communicate with the LoRa module with ESP32
uart2 = busio.UART(board.TX2, board.RX2, baudrate=9600)
# Create a LoRaE32 object, passing the UART object and pin configurations
lora = LoRaE32('433T20D', uart2, aux_pin=board.D15, m0_pin=board.D21, m1_pin=board.D19)

# Create a UART object to communicate with the LoRa module with Raspberry Pi Pico
# uart2 = busio.UART(board.TX1, board.RX1, baudrate=9600)
# Use the Serial1 pins of Arduino env on the Raspberry Pi Pico
# uart2 = busio.UART(board.D9, board.D8, baudrate=9600)
# lora = LoRaE32('433T20D', uart2, aux_pin=board.D2, m0_pin=board.D10, m1_pin=board.D11)
# STM32F411CEU6 Shield
# uart2 = busio.UART(board.TX2, board.RX2, baudrate=9600)
# lora = LoRaE32('433T20D', uart2, aux_pin=board.PA0, m0_pin=board.PB0, m1_pin=board.PB2)

code = lora.begin()
print("Initialization: {}", ResponseStatusCode.get_description(code))

code, configuration = lora.get_configuration()

print("Retrieve configuration: {}", ResponseStatusCode.get_description(code))

print_configuration(configuration)

# Initialization: {} Success
# Retrieve configuration: {} Success
# ----------------------------------------
# HEAD : 0b11000000 192
#
# AddH : 0
# AddL : 0
# Chan : 23  ->  433
#
# SpeedParityBit    : 0b0  ->  8N1 (Default)
# SpeedUARTDatte : 0b11  ->  9600bps (default)
# SpeedAirDataRate  : 0b10  ->  2.4kbps (default)
# OptionTrans       : 0b0  ->  Transparent transmission (default)
# OptionPullup      : 0b1  ->  TXD, RXD, AUX are push-pulls/pull-ups (default)
# OptionWakeup      : 0b0  ->  250ms (default)
# OptionFEC         : 0b1  ->  Turn on Forward Error Correction Switch (Default)
# OptionPower       : 0b0  ->  20dBm (Default)
# ----------------------------------------
# CircuitPython v1.19.1 on 2022-06-18; ESP32 module with ESP32
