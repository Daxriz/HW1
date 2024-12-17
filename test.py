import unittest
from shell_emulator import ShellEmulator

class TestShellEmulator(unittest.TestCase):
    # Здесь вы можете создать тесты для ls, cd и остальных команд
    def setUp(self):
        self.emulator = ShellEmulator("TestHost", "test.zip", "log.json")
    
    def test_ls(self):
        self.emulator.list_files([])
        # Проверка вывода на наличие ожидаемых результатов
    
    def test_cd(self):
        self.emulator.change_directory(["/new_directory"])
        # Проверка изменения текущего пути

    # Добавьте дополнительные тесты для команд clear, pwd, rmdir и exit

if __name__ == '__main__':
    unittest.main()
