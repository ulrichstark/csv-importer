import guess


class Dialect:
    encoding: str = "utf-8"
    hasHeader: bool = False
    sepChar: str = ","
    quoteChar: str = "\""

    def __init__(self, filePath: str = None):
        if filePath is not None:
            self.guessFromFile(filePath)

    def guessFromFile(self, filePath: str):
        self.encoding = guess.encoding(filePath)
        self.hasHeader = guess.hasHeader(filePath)

        dialect = guess.dialect(filePath)
        if dialect is not None:
            self.sepChar = dialect.delimiter
            self.quoteChar = dialect.quotechar
