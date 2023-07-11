#!/usr/bin/python3
"""
Script for log parsing
"""
import sys

if __name__ == "__main__":
    log_entries = []
    status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    status_code_counts = {code: 0 for code in status_codes}
    entry_count = 0
    total_file_size = 0

    try:
        for line in sys.stdin:
            log_entry = line.split(" ")
            if "\n" in log_entry[-1]:
                file_size = log_entry[-1][:-1]
            else:
                file_size = log_entry[-1]
            if (
                len(log_entry) > 2
                and log_entry[-2] in status_codes
                and file_size.isnumeric()
            ):
                status_code_counts[log_entry[-2]] += 1
                total_file_size += int(file_size)
                entry_count += 1
            if entry_count % 10 == 0:
                print(f"Total File Size: {total_file_size}")
                for code in status_codes:
                    if status_code_counts[code] > 0:
                        print(f"{code}: {status_code_counts[code]}")
        exit()
    except Exception:
        pass
    finally:
        print(f"Total File Size: {total_file_size}")
        for code in status_codes:
            if status_code_counts[code] > 0:
                print(f"{code}: {status_code_counts[code]}")
