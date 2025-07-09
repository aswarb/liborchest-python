import os
import sys
from enum import Enum

PROGRAM_NAME = "orchest"

LINUX_DEFAULT_PATH = f"~/{PROGRAM_NAME}"
WINDOWS_DEFAULT_PATH = f"%APPDATA%\\{PROGRAM_NAME}"
MACOS_DEFAULT_PATH = f"~/Library/Application Support/{PROGRAM_NAME}"
UNKOWN_DEFAULT_PATH = f"/tmp/{PROGRAM_NAME}"

SCRIPTS_SUBDIR = "/scripts"
DATA_SUBDIR = "/data"


class OSType(Enum):
    UNKNOWN = 0
    WINDOWS = 1
    MACOS = 2
    LINUX = 3


def get_os():
    if sys.platform.startswith("win"):
        return OSType.WINDOWS
    elif sys.platform == "darwin":
        return OSType.MACOS
    elif sys.platform.startswith("linux"):
        return OSType.LINUX
    else:
        return OSType.UNKNOWN


def validate_blob_exists(path: str) -> bool:
    return False


def get_absolute_path(relPath: str) -> str:
    return os.path.abspath(relPath)


def get_blob_path() -> str:
    value = os.getenv(f"{PROGRAM_NAME.upper()}_DATA_PATH_OVERRIDE", None)
    if value is not None:
        return value

    os_type = get_os()
    path = ""
    match os_type:
        case OSType.WINDOWS:
            path = WINDOWS_DEFAULT_PATH
        case OSType.MACOS:
            path = MACOS_DEFAULT_PATH
        case OSType.LINUX:
            path = LINUX_DEFAULT_PATH
        case OSType.UNKNOWN:
            path = UNKOWN_DEFAULT_PATH
        case _:
            path = ""
    return f"{path}{DATA_SUBDIR}"


if __name__ == "__main__":
    print("liborchest.config")
