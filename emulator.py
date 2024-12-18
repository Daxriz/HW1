class ShellEmulator:
    def __init__(self, hostname, vfs, logger):
        self.hostname = hostname
        self.vfs = vfs
        self.logger = logger
        self.current_dir = "/"

    def execute(self, command):
        self.logger.log(f"Executing command: {command}")
        parts = command.strip().split()
        if not parts:
            return ""

        cmd = parts[0]
        args = parts[1:]

        if cmd == "ls":
            return self.vfs.list_directory(self.current_dir)
        elif cmd == "cd":
            if args:
                self.current_dir = self.vfs.change_directory(self.current_dir, args[0])
                return ""
            else:
                return "Usage: cd <directory>"
        elif cmd == "pwd":
            return self.current_dir
        elif cmd == "clear":
            return "[CLEAR_SCREEN]"
        elif cmd == "rmdir":
            if args:
                return self.vfs.remove_directory(self.current_dir, args[0])
            else:
                return "Usage: rmdir <directory>"
        elif cmd == "exit":
            self.logger.save()
            exit(0)
        else:
            return f"Unknown command: {cmd}"
