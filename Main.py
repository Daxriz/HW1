import argparse
from gui import ShellGUI
from logger import Logger
from virtual_fs import VirtualFileSystem
from shell_emulator import ShellEmulator

def main():
    parser = argparse.ArgumentParser(description="Shell Emulator")
    parser.add_argument("--hostname", required=True, help="Computer hostname for shell prompt")
    parser.add_argument("--fs", required=True, help="Path to virtual filesystem ZIP archive")
    parser.add_argument("--log", required=True, help="Path to log file")

    args = parser.parse_args()

    # Initialize components
    logger = Logger(args.log)
    vfs = VirtualFileSystem(args.fs)
    shell = ShellEmulator(args.hostname, vfs, logger)

    # Start GUI
    gui = ShellGUI(shell)
    gui.run()

if __name__ == "__main__":
    main()
