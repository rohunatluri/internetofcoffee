f = open("factlist.txt", "r")

def makeList(File):
    List = []
    for line in File:
        List.append(line)

    return List