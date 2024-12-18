import os
import sys
import zipfile
import json
from file_system import FileSystem
from logger import Logger

class ShellEmulator:
    def __init__(self, host_name, fs_path, log_path):
        self.host_name = host_name
        self.fs_path = fs_path
        self.log_path = log_path
        self.fs = FileSystem(self.fs_path)
        self.logger = Logger(self.log_path)
        self.current_dir = self.fs.root  # Стартовая директория

    def print_prompt(self):
        return f"{self.host_name}:{self.current_dir} $ "

    def run(self):
        while True:
            try:
                command = input(self.print_prompt()).strip().lower()
                if command == "exit":
                    self.logger.log_command("exit")
                    break
                elif command.startswith("cd "):
                    self.change_directory(command[3:])
                elif command == "ls":
                    self.list_directory()
                elif command == "clear":
                    self.clear_screen()
                elif command == "pwd":
                    self.print_working_directory()
                elif command.startswith("rmdir "):
                    self.remove_directory(command[6:])
                else:
                    print("Unknown command.")
            except Exception as e:
                print(f"Error: {e}")
                self.logger.log_error(str(e))

    def change_directory(self, path):
        if path == "..":
            if self.current_dir != self.fs.root:
                self.current_dir = os.path.dirname(self.current_dir)
            self.logger.log_command(f"cd {path}")
        elif self.fs.is_directory(path):
            self.current_dir = path
            self.logger.log_command(f"cd {path}")
        else:
            print(f"cd: no such file or directory: {path}")

    def list_directory(self):
        files = self.fs.list_files(self.current_dir)
        for file in files:
            print(file)
        self.logger.log_command("ls")

    def clear_screen(self):
        os.system("clear")
        self.logger.log_command("clear")

    def print_working_directory(self):
        print(self.current_dir)
        self.logger.log_command("pwd")

    def remove_directory(self, dir_name):
        if self.fs.remove_directory(dir_name):
            print(f"rmdir: removed {dir_name}")
            self.logger.log_command(f"rmdir {dir_name}")
        else:
            print(f"rmdir: failed to remove {dir_name}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python emulator.py <host_name> <fs_zip_path> <log_path>")
        sys.exit(1)

    host_name = sys.argv[1]
    fs_path = sys.argv[2]
    log_path = sys.argv[3]
    
    emulator = ShellEmulator(host_name, fs_path, log_path)
    emulator.run()
