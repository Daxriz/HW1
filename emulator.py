import os
import zipfile
import json
import tkinter as tk
from tkinter import messagebox
from fs_utils import VirtualFileSystem, FileSystemCommandHandler

class ShellEmulator:
    def __init__(self, hostname, zip_file, log_file):
        self.hostname = hostname
        self.vfs = VirtualFileSystem(zip_file)
        self.log_file = log_file
        self.command_handler = FileSystemCommandHandler(self.vfs, self.log_file)
        self.current_dir = "/"

    def run(self):
        # Инициализация GUI
        root = tk.Tk()
        root.title(f"Shell Emulator - {self.hostname}")

        # Окно вывода и ввода команд
        self.output_text = tk.Text(root, height=20, width=80)
        self.output_text.pack()

        self.input_entry = tk.Entry(root, width=80)
        self.input_entry.bind("<Return>", self.process_command)
        self.input_entry.pack()

        # Инициализация интерфейса
        self.display_prompt()
        root.mainloop()

    def process_command(self, event):
        command = self.input_entry.get().strip()
        self.input_entry.delete(0, tk.END)
        if command:
            output = self.command_handler.execute(command)
            self.display_output(output)

    def display_output(self, output):
        self.output_text.insert(tk.END, output + '\n')
        self.display_prompt()

    def display_prompt(self):
        prompt = f"{self.hostname}:{self.current_dir}$ "
        self.output_text.insert(tk.END, prompt)
        self.output_text.yview(tk.END)

if __name__ == "__main__":
    # Пример использования
    emulator = ShellEmulator(
        hostname="localhost", 
        zip_file="path/to/virtual_filesystem.zip", 
        log_file="path/to/log.json"
    )
    emulator.run()
