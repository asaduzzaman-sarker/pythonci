"""
This script fixes invalid (fancy) quotation marks in the SSH config file (~/.ssh/config),
which can cause git/ssh errors. It also creates a backup before making changes.
"""
import shutil
from pathlib import Path

def fix_ssh_config(file_path):
    """
    Fixes invalid (fancy) quotation marks in an SSH config file.

    Args:
        file_path (str or Path): Path to the SSH config file.
    """
    file_path = Path(file_path)

    if not file_path.exists():
        print(f"Error: File '{file_path}' does not exist.")
        return

    # Backup the original config
    backup_path = file_path.with_suffix('.bak')
    shutil.copy(file_path, backup_path)
    print(f"Backup created at '{backup_path}'")

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace fancy quotes with normal quotes
    content = content.replace('“', '"').replace('”', '"').replace('‘', "'").replace('’', "'")

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

    print(f"Fixed quotes in '{file_path}'")

if __name__ == "__main__":
    ssh_config_path = Path.home() / ".ssh" / "config"  # Automatically find user's home folder
    fix_ssh_config(ssh_config_path)
