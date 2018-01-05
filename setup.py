import os
import json

## TODO: read the img folder
## IMG folder:
## subfolders = categories
## fileNames = titles
## output all to json files
## Edit portfolio.js and portfolio.html accordingly

def extractInfoToJson():
    """
    Reads the img folder, and extracts the information from it.
    Subfolders of img: categories
    File names of the images: titles
    Writes all the information in a json file under the folder json/
    """
    rootPath = "./img"
    data = []

    categories = os.listdir(rootPath) # The array of categories
    for category in categories:

        images = []
        files = os.listdir(rootPath + "/" + category)
        for f in files:
            fileToAdd = {"fileName": f, "title": os.path.splitext(f)[0]}
            images.append(fileToAdd)

        data.append({"category": category, "images": images})

    with open('./json/data.json', 'w', encoding='utf8') as outfile:
        outfile.write("data = ")
        json.dump(data, outfile)


def getName():
    """
    Requests the name of the user wishing to generate a portfolio
    Outputs the give name to JSON
    """
    name = ""
    while(name == ""):
        name = input("Please type in your username: ")

    with open('./json/misc.json', 'w', encoding='utf8') as outfile:
        outfile.write("misc = ")
        json.dump({"name": name}, outfile)

getName()
extractInfoToJson()
