import csv
import chardet


class Importer:
    __importedRows = []

    def __detectFileEncoding(self, filePath: str):
        with open(filePath, "rb") as testFile:
            testFileContent = testFile.read()
            chardetAnswer = chardet.detect(testFileContent)
            return chardetAnswer["encoding"]

    def importCSVFile(self, filePath: str, encoding: str = None):
        if str is None:
            encoding = self.__detectFileEncoding(filePath)

        with open(filePath, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                self.__importedRows.append(row)

    def export(self, outputFilePath: str, newline=""):
        with open(outputFilePath, "w", newline=newline) as outputFile:
            writer = csv.writer(outputFile)
            writer.writerows(self.__importedRows)

    def reset(self):
        __importedRows = []
