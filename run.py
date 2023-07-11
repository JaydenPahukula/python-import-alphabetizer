import os
import os.path

IGNORE = set()


def parseImportLine(line:str):
    a = line.split()
    output = ""
    # import ______
    if len(a) == 2 and a[0] == "import":
        output = a[1]
    # from _____ import ______
    elif len(a) >= 4 and a[0] == "from" and a[2] == "import":
        output = a[1] + "".join([s.strip(",") for s in a[3:]])
    return "".join(filter(str.isalpha, output))



def alphabetizeNames(path:str):

    # read all lines
    entireFile = []
    with open(path, "r") as file:
        entireFile = file.readlines()

    # parse import lines
    lines = []
    i = 0
    while i < len(entireFile):
        parsedLine = parseImportLine(entireFile[i].strip("\n"))
        if not parsedLine: break
        lines.append((parsedLine, entireFile[i]))
        i += 1

    # return if there are 1 or fewer lines
    if len(lines) <= 1: return False

    # sort lines
    sortedLines = sorted(lines)

    # return if lines did not change
    if sortedLines == lines: return False

    with open(path, "w") as file:
        # write include lines in new order
        for parsedLine, line in sortedLines:
            file.write(line)
        # Write the rest of the file
        file.write("".join(entireFile[i:]))

    print(f"  > {path}: alphabetized imports")
    return True



def recurseDir(root:str):
    count = 0

    # get list of files
    files = os.listdir(root)

    for name in files:
        # skip if in IGNORE
        if name in IGNORE: continue

        path = root+"/"+name

        # recurse if file is directory
        if os.path.isdir(path):
            count += recurseDir(path)

        # rearrange if file is .py
        elif os.path.isfile(path) and name[-3:] == ".py":
            if alphabetizeNames(path):
                count += 1
    
    return count



if __name__ == "__main__":

    # add all names from toskip.txt to IGNORE
    with open("toskip.txt", "r") as file:
        IGNORE.add(file.readline().strip("\n"))

    # prompt for directory to start in
    start = input("\n\nDirectory to start from: (blank for current directory) ")
    while start and not os.path.exists(start):
        print(f"Path '{start}' does not exist")
        start = input("Directory to start from: (blank for current directory) ")

    # default to current directory
    if start == "":
        start = os.getcwd()

    # start!
    count = recurseDir(start)

    print(f"Done (alphabetized {count} files' imports)")