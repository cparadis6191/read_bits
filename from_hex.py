#!/usr/bin/env python3

import binascii
import sys

from read_bits.read_bits import *


if __name__ == '__main__':
    hex_string = sys.stdin.readlines()

    clean_hex_string = ''.join(hex_string).rstrip().replace(
        '0x', '').replace('\n', '').replace(' ', '')

    # Pad out to an even number of hex digits to work with binascii.unhexlify.
    if (len(clean_hex_string) & 1) == 1:
        clean_hex_string = '0' + clean_hex_string

    byte_list = binascii.unhexlify(
        ('0' if (len(clean_hex_string) & 1) == 1 else '') + clean_hex_string)

    # Indices
    out_index_list = [str(byte).ljust(8) for byte in list(range(len(byte_list)))]

    print(' '.join(out_index_list))

    # Char
    out_char_list = []

    for byte in byte_list:
        char = chr(byte)
        # Non-printable characters are replace with a Unicode replacement
        # character.
        out_char_list.append((char if char.isprintable() else u'\ufffd').ljust(8))

    print(' '.join(out_char_list))

    # Hex
    out_hex_string_list = [''.join(
        [format(byte, '02x')[0].ljust(4),
            format(byte, '02x')[1].ljust(4)]) for byte in byte_list]

    print(' '.join(out_hex_string_list))

    # Bits
    out_bits_string_list = [format(byte, '08b') for byte in byte_list]

    print(' '.join(out_bits_string_list))
