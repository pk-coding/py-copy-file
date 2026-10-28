import os
from shutil import copy


def copy_file(command: str) -> None:
    split_command: list[str] = command.split()

    if len(split_command) != 3 or split_command[0] != "cp":
        return

    filename = split_command[1]
    new_filename = split_command[2]

    if filename == new_filename:
        return

    if not os.path.isfile(filename):
        return

    copy(filename, new_filename)
