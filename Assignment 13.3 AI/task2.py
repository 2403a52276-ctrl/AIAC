from typing import Optional
import sys

"""
task2.py

Refactored safe file reader using context manager and explicit error handling.
"""



def read_file(filename: str) -> Optional[str]:
    """Read and return the contents of filename.
    Returns None if the file cannot be read."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except PermissionError:
        print(f"Permission denied: {filename}")
    except OSError as e:
        print(f"Error reading {filename}: {e}")
    return None


if __name__ == "__main__":
    # Example usage: python task2.py path/to/file.txt

    if len(sys.argv) < 2:
        print("Usage: python task2.py <filename>")
    else:
        content = read_file(sys.argv[1])
        if content is not None:
            print(content)