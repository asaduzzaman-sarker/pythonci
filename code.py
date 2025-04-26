# Fix bad quotes in ~/.ssh/config

def fix_ssh_config(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace fancy quotes with normal quotes
    content = content.replace('“', '"').replace('”', '"').replace('‘', "'").replace('’', "'")

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

    print(f"Fixed quotes in {file_path}")

if __name__ == "__main__":
    ssh_config_path = r"C:\Users\85152406\.ssh\config"  # Update your username if needed
    fix_ssh_config(ssh_config_path)
