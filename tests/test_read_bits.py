import unittest

from read_bits.read_bits import *


class Test(unittest.TestCase):

    def test_read_bits_from_byte(self):
        self.assertEqual(read_bits_from_byte(0xff), 0xff)

        self.assertEqual(read_bits_from_byte(0xff, 0, 7), 0xff)
        self.assertEqual(read_bits_from_byte(0xff, 1, 7), 0x7f)
        self.assertEqual(read_bits_from_byte(0xff, 2, 7), 0x3f)
        self.assertEqual(read_bits_from_byte(0xff, 3, 7), 0x1f)
        self.assertEqual(read_bits_from_byte(0xff, 4, 7), 0x0f)
        self.assertEqual(read_bits_from_byte(0xff, 5, 7), 0x07)
        self.assertEqual(read_bits_from_byte(0xff, 6, 7), 0x03)
        self.assertEqual(read_bits_from_byte(0xff, 7, 7), 0x01)

        self.assertEqual(read_bits_from_byte(0xff, 0, 7), 0xff)
        self.assertEqual(read_bits_from_byte(0xff, 0, 6), 0x7f)
        self.assertEqual(read_bits_from_byte(0xff, 0, 5), 0x3f)
        self.assertEqual(read_bits_from_byte(0xff, 0, 4), 0x1f)
        self.assertEqual(read_bits_from_byte(0xff, 0, 3), 0x0f)
        self.assertEqual(read_bits_from_byte(0xff, 0, 2), 0x07)
        self.assertEqual(read_bits_from_byte(0xff, 0, 1), 0x03)
        self.assertEqual(read_bits_from_byte(0xff, 0, 0), 0x01)

        self.assertEqual(read_bits_from_byte(0b00010101, 0, 0), 0b0)
        self.assertEqual(read_bits_from_byte(0b00010101, 0, 2), 0b000)
        self.assertEqual(read_bits_from_byte(0b00010101, 0, 3), 0b0001)
        self.assertEqual(read_bits_from_byte(0b00010101, 0, 4), 0b00010)
        self.assertEqual(read_bits_from_byte(0b00010101, 0, 5), 0b000101)
        self.assertEqual(read_bits_from_byte(0b00010101, 0, 6), 0b0001010)
        self.assertEqual(read_bits_from_byte(0b00010101, 0, 7), 0b00010101)

        self.assertEqual(read_bits_from_byte(0b00010101, 7, 7), 0b1)
        self.assertEqual(read_bits_from_byte(0b00010101, 6, 7), 0b01)
        self.assertEqual(read_bits_from_byte(0b00010101, 5, 7), 0b101)
        self.assertEqual(read_bits_from_byte(0b00010101, 4, 7), 0b0101)
        self.assertEqual(read_bits_from_byte(0b00010101, 3, 7), 0b10101)
        self.assertEqual(read_bits_from_byte(0b00010101, 2, 7), 0b010101)
        self.assertEqual(read_bits_from_byte(0b00010101, 1, 7), 0b0010101)
        self.assertEqual(read_bits_from_byte(0b00010101, 0, 7), 0b00010101)

        self.assertEqual(read_bits_from_byte(0b00010101, 4, 4), 0b0)
        self.assertEqual(read_bits_from_byte(0b00010101, 4, 5), 0b01)
        self.assertEqual(read_bits_from_byte(0b00010101, 3, 5), 0b101)
        self.assertEqual(read_bits_from_byte(0b00010101, 3, 6), 0b1010)
        self.assertEqual(read_bits_from_byte(0b00010101, 2, 6), 0b01010)
        self.assertEqual(read_bits_from_byte(0b00010101, 2, 7), 0b010101)
        self.assertEqual(read_bits_from_byte(0b00010101, 1, 7), 0b0010101)
        self.assertEqual(read_bits_from_byte(0b00010101, 0, 7), 0b00010101)


    def test_read_bits_from_bytearray(self):
        self.assertEqual(read_bits_from_bytearray(bytearray([0x75, 0x57]), 0, 2, 8), 0xd5)

        self.assertEqual(read_bits_from_bytearray(bytearray([0x00, 0xff, 0xff]), 1, 0, 16), 0xffff)

        self.assertEqual(read_bits_from_bytearray(bytearray([0x01, 0x80]), 0, 7, 2), 0x3)
        self.assertEqual(read_bits_from_bytearray(bytearray([0x01, 0x80]), 0, 6, 3), 0x3)
        self.assertEqual(read_bits_from_bytearray(bytearray([0x01, 0x80]), 0, 5, 4), 0x3)
        self.assertEqual(read_bits_from_bytearray(bytearray([0x01, 0x80]), 0, 4, 5), 0x3)
        self.assertEqual(read_bits_from_bytearray(bytearray([0x01, 0x80]), 0, 3, 6), 0x3)


if __name__ == '__main__':
    unittest.main()
