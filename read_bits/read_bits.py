def read_bits_from_byte(byte, first_bit_index=0, last_bit_index=7):
    if first_bit_index < 0:
        raise ValueError

    if last_bit_index < 0:
        raise ValueError

    val = byte

    val >>= 7 - last_bit_index

    bit_cnt = last_bit_index - first_bit_index + 1
    mask = (1 << bit_cnt) - 1

    val &= mask

    return val


def read_bits_from_bytearray(byte_array, first_byte_index=0, first_bit_index=0, bit_count=8):
    if first_byte_index < 0:
        raise ValueError

    if first_bit_index < 0:
        raise ValueError

    if bit_count < 0:
        raise ValueError

    val = 0

    temp_byte_index = first_byte_index

    temp_first_bit_index = first_bit_index

    # Carry first bit index over into the first byte index.
    if temp_first_bit_index > 8:
        temp_byte_index += int(temp_first_bit_index / 8)

        temp_first_bit_index %= 8

    bits_remaining = bit_count

    while bits_remaining > 0:
        bits_remaining_in_byte = min(bits_remaining, 8 - temp_first_bit_index)

        temp_last_bit_index = temp_first_bit_index + bits_remaining_in_byte - 1

        val = (val << bits_remaining_in_byte) | read_bits_from_byte(byte_array[temp_byte_index],
                temp_first_bit_index, temp_last_bit_index)

        temp_byte_index += 1
        temp_first_bit_index = 0
        bits_remaining = bits_remaining - bits_remaining_in_byte

    return val
