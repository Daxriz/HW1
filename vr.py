import zipfile
import os

class VirtualFileSystem:
    def __init__(self, zip_path):
        self.zip_path = zip_path
        self.current_path = "/"
        self.virtual_fs = {}
        self.load_zip()

    def load_zip(self):
        with zipfile.ZipFile(self.zip_path, 'r') as zip_ref:
            for file in zip_ref.namelist():
                self.virtual_fs[file] = None  # Эмуляция содержимого
        print("Виртуальная файловая система загружена.")

    def list_dir(self, path):
        result = []
        for file in self.virtual_fs:
            if file.startswith(path) and file != path:
                sub_path = file[len(path):].strip("/")
                if "/" not in sub_path:
                    result.append(sub_path)
        return result

    def change_dir(self, path):
        if path == "/":
            self.current_path = "/"
        elif any(file.startswith(path) for file in self.virtual_fs):
            self.current_path = path.rstrip("/") + "/"
        else:
            raise FileNotFoundError("Директория не найдена.")

    def remove_dir(self, path):
        keys_to_remove = [file for file in self.virtual_fs if file.startswith(path)]
        if keys_to_remove:
            for key in keys_to_remove:
                del self.virtual_fs[key]
        else:
            raise FileNotFoundError("Директория не найдена.")
