with open("029config", "r") as file1:
    for line in file1:
        linestr = line.strip()
        if linestr.startswith("!") != True:
            print(line.strip())