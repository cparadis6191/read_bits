#!/usr/bin/env python3

import sys

from read_bits.read_bits import *


if __name__ == '__main__':
    bits_string = sys.stdin.readlines()

    hex_string = format(int(''.join(bits_string).replace(
        '0b', '').replace('\n', '').replace(' ', ''), 2), 'x')

    # Pad out to an even number of hex digits to work with binascii.unhexlify.
    if (len(hex_string) & 1) == 1:
        hex_string = '0' + hex_string

    print('0x' + hex_string)
