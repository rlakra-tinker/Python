#
# Author: Rohtash Lakra
#
from pathlib import Path
import datetime

print()
base_dir = Path.cwd()
print(f"base_dir: {base_dir}")

def print_folder(base_dir: Path):
    print()
    print(f"----------------<{base_dir.name}>----------------")
    print(f"Parent: {base_dir.parent}")
    print(f"Is Folder: {base_dir.is_dir()}")
    print(f"Is Symlink: {base_dir.is_symlink()}")
    print(f"Is File: {base_dir.is_file()}")
    print(f"Exists: {base_dir.exists()}")
    print(f"Name: {base_dir.name}")
    print(f"CWD: {base_dir.cwd()}")
    print(f"Home: {base_dir.home()}")
    print(f"Owner: {base_dir.owner()}")
    print(f"Absolute: {base_dir.absolute()}")
    print(f"Parts: {base_dir.parts}")

# print folder
print_folder(base_dir)

print()
for entry in base_dir.iterdir():
    print_folder(entry)

print()
date = datetime.date.today()
today_logs = Path.cwd().joinpath("logs",str(date), "*.txt")
print(f"today_logs={today_logs}")

print()
print(f"Find me here <{Path(__file__).parent}>")
log_file_path = Path(__file__).parent.parent.joinpath("sql", "call_logs", "get_call_log_details.sql")
print(f"log_file_path: {log_file_path}>")
# date = datetime.date.today()
# today_logs = Path.cwd().joinpath("logs",str(date), "*.txt")
# print(f"today_logs={today_logs}")
