#!/usr/bin/python3
"""Parse HTTP log lines and display cumulative statistics."""

import sys


STATUS_CODES = ("200", "301", "400", "401",
                "403", "404", "405", "500")


def print_stats(total_size, counts):
    """Print accumulated file size and status counts."""
    print("File size: {}".format(total_size))

    for code in STATUS_CODES:
        if counts[code] > 0:
            print("{}: {}".format(code, counts[code]))

    sys.stdout.flush()


def main():
    """Read log lines from standard input."""
    total_size = 0
    counts = {code: 0 for code in STATUS_CODES}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            if len(parts) >= 2:
                try:
                    file_size = int(parts[-1])
                except ValueError:
                    pass
                else:
                    if file_size >= 0:
                        total_size += file_size

                        status = parts[-2]

                        if status in counts:
                            counts[status] += 1

            if line_count % 10 == 0:
                print_stats(total_size, counts)

    except KeyboardInterrupt:
        pass

    finally:
        print_stats(total_size, counts)


if __name__ == "__main__":
    main()
