import re
import csv
import pandas
import chardet


def encoding(filePath: str):
    with open(filePath, "rb") as testFile:
        testFileContent = testFile.read()
        chardetAnswer = chardet.detect(testFileContent)
        return chardetAnswer["encoding"]


def hasHeader(sample: str):
    return csv.Sniffer().has_header(sample)


def dialect(sample: str):
    return csv.Sniffer().sniff(sample)

regexEMail = re.compile(r"^[a-zA-Z0-9_.-]+@[a-zA-Z0-9.-]+.[a-z.]{2,6}$")
regexDate = re.compile(r"^[0-3]?[0-9][/.][0-3]?[0-9][/.](?:[0-9]{2})?[0-9]{2}$")
regexTime = re.compile(r"^[0-2]\d:[0-6]\d:[0-6]\d$")
regexNumber = re.compile(r"^[+-]?\d+([,.]\d+)?$")

def dataType(sample: str):
    if regexEMail.match(sample):
        return "Email"

    if regexDate.match(sample):
        return "Date"

    if regexTime.match(sample):
        return "Time"

    if regexNumber.match(sample):
        return "Number"

    return "Text"

def headerNames(dataFrame: pandas.DataFrame):
    headerNameCount = {}
    newColumns = {}

    for column in dataFrame.columns:
        cellsInColumn = dataFrame[column]
        sample = str(cellsInColumn[0])
        headerName = dataType(sample)

        if headerName not in headerNameCount:
            headerNameCount[headerName] = 0

        count = headerNameCount[headerName]
        headerNameCount[headerName] = count + 1

        headerName += "_" + str(count)

        newColumns[column] = headerName
    
    return newColumns

