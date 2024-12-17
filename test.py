import unittest
import os
import json
from shell_emulator import ShellEmulator


class TestShellEmulator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Здесь предполагается создание временного zip-архива для тестирования
        cls.test_zip_path = 'test_files.zip'
        cls.log_file_path = 'test_log.json'
        
        # Создание временного zip-файла с тестовыми файлами
        with zipfile.ZipFile(cls.test_zip_path, 'w') as zipf:
            zipf.writestr('file1.txt', 'Content of file 1.')
            zipf.writestr('subdir/file2.txt', 'Content of file 2.')
            zipf.writestr('subdir2/', '')  # Создаем пустую папку

    @classmethod
    def tearDownClass(cls):
        # Очистка временных файлов
        os.remove(cls.test_zip_path)
        if os.path.exists(cls.log_file_path):
            os.remove(cls.log_file_path)

    def setUp(self):
        self.emulator = ShellEmulator("TestHost", self.test_zip_path, self.log_file_path)

    def test_ls_empty_directory(self):
        self.emulator.current_path = 'subdir2/'
        with self.assertLogs(self.emulator, 'INFO') as log:
            self.emulator.list_files([])
            self.assertIn("Directory is empty or does not exist", self.emulator.text_area.get("1.0", "end-1c"))

    def test_ls_populated_directory(self):
        self.emulator.current_path = ''
        with self.assertLogs(self.emulator, 'INFO') as log:
            self.emulator.list_files([])
            self.assertIn("file1.txt", self.emulator.text_area.get("1.0", "end-1c"))

    def test_cd_change_directory(self):
        self.emulator.change_directory(['subdir'])
        self.assertEqual(self.emulator.current_path, 'subdir')

    def test_cd_to_nonexistent_directory(self):
        response = self.emulator.change_directory(['nonexistent_dir'])
        self.assertIn("Incorrect path", self.emulator.text_area.get("1.0", "end-1c"))
        self.assertNotEqual(self.emulator.current_path, 'nonexistent_dir')

    def test_exit_emulator(self):
        self.emulator.exit_emulator()
        self.assertFalse(self.emulator.window.winfo_exists()) 

    def test_clear_text_area(self):
        self.emulator.text_area.insert('insert', "Some text")
        self.emulator.clear_text_area()
        self.assertEqual(self.emulator.text_area.get("1.0", "end-1c"), "")  

    def test_pwd(self):
        self.emulator.show_current_directory()
        self.assertIn(self.emulator.current_path, self.emulator.text_area.get("1.0", "end-1c"))

    def test_rmdir(self):
        self.emulator.remove_directory(['subdir2'])
        self.assertIn("Removed directory: subdir2", self.emulator.text_area.get("1.0", "end-1c"))

    def test_rmdir_nonexistent(self):
        self.emulator.remove_directory(['nonexistent_dir'])
        self.assertIn("Directory does not exist", self.emulator.text_area.get("1.0", "end-1c"))


if __name__ == '__main__':
    unittest.main()
