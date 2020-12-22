import pandas
import guess
from io import StringIO
from lxml import etree
from dialect import Dialect


class Importer:
    __dataFrame: pandas.DataFrame
    __headerSeen: bool

    def __init__(self):
        self.reset()

    def importXMLFile(self, xmlFilePath: str, xslFilePath: str, xslParameters = {}):
        xmlFile = etree.parse(xmlFilePath)
        xslFile = etree.parse(xslFilePath)
        transformer = etree.XSLT(xslFile)

        transformedOutput = str(transformer(xmlFile, **xslParameters))

        dialect = Dialect()
        dialect.guessFromSample(transformedOutput)

        buffer = StringIO(transformedOutput)

        self.importCSVFile(buffer, dialect)


    def importCSVFile(self, filePathOrBuffer: str, dialect: Dialect):
        header = "infer" if dialect.hasHeader else None
        dataFrame = pandas.read_csv(
            filePathOrBuffer,
            sep=dialect.sepChar,
            quotechar=dialect.quoteChar,
            encoding=dialect.encoding,
            header=header
        )

        if dialect.hasHeader is False:
            newColumns = guess.headerNames(dataFrame)
            dataFrame.rename(columns=newColumns, inplace=True)

        if self.__dataFrame.empty:
            self.__dataFrame = dataFrame
        else:
            if len(self.__dataFrame.columns) is not len(dataFrame.columns):
                raise ValueError("Column count does not match already imported rows")

            if not self.__headerSeen and dialect.hasHeader:
                # Aktueller DataFrame erhält Header der neu zu importierenden Datei
                newColumns = {x: y for x, y in zip(self.__dataFrame, dataFrame)}
                self.__dataFrame.rename(columns=newColumns, inplace=True)

            if self.__headerSeen and not dialect.hasHeader:
                # Aktuell zu importierende Datei erhält Header des bisherigen DataFrames
                newColumns = {x: y for x, y in zip(dataFrame, self.__dataFrame)}
                dataFrame.rename(columns=newColumns, inplace=True)

            self.__dataFrame = self.__dataFrame.append(dataFrame)

        if not self.__headerSeen and dialect.hasHeader:
            self.__headerSeen = True

    def getDictionary(self):
        return self.__dataFrame.to_dict(orient="list")

    def getLists(self):
        lists = self.__dataFrame.values.tolist()
        headerNames = list(self.__dataFrame.columns)
        lists.insert(0, headerNames)
        return lists

    def getNumPyArray(self):
        return self.__dataFrame.to_numpy()

    def getDataFrame(self):
        return self.__dataFrame

    def reset(self):
        self.__dataFrame = pandas.DataFrame()
        self.__headerSeen = False
