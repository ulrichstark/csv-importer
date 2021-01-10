import pandas
import guess
from io import StringIO
from lxml import etree
from dialect import Dialect


class Importer:
    """
    Class used to dynamically add csv or xml files to import.
    Importer merges them all into an internal DataFrame.
    Can be resetted for future use with new clean internal state.
    Also offers methods to convert merged state to dictionary, lists of lists, numpy array 
    """
    __dataFrame: pandas.DataFrame
    __headerSeen: bool

    def __init__(self):
        self.reset()

    def importXMLFile(self, xmlFilePath: str, xslFilePath: str, xslParameters = {}):
        """
        Imports a xml file by using its filePath along the filePath to its corresponding xsl file for transforming.
        xslParameters can also be supplied to change parameter values of the xsl transformer.
        """
        xmlFile = etree.parse(xmlFilePath)
        xslFile = etree.parse(xslFilePath)
        transformer = etree.XSLT(xslFile)

        transformedOutput = str(transformer(xmlFile, **xslParameters))

        dialect = Dialect()
        dialect.guessFromSample(transformedOutput)

        buffer = StringIO(transformedOutput)

        self.importCSVFile(buffer, dialect)


    def importCSVFile(self, filePathOrBuffer: str, dialect: Dialect):
        """
        Imports a csv file by using its filePath or a buffer containing a csv-formatted string.
        Use the dialect parameter to further specify the format of the csv file/string.
        """
        header = "infer" if dialect.hasHeader else None
        dataFrame = pandas.read_csv(
            filePathOrBuffer,
            sep=dialect.sepChar,
            quotechar=dialect.quoteChar,
            encoding=dialect.encoding,
            header=header
        )

        if dialect.hasHeader is False:
            # guess header names if csv file has none
            newColumns = guess.headerNames(dataFrame)
            dataFrame.rename(columns=newColumns, inplace=True)

        if self.__dataFrame.empty:
            # just set the new imported DataFrame if no internal DataFrame is set yet
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
            # did we get a valid header from the currently imported file for the first time?
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
        """
        Reset the internal state to restart importing
        """
        self.__dataFrame = pandas.DataFrame()
        self.__headerSeen = False
