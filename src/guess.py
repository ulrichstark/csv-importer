import csv
import chardet


def guessFileEncoding(filePath: str):
    with open(filePath, "rb") as testFile:
        testFileContent = testFile.read()
        chardetAnswer = chardet.detect(testFileContent)
        return chardetAnswer["encoding"]


def guessHeaderPresence(filePath: str):
    with open(filePath, "r") as testFile:
        firstLine = testFile.readline()
        return csv.Sniffer().has_header(firstLine)
