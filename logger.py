import json
import os

class Logger:
    def __init__(self, log_path):
        self.log_path = log_path

    def log(self, command):
        log_entry = {"command": command}
        with open(self.log_path, "a") as log_file:
            json.dump(log_entry, log_file)
            log_file.write("\n")
