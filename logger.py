import json
from datetime import datetime

class Logger:
    def __init__(self, log_path):
        self.log_path = log_path

    def log_command(self, command):
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "command": command,
            "status": "success"
        }
        self.write_log(log_entry)

    def log_error(self, error):
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "error": error,
            "status": "error"
        }
        self.write_log(log_entry)

    def write_log(self, log_entry):
        with open(self.log_path, 'a') as log_file:
            json.dump(log_entry, log_file)
            log_file.write("\n")
