import sys
from pathlib import Path
from colorama import init, Fore

init(autoreset=True)


def print_directory_structure(path: Path, indent: str = ""):
    try:
        for item in sorted(path.iterdir()):
            if item.is_dir():
                print(indent + Fore.BLUE + item.name + "/")
                print_directory_structure(item, indent + "    ")
            else:
                print(indent + Fore.GREEN + item.name)
    except PermissionError:
        print(indent + Fore.RED + "Немає доступу")


def main():
    if len(sys.argv) != 2:
        print(Fore.RED + "Використання: python hw03.py <шлях>")
        sys.exit(1)

    dir_path = Path(sys.argv[1])

    if not dir_path.exists() or not dir_path.is_dir():
        print(Fore.RED + "Некоректний шлях до директорії")
        sys.exit(1)

    print(Fore.CYAN + dir_path.name + "/")
    print_directory_structure(dir_path)


if __name__ == "__main__":
    main()
