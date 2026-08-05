def copy_file(command: str) -> None:

    comand = command.split(" ")

    if len(comand) != 3 or comand[0] != "cp":
        return

    source = comand[1]
    destination = comand[2]

    if source == destination:
        return

    try:
        with open(source, "r") as src_file:
            with open(destination, "w") as dest_file:
                dest_file.write(src_file.read())
    except FileNotFoundError:
        return
