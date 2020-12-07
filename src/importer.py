import csv
import chardet
import pandas


class Importer:
    __dataFrame: pandas.DataFrame
    __columnCount: int

    def __init__(self):
        self.reset()

    def __detectFileEncoding(self, filePath: str):
        with open(filePath, "rb") as testFile:
            testFileContent = testFile.read()
            chardetAnswer = chardet.detect(testFileContent)
            return chardetAnswer["encoding"]

    def __isHeaderPresent(self, filePath: str):
        with open(filePath, "r") as testFile:
            firstLine = testFile.readline()
            return csv.Sniffer().has_header(firstLine)

    def importCSVFile(self, filePath: str, encoding: str = None, headerPresent: bool = None):
        if encoding is None:
            encoding = self.__detectFileEncoding(filePath)
            print("Guessed encoding: " + encoding)

        if headerPresent is None:
            headerPresent = self.__isHeaderPresent(filePath)
            print("Guessed headerPresent: " + str(headerPresent))

        header = "infer" if headerPresent else None

        dataFrame = pandas.read_csv(filePath, encoding=encoding, header=header)
        columnCount = len(dataFrame.columns)

        if self.__dataFrame is None:
            self.__dataFrame = dataFrame
            self.__columnCount = columnCount
        else:
            if self.__columnCount is not columnCount:
                raise ValueError(
                    "Column count does not match already imported rows")

            self.__dataFrame = self.__dataFrame.append(dataFrame)

    def exportLists(self):
        pass

    def exportNumPyArray(self):
        pass

    def exportDataFrame(self):
        return self.__dataFrame

    def exportCSVFile(self, filePath: str, encoding: str, seperator: str):
        self.__dataFrame.to_csv(
            filePath, index=False, encoding=encoding, sep=seperator)

    def exportXMLFile(self):
        pass

    def reset(self):
        self.__dataFrame = None
