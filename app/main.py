
def copy_file(command: str) -> None:
    split_command: list[str] = command.split()

    if len(split_command) != 3 or split_command[0] != "cp":
        return

    source_file_name = split_command[1]
    new_filename = split_command[2]

    if source_file_name == new_filename:
        return

    try:
        with (open(source_file_name, "r") as file_in,
              open(new_filename, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
