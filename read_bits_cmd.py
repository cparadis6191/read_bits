#!/usr/bin/env python3

import argparse
import binascii
import sys

from read_bits.read_bits import *


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument(
            'first_byte_index', metavar='first_byte_index', type=int)

    arg_parser.add_argument(
            'first_bit_index', metavar='first_bit_index', type=int)

    arg_parser.add_argument(
            'bit_count', metavar='bit_count', type=int)

    parsed_args = arg_parser.parse_args()

    hex_string = ''.join(sys.stdin.readlines()).rstrip().replace(
            '\n', '').replace(' ', '')

    print(hex(read_bits_from_bytearray(
        binascii.unhexlify(hex_string),
        parsed_args.first_byte_index,
        parsed_args.first_bit_index,
        parsed_args.bit_count)))
