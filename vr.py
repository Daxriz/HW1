import zipfile
import os

class VirtualFileSystem:
    def __init__(self, zip_path):
        self.filesystem = {}
        self.load_zip(zip_path)

    def load_zip(self, zip_path):
        with zipfile.ZipFile(zip_path, 'r') as zip_file:
            for name in zip_file.namelist():
                self.filesystem[name] = None  # Simplified representation

    def list_directory(self, path):
        return "\n".join([name for name in self.filesystem if name.startswith(path)])

    def change_directory(self, current, target):
        new_path = os.path.normpath(os.path.join(current, target))
        if new_path in self.filesystem or new_path == "/":
            return new_path
        raise FileNotFoundError(f"Directory not found: {target}")

    def remove_directory(self, current, name):
        dir_path = os.path.join(current, name)
        if dir_path in self.filesystem:
            del self.filesystem[dir_path]
            return "Directory removed."
        else:
            return "Directory not found."
