
import sys
import os
from site import getsitepackages


def is_venv() -> str | None:
    if sys.prefix != sys.base_prefix:
        return os.path.basename(sys.prefix)
    return None


def main() -> None:
    if os.getenv("VIRTUAL_ENV"):
        print("MATRIX STATUS: Welcome to the construct\n")
        print("Current Python:", sys.executable)
        print("Virtual Environment:", is_venv())
        print("Environment Path", os.getenv("VIRTUAL_ENV"))
        print(r"""
SUCCESS: You're in an isolated environment!
Safe to install packages without affecting
the global system.""")
        print("Package installation path:", getsitepackages()[0])
        print("\n'deactivate' to quit the matrix")
    else:
        print("MATRIX STATUS: You're still plugged in\n")
        print("Current Python:", sys.executable)
        print("Virtual Environment:", is_venv())
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print(r"""
To enter the construct, run:
python -m venv matrix_env
source matrix_env/bin/activate # On Unix
matrix_env
Scripts
activate # On Windows

Then run this program again""")


if __name__ == "__main__":
    main()
