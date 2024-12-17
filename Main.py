import sys
import json
from shell_emulator import ShellEmulator

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <hostname> <zip_filepath> <log_filepath>")
        return

    hostname = sys.argv[1]
    zip_filepath = sys.argv[2]
    log_filepath = sys.argv[3]

    emulator = ShellEmulator(hostname, zip_filepath, log_filepath)
    emulator.run()

if __name__ == "__main__":
    main()
