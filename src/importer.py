import pandas


class Importer:
    __dataFrame: pandas.DataFrame
    __columnCount: int

    def __init__(self):
        self.reset()

    def importCSVFile(self, filePath: str, encoding: str, headerPresent: bool):
        header = "infer" if headerPresent else None
        dataFrame = pandas.read_csv(filePath, encoding=encoding, header=header)
        columnCount = len(dataFrame.columns)

        if self.__dataFrame is None:
            self.__dataFrame = dataFrame
            self.__columnCount = columnCount
        else:
            if self.__columnCount is not columnCount:
                raise ValueError(
                    "Column count does not match already imported rows")

            self.__dataFrame = self.__dataFrame.append(dataFrame)

    def exportLists(self):
        pass

    def exportNumPyArray(self):
        pass

    def exportDataFrame(self):
        return self.__dataFrame

    def exportCSVFile(self, filePath: str, encoding: str, seperator: str):
        self.__dataFrame.to_csv(
            filePath, index=False, encoding=encoding, sep=seperator)

    def exportXMLFile(self):
        pass

    def reset(self):
        self.__dataFrame = None
