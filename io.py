import sys
import os
from enum import Enum
from .config import validate_blob_exists, get_blob_path


class WriteMode(Enum):
    WRITE = 0
    APPEND = 1


def read_stdin_bytes() -> bytes:
    return sys.stdin.buffer.read()


def write_stdin_bytes(data: bytes):
    sys.stdout.buffer.write(data)
    sys.stdout.buffer.flush()


def read_blob(fileName: str) -> bytes:
    if os.path.exists(fileName):
        print("File Found!")
    elif validate_blob_exists(fileName):
        fullPath = get_blob_path(fileName)
        with open(fullPath, "rb") as f:
            return f.read()
    else:
        print("File NOT Found!")


def write_blob(filePath: str, data: bytes, writemode: WriteMode):

    fileExists = os.path.exists(filePath)

    if writemode == WriteMode.WRITE:
        with open(filePath, "wb") as f:
            f.write(data)

    elif writemode == WriteMode.APPEND:
        if not fileExists:
            write_blob(filePath, data, WriteMode.WRITE)
        else:
            with open(filePath, "ab") as f:
                f.write(data)
    else:
        e = f"WriteMode {writemode.name} must be a value of WriteMode"
        raise ValueError(e)


if __name__ == "__main__":
    print("liborchest io.py")
