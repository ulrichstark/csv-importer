import csv
import chardet


class Importer:
    __importedRows = []

    def __detectFileEncoding(self, filePath):
        with open(filePath, "rb") as testFile:
            testFileContent = testFile.read()
            chardetAnswer = chardet.detect(testFileContent)
            return chardetAnswer["encoding"]

    def importCSVFile(self, filePath, encoding=None):
        if not isinstance(filePath, str):
            raise TypeError("filePath should be a string")

        if not isinstance(encoding, str):
            encoding = self.__detectFileEncoding(filePath)

        with open(filePath, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                self.__importedRows.append(row)

    def export(self, outputFilePath, newline=""):
        if not isinstance(outputFilePath, str):
            raise TypeError("outputFilePath should be a string")

        with open(outputFilePath, "w", newline=newline) as outputFile:
            writer = csv.writer(outputFile)
            writer.writerows(self.__importedRows)

    def reset(self):
        __importedRows = []
