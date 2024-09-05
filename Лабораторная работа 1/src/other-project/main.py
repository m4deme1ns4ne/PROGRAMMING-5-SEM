import subprocess
from termcolor import colored

from printHelloWorld import printHelloWorldfunc


def list_installed_packages():
    result = subprocess.run(['pip', 'list'], capture_output=True, text=True)
    packages = result.stdout.splitlines()
    for package in packages:
        if 'printHelloWorld' in package:
            print(f"{colored(package, 'green')}        {colored("<- My package", "green")}")
        else:
            print(package)


def main():
    print()
    printHelloWorldfunc()
    print()
    list_installed_packages()


if __name__ == '__main__':
    main()
