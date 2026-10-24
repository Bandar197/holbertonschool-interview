#!/usr/bin/python3
"""UTF-8 validation."""


def validUTF8(data):
    """Return True if the data contains valid UTF-8 bytes."""
    data = [value & 0xFF for value in data]
    pos = 0
    while pos < len(data):
        first = data[pos]
        if first <= 0x7F:
            size = 1
        elif 0xC2 <= first <= 0xDF:
            size = 2
        elif 0xE0 <= first <= 0xEF:
            size = 3
        elif 0xF0 <= first <= 0xF4:
            size = 4
        else:
            return False
        if pos + size > len(data):
            return False
        for index in range(1, size):
            if data[pos + index] & 0xC0 != 0x80:
                return False
        if size > 1:
            second = data[pos + 1]
            if first == 0xE0 and second < 0xA0:
                return False
            if first == 0xED and second > 0x9F:
                return False
            if first == 0xF0 and second < 0x90:
                return False
            if first == 0xF4 and second > 0x8F:
                return False
        pos += size
    return True
