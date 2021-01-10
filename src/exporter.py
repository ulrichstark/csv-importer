import pandas
from lxml import etree
from importer import Importer


class Exporter:
    """
    Class used to export the imported rows from an Importer
    """
    __dataFrame: pandas.DataFrame

    def __init__(self, importer: Importer):
        self.__dataFrame = importer.getDataFrame()

    def exportCSVFile(self, filePath: str, encoding: str, sepChar: str, quoteChar: str):
        """
        Export the imported rows to a CSV file with specified format
        """
        self.__dataFrame.to_csv(
            filePath,
            encoding=encoding,
            sep=sepChar,
            quotechar=quoteChar,
            index=False
        )

    def exportXMLFile(self, filePath: str, encoding: str):
        """
        Export the imported rows to a XML file with specified encoding
        """
        itemsElement = etree.Element("items")

        for _, row in self.__dataFrame.iterrows():
            itemElement = etree.SubElement(itemsElement, "item")

            for field in row.index:
                fieldElement = etree.SubElement(itemElement, field)
                fieldElement.text = str(row[field])

        document = etree.ElementTree(itemsElement)
        document.write(filePath, xml_declaration=True, pretty_print=True, encoding=encoding)
