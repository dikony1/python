with open("my_list.txt", "r") as source_file:
    contents = source_file.read()
    with open("destination.txt", "w") as destination_file:
        destination_file.write(contents)