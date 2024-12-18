import zipfile
import os
import io

class FileSystem:
    def __init__(self, zip_path):
        self.zip_path = zip_path
        self.files = self.load_filesystem(zip_path)
        self.root = "/"

    def load_filesystem(self, zip_path):
        files = {}
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            for file in zip_ref.namelist():
                files[file] = zip_ref.read(file)
        return files

    def is_directory(self, path):
        # Простейшая проверка: если директория существует в архиве
        return path in self.files

    def list_files(self, dir_path):
        return [file for file in self.files if file.startswith(dir_path)]

    def remove_directory(self, dir_name):
        # Удаляем только пустую директорию
        if dir_name in self.files:
            del self.files[dir_name]
            return True
        return False
