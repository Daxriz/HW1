import pytest
from emulator import ShellEmulator
from unittest.mock import patch, MagicMock

# Тестируем команды
@pytest.fixture
def emulator():
    return ShellEmulator("test_host", "test.zip", "log.json")

def test_ls(emulator):
    with patch("builtins.input", return_value="ls"):
        with patch("builtins.print") as mocked_print:
            emulator.run()
            mocked_print.assert_called_with("file1.txt")
    
def test_cd(emulator):
    with patch("builtins.input", return_value="cd /folder"):
        emulator.run()
        assert emulator.current_dir == "/folder"

def test_pwd(emulator):
    with patch("builtins.input", return_value="pwd"):
        with patch("builtins.print") as mocked_print:
            emulator.run()
            mocked_print.assert_called_with("/")

def test_rmdir(emulator):
    with patch("builtins.input", return_value="rmdir folder"):
        with patch("builtins.print") as mocked_print:
            emulator.run()
            mocked_print.assert_called_with("rmdir: removed folder")
