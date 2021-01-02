import guess


class Dialect:
    """
    Class representing the format of a CSV file/string
    """
    encoding: str = "utf-8"
    hasHeader: bool = False
    sepChar: str = ","
    quoteChar: str = "\""

    def guessFromFile(self, filePath: str):
        """
        This method calls guessFromSample with the content of the file belonging to the supplied filePath.
        It also guesses the encoding of the file and sets it one the Dialect object it was called on.

        Args:
            filePath (str): The relative or absolute filepath to guess the Dialect parameters from
        """
        self.encoding = guess.encoding(filePath)

        with open(filePath, "r") as testFile:
            testFileContent = testFile.read()
            self.guessFromSample(testFileContent)

    def guessFromSample(self, sample: str):
        """
        This method guesses the seperator and quotation character and
        also whether the supplied sample appears to have a header.

        It sets every guessed value on the Dialect object it was called on.

        Args:
            sample (str): Part of the content of a CSV formatted text
        """
        self.hasHeader = guess.hasHeader(sample)

        dialect = guess.dialect(sample)
        if dialect is not None:
            self.sepChar = dialect.delimiter
            self.quoteChar = dialect.quotechar
