import os
import json

configFile = json.loads(open("config.json").read())

for file in os.listdir():
    if os.path.isfile(file):
        if not any(file in i for i in configFile["ignored"]):
            for fileName in configFile["sort"]:
                for fileExtension in configFile["sort"][fileName]:
                    if file.split('.')[-1] == fileExtension:
                        if not os.path.exists(fileName):
                            os.makedirs(fileName)
                        os.rename(file, fileName + "/" + file)
print("done")
