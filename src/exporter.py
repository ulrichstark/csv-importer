import pandas
from importer import Importer


class Exporter:
    __dataFrame: pandas.DataFrame

    def __init__(self, importer: Importer):
        self.__dataFrame = importer.getDataFrame()

    def exportCSVFile(self, filePath: str, encoding: str, seperator: str):
        self.__dataFrame.to_csv(
            filePath, index=False, encoding=encoding, sep=seperator)

    def exportXMLFile(self):
        pass
