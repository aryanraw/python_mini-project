def links():
    obj = open("links.txt", "r")
    lin = []
    for line in obj:
        lin.append(line.split())
    obj.close()
    return lin