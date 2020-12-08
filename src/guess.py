import csv
import chardet


def encoding(filePath: str):
    with open(filePath, "rb") as testFile:
        testFileContent = testFile.read()
        chardetAnswer = chardet.detect(testFileContent)
        return chardetAnswer["encoding"]


def hasHeader(filePath: str):
    with open(filePath, "r") as testFile:
        firstLine = testFile.readline()
        return csv.Sniffer().has_header(firstLine)


def dialect(filePath: str):
    with open(filePath, "r") as testFile:
        firstLine = testFile.readline()
        return csv.Sniffer().sniff(firstLine)
