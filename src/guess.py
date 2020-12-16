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

regexGeoCoord = re.compile(r"^(N|S)?0*\d{1,2}°0*\d{1,2}(′|')0*\d{1,2}\.\d*(″|\")(?(1)|(N|S)) (E|W)?0*\d{1,2}°0*\d{1,2}(′|')0*\d{1,2}\.\d*(″|\")(?(5)|(E|W))$")
regexEMail = re.compile(r"^[a-zA-Z0-9_.-]+@[a-zA-Z0-9.-]+.[a-z.]{2,6}$")
regexURL = re.compile(r"^((https?|ftp|smtp):\/\/)?(www.)?[a-z0-9]+\.[a-z]+(\/[a-zA-Z0-9#]+\/?)*$")
regexDatetime = re.compile(r"^(?:(?:31(/|-|.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(/|-|.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(/|-|.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(/|-|.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2}).([0-1]\d|2[0-3]):[0-5]\d(:[0-5]\d)*$")
regexDate = re.compile(r"^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$")
regexTime = re.compile(r"^([0-1]\d|2[0-3]):[0-5]\d(:[0-5]\d)*$")
regexFloat = re.compile(r"^[+-]?\d+[,.]\d+$") 
regexInteger = re.compile(r"^[+-]?\d+$")
regexBoolean = re.compile(r"^(wahr|falsch|ja|nein|yes|no|true|false|t|f|1|0)$", flags=re.IGNORECASE)

def dataType(sample: str):
    if regexGeoCoord.match(sample):
        return "GeoCoord"

    if regexEMail.match(sample):
        return "Email"

    if regexURL.match(sample):
        return "URL"

    if regexDatetime.match(sample):
        return "Datetime"

    if regexDate.match(sample):
        return "Date"

    if regexTime.match(sample):
        return "Time"

    if regexFloat.match(sample):
        return "Float"

    if regexInteger.match(sample):
        return "Integer"

    if regexBoolean.match(sample):
        return "Boolean"

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

