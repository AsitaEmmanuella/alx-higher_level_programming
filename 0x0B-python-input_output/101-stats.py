#!/usr/bin/python3
import sys

def parse_line(line):
    parts = line.split()
    return parts[-2], int(parts[-1])

def print_stats(file_size, status_counts):
    print(f"File size: {file_size}")
    for status, count in sorted(status_counts.items()):
        print(f"{status}: {count}")

def main():
    file_size = 0
    status_counts = {}

    try:
        for line in sys.stdin:
            status, size = parse_line(line)
            file_size += size
            status_counts[status] = status_counts.get(status, 0) + 1
            if len(status_counts) == 10:  # Assuming only 10 unique status codes
                print_stats(file_size, status_counts)
                status_counts.clear()
                file_size = 0
    except KeyboardInterrupt:
        print_stats(file_size, status_counts)

if __name__ == "__main__":
    main()

