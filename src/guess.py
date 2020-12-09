import csv
import chardet


def encoding(filePath: str):
    with open(filePath, "rb") as testFile:
        testFileContent = testFile.read()
        chardetAnswer = chardet.detect(testFileContent)
        return chardetAnswer["encoding"]


def hasHeader(filePath: str):
    with open(filePath, "r") as testFile:
        testFileContent = testFile.read()
        return csv.Sniffer().has_header(testFileContent)


def dialect(filePath: str):
    with open(filePath, "r") as testFile:
        testFileContent = testFile.read()
        return csv.Sniffer().sniff(testFileContent)
