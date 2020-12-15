import guess


class Dialect:
    encoding: str = "utf-8"
    hasHeader: bool = False
    sepChar: str = ","
    quoteChar: str = "\""

    def guessFromFile(self, filePath: str):
        self.encoding = guess.encoding(filePath)

        with open(filePath, "r") as testFile:
            testFileContent = testFile.read()
            self.guessFromSample(testFileContent)

    def guessFromSample(self, sample: str):
        self.hasHeader = guess.hasHeader(sample)

        dialect = guess.dialect(sample)
        if dialect is not None:
            self.sepChar = dialect.delimiter
            self.quoteChar = dialect.quotechar
