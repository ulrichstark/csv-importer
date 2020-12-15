from importer import Importer
from exporter import Exporter
from dialect import Dialect

importer = Importer()

def importCSV(filePath: str):
    dialect = Dialect()
    dialect.guessFromFile(filePath)
    importer.importCSVFile(filePath, dialect)

importCSV("../example/regex_test.csv")
importCSV("../example/regex_test_mit_header.csv")

print(importer.getDataFrame())

exporter = Exporter(importer)

exporter.exportCSVFile("sample_export.csv", "utf-8", ",")
