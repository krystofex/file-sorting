import os
import json
import sys

configFilePath = "config.json"


def sort():
    configFile = json.loads(open(configFilePath).read())
    for file in os.listdir():
        if os.path.isfile(file):
            if not any(file in i for i in configFile["ignored"]):
                for fileName in configFile["sort"]:
                    for fileExtension in configFile["sort"][fileName]:
                        if file.split('.')[-1] == fileExtension:
                            if not os.path.exists(fileName):
                                os.makedirs(fileName)
                            os.rename(file, fileName + "/" + file)


# arguments handling
for x in range(len(sys.argv)):
    if sys.argv[x] == "-h" or sys.argv[x] == "--help":
        returnString = ("\ncommands:"
                        "\n -h or --help                | writes all commands"
                        "\n -p or --path + path         | example: main.py - p config.json"
                        "\n -c or                       | run program without gui"
                        )
        exit(returnString)
    elif sys.argv[x] == "-p" or sys.argv[x] == "--path":
        try:
            configFilePath = sys.argv[x+1]
            x += 1
        except:
            print("error: path was not defined try -h")
    elif sys.argv[x] == "-c":
        sort()
        exit("done")

sort()
exit("done")
