# Author: Renzo Mischianti
# Website: www.mischianti.org
#
# Description:
# This script demonstrates how to use the E32 LoRa module with CircuitPython.
# It includes examples of sending and receiving string using both transparent and fixed transmission modes.
# The code also configures the module's address and channel for fixed transmission mode.
# Address and channel of this receiver:
# ADDH = 0x00
# ADDL = 0x01
# CHAN = 23
#
# Can be used with the send_fixed_string and send_transparent_string scripts
#
# Note: This code was written and tested using CircuitPython on an ESP32 board.
#       It works with other boards, but you may need to change the UART pins.

import busio
import board

import time

from lora_e32 import LoRaE32, Configuration
from lora_e32_operation_constant import ResponseStatusCode

from lora_e32_constants import FixedTransmission, RssiEnableByte

# Initialize the LoRaE32 module
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

# Set the configuration to default values and print the updated configuration to the console
# Not needed if already configured
configuration_to_set = Configuration('433T20D')
configuration_to_set.ADDL = 0x01 # Address of this receive no sender
configuration_to_set.OPTION.fixedTransmission = FixedTransmission.FIXED_TRANSMISSION
code, confSetted = lora.set_configuration(configuration_to_set)
print("Set configuration: {}", ResponseStatusCode.get_description(code))

print("Waiting for messages...")
while True:
    if lora.available() > 0:
        code, value = lora.receive_message()
        print(ResponseStatusCode.get_description(code))

        print(value)
        utime.sleep_ms(2000)
