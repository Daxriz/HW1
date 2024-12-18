import unittest
from fs_utils import VirtualFileSystem, FileSystemCommandHandler
import os

class TestShellEmulator(unittest.TestCase):

    def setUp(self):
        self.vfs = VirtualFileSystem("test_files.zip")
        self.command_handler = FileSystemCommandHandler(self.vfs, "log.json")

    def test_ls_valid(self):
        result = self.command_handler.ls(['/'])
        self.assertIn('somefile.txt', result)  # Предполагается наличие файла в корне

    def test_ls_invalid_directory(self):
        result = self.command_handler.ls(['/nonexistent'])
        self.assertIn("Directory /nonexistent not found", result)

    def test_cd_valid(self):
        result = self.command_handler.cd(['/valid_dir'])
        self.assertIn("Changed directory to", result)

    def test_cd_invalid(self):
        result = self.command_handler.cd(['/nonexistent_dir'])
        self.assertIn("Directory /nonexistent_dir not found", result)

    def test_rmdir_valid(self):
        result = self.command_handler.rmdir(['/empty_dir'])
        self.assertIn("Directory /empty_dir removed", result)

    def test_rmdir_invalid(self):
        result = self.command_handler.rmdir(['/non_empty_dir'])
        self.assertIn("Directory /non_empty_dir not found", result)

if __name__ == "__main__":
    unittest.main()
