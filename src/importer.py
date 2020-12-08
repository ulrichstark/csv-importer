import pandas
from dialect import Dialect


class Importer:
    __dataFrame: pandas.DataFrame
    __columnCount: int

    def __init__(self):
        self.reset()

    def importCSVFile(self, filePath: str, dialect: Dialect):
        header = "infer" if dialect.hasHeader else None
        dataFrame = pandas.read_csv(
            filePath,
            sep=dialect.sepChar,
            quotechar=dialect.quoteChar,
            encoding=dialect.encoding,
            header=header
        )
        columnCount = len(dataFrame.columns)

        if self.__dataFrame is None:
            self.__dataFrame = dataFrame
            self.__columnCount = columnCount
        else:
            if self.__columnCount is not columnCount:
                raise ValueError(
                    "Column count does not match already imported rows")

            self.__dataFrame = self.__dataFrame.append(dataFrame)

    def getDictionary(self):
        pass

    def getLists(self):
        pass

    def getNumPyArray(self):
        pass

    def getDataFrame(self):
        return self.__dataFrame

    def reset(self):
        self.__dataFrame = None
