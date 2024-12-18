import zipfile
import os

class VirtualFileSystem:
    def __init__(self, zip_path):
        self.zip_path = zip_path
        self.current_path = "/"
        self.virtual_fs = {}
        self.load_zip()

    def load_zip(self):
        """Загрузка содержимого ZIP-архива в виртуальную файловую систему"""
        with zipfile.ZipFile(self.zip_path, 'r') as zip_ref:
            for file in zip_ref.namelist():
                self.virtual_fs[file] = None  # Эмуляция содержимого архива
        print("Виртуальная файловая система загружена.")

    def list_dir(self, path):
        """Возвращает список файлов и директорий в заданной директории"""
        result = []
        print(f"Список файлов для пути '{path}':")  # Отладочный вывод
        for file in self.virtual_fs:
            if file.startswith(path) and file != path:
                sub_path = file[len(path):].strip("/")
                print(f"  - {file} (subpath: {sub_path})")  # Отладочная информация
                if "/" not in sub_path:
                    result.append(sub_path)
        if result:
            return result
        else:
            return ["Пусто."]
    
    def change_dir(self, path):
        """Меняет текущую директорию на указанную"""
        print(f"Попытка смены директории на: {path}")  # Отладочный вывод
        if path == "/":
            self.current_path = "/"
        elif any(file.startswith(path) for file in self.virtual_fs):
            self.current_path = path.rstrip("/") + "/"
        else:
            raise FileNotFoundError("Директория не найдена.")
