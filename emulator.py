import os
import sys

class CommandHandler:
    def __init__(self, vfs, logger):
        self.vfs = vfs
        self.logger = logger

    def execute(self, command):
        args = command.split()
        if not args:
            return

        cmd = args[0]

        if cmd == "ls":
            result = self.vfs.list_dir(self.vfs.current_path)
            print("\n".join(result) if result else "Пусто.")
            self.logger.log(command)

        elif cmd == "cd":
            path = args[1] if len(args) > 1 else "/"
            try:
                self.vfs.change_dir(path)
                self.logger.log(command)
            except FileNotFoundError as e:
                print(e)

        elif cmd == "clear":
            os.system("cls" if os.name == "nt" else "clear")
            self.logger.log(command)

        elif cmd == "pwd":
            print(self.vfs.current_path)
            self.logger.log(command)

        elif cmd == "rmdir":
            if len(args) < 2:
                print("Укажите путь к директории для удаления.")
                return
            try:
                self.vfs.remove_dir(args[1])
                print(f"Директория '{args[1]}' удалена.")
                self.logger.log(command)
            except FileNotFoundError as e:
                print(e)

        elif cmd == "exit":
            print("Завершение работы...")
            self.logger.log(command)
            sys.exit(0)  # Завершаем выполнение программы

        else:
            print(f"Команда '{cmd}' не найдена.")
