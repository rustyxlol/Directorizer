import os
from shutil import copyfile
from pathlib import Path
import shutil


def getFiles(src):
    return [i for i in os.listdir(src) if os.path.isfile(os.path.join(src, i))]


def getMatches(fileName, categories):
    return [match for match in categories if match in fileName.lower()]


def createDirectories(src, categories):
    for category in categories:
        dirName = os.path.join(src, category)
        try:
            os.makedirs(dirName)
        except OSError:
            print("File already exists!")
            pass


def moveFile(src, dst):
    if os.path.isfile(src):
        shutil.move(src, dst)


if __name__ == "__main__":
    src = input("Enter source path: ")
    input_categories = input("Enter categories separated by comma(a,b,c) : ").split(",")

    categories = [i.lower() for i in input_categories]
    createDirectories(src, categories)

    fileNames = getFiles(src)

    for fileName in fileNames:
        matches = getMatches(fileName, categories)
        if matches:
            srcFile = os.path.join(src, fileName)
            dstFile = os.path.join(src, matches[0], fileName)
            moveFile(srcFile, dstFile)
    print("Finished the job boss")
