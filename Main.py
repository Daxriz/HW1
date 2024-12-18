import zipfile
import os
import json

class VirtualFileSystem:
    def __init__(self, zip_path):
        self.zip_path = zip_path
        self.mount()

    def mount(self):
        # Распаковка архива в временную директорию
        self.temp_dir = "/tmp/vfs"  # Пример временной директории
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)

        with zipfile.ZipFile(self.zip_path, 'r') as zip_ref:
            zip_ref.extractall(self.temp_dir)

    def list_dir(self, path):
        full_path = os.path.join(self.temp_dir, path.lstrip('/'))
        if not os.path.isdir(full_path):
            raise FileNotFoundError(f"Directory {path} not found")
        return os.listdir(full_path)

    def change_dir(self, path):
        full_path = os.path.join(self.temp_dir, path.lstrip('/'))
        if not os.path.isdir(full_path):
            raise FileNotFoundError(f"Directory {path} not found")
        return path

    def remove_dir(self, path):
        full_path = os.path.join(self.temp_dir, path.lstrip('/'))
        if os.path.isdir(full_path):
            os.rmdir(full_path)
            return f"Directory {path} removed"
        else:
            raise FileNotFoundError(f"Directory {path} not found")

class FileSystemCommandHandler:
    def __init__(self, vfs, log_file):
        self.vfs = vfs
        self.log_file = log_file

    def execute(self, command):
        command_parts = command.split()
        cmd = command_parts[0]
        args = command_parts[1:]

        if cmd == "ls":
            return self.ls(args)
        elif cmd == "cd":
            return self.cd(args)
        elif cmd == "clear":
            return self.clear()
        elif cmd == "pwd":
            return self.pwd()
        elif cmd == "rmdir":
            return self.rmdir(args)
        elif cmd == "exit":
            return self.exit_shell()
        else:
            return f"Unknown command: {cmd}"

    def ls(self, args):
        path = args[0] if args else '/'
        try:
            return "\n".join(self.vfs.list_dir(path))
        except Exception as e:
            return str(e)

    def cd(self, args):
        if not args:
            return "cd: missing argument"
        path = args[0]
        try:
            self.vfs.change_dir(path)
            return f"Changed directory to {path}"
        except Exception as e:
            return str(e)

    def clear(self):
        return "\033[H\033[J"  # Эмуляция очистки экрана

    def pwd(self):
        return self.vfs.temp_dir

    def rmdir(self, args):
        if not args:
            return "rmdir: missing argument"
        path = args[0]
        try:
            return self.vfs.remove_dir(path)
        except Exception as e:
            return str(e)

    def exit_shell(self):
        return "Exiting shell..."

    def log_action(self, action):
        with open(self.log_file, 'a') as log:
            json.dump(action, log)
            log.write("\n")
