#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total_args = 0
    for arg in range(1, len(sys.argv)):
        total_args += int(sys.argv[arg])
    print("{}".format(total_args))
