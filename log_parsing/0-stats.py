#!/usr/bin/python3
"""Read HTTP logs from stdin and calculate statistics."""

import re
import sys


VALID_CODES = (200, 301, 400, 401, 403, 404, 405, 500)

LOG_PATTERN = re.compile(
    r'^((?:[0-9]{1,3}\.){3}[0-9]{1,3}) - '
    r'\[[^\]]+\] "GET /projects/260 HTTP/1\.1" '
    r'([0-9]+) ([0-9]+)$'
)


def print_statistics(total_size, status_counts):
    """Print total file size and status code counts."""
    print("File size: {}".format(total_size))

    for code in VALID_CODES:
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


def main():
    """Process input logs and display statistics."""
    total_size = 0
    line_count = 0
    status_counts = {code: 0 for code in VALID_CODES}

    try:
        for line in sys.stdin:
            line_count += 1
            match = LOG_PATTERN.match(line.rstrip("\r\n"))

            if match:
                ip_address = match.group(1)
                octets = ip_address.split(".")

                if all(int(octet) <= 255 for octet in octets):
                    status_code = int(match.group(2))
                    file_size = int(match.group(3))

                    total_size += file_size

                    if status_code in status_counts:
                        status_counts[status_code] += 1

            if line_count % 10 == 0:
                print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)

    else:
        if line_count % 10 != 0:
            print_statistics(total_size, status_counts)


if __name__ == "__main__":
    main()
