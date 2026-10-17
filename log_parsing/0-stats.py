#!/usr/bin/python3
"""Read HTTP access logs and print cumulative statistics."""

import re
import sys


STATUS_CODES = (200, 301, 400, 401, 403, 404, 405, 500)

LOG_PATTERN = re.compile(
    r'^(\d{1,3}(?:\.\d{1,3}){3}) - '
    r'\[[^\]\r\n]+\] "GET /projects/260 HTTP/1\.1" '
    r'(\d+) (\d+)$'
)


def print_stats(total_size, counts):
    """Display the total file size and status code counts."""
    print("File size: {}".format(total_size))

    for code in STATUS_CODES:
        if counts[code] > 0:
            print("{}: {}".format(code, counts[code]))

    sys.stdout.flush()


def main():
    """Process log lines and display cumulative statistics."""
    total_size = 0
    counts = {code: 0 for code in STATUS_CODES}
    lines_seen = 0

    try:
        for line in sys.stdin:
            lines_seen += 1
            match = LOG_PATTERN.match(line.strip())

            if match is not None:
                octets = match.group(1).split(".")

                if all(int(octet) <= 255 for octet in octets):
                    status = int(match.group(2))
                    total_size += int(match.group(3))

                    if status in counts:
                        counts[status] += 1

            if lines_seen % 10 == 0:
                print_stats(total_size, counts)

    except KeyboardInterrupt:
        pass

    finally:
        print_stats(total_size, counts)


if __name__ == "__main__":
    main()
