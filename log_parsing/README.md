# Log Parsing

## Description

A Python script that reads HTTP access logs from standard input
and calculates statistics.

## Features

- Reads log entries from stdin.
- Validates the required log format.
- Calculates the total file size.
- Counts valid HTTP status codes.
- Prints statistics after every 10 input lines.
- Prints statistics when interrupted with Ctrl+C.
- Handles incomplete batches at end of input.
- Uses Python 3.4 compatible syntax.

## Usage

```bash
./0-stats.py
```

## Requirements

- Ubuntu 14.04 LTS
- Python 3.4.3
- PEP 8 style
