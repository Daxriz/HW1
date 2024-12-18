import sys
import zipfile
import os
import json
from file_system import VirtualFileSystem
from commands import CommandHandler
from logger import Logger

def main():
    # Обработка аргументов командной строки
    if len(sys.argv) != 4:
        print("Использование: python main.py <имя компьютера> <путь к архиву> <путь к лог-файлу>")
        sys.exit(1)

    computer_name = sys.argv[1]
    zip_path = sys.argv[2]
    log_path = sys.argv[3]

    # Проверка существования файла zip
    if not os.path.isfile(zip_path):
        print("Ошибка: Файл виртуальной файловой системы не найден.")
        sys.exit(1)

    # Инициализация компонентов
    logger = Logger(log_path)
    vfs = VirtualFileSystem(zip_path)
    handler = CommandHandler(vfs, logger)

    # Эмуляция оболочки
    print(f"Добро пожаловать в эмулятор оболочки [{computer_name}]!")

    # Цикл для ввода команд
    while True:
        try:
            # Ожидаем ввод команды
            command = input(f"{computer_name}> ").strip()
            handler.execute(command)  # Передаем команду на обработку
        except KeyboardInterrupt:
            # Если произошел KeyboardInterrupt, завершаем цикл
            print("\nЗавершение работы...")
            break  # Прерываем цикл

# Важно: функция main() должна быть вызвана при запуске
if __name__ == "__main__":
    main()
