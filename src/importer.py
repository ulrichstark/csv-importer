import pandas
from dialect import Dialect


class Importer:
    __dataFrame: pandas.DataFrame
    __columnCount: int
    __headerSeen: bool

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

            if not self.__headerSeen and dialect.hasHeader:
                # Aktueller DataFrame erhält Header der neu zu importierenden Datei
                newCols = {x: y for x, y in zip(self.__dataFrame, dataFrame)}
                self.__dataFrame = self.__dataFrame.rename(columns=newCols)

            if self.__headerSeen and not dialect.hasHeader:
                # Aktuell zu importierende Datei erhält Header des bisherigen DataFrames
                newCols = {x: y for x, y in zip(dataFrame, self.__dataFrame)}
                dataFrame = dataFrame.rename(columns=newCols)

            self.__dataFrame = self.__dataFrame.append(dataFrame)

        if not self.__headerSeen and dialect.hasHeader:
            self.__headerSeen = True

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
        self.__columnCount = 0
        self.__headerSeen = False
