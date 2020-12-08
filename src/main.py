from importer import Importer
from exporter import Exporter
from dialect import Dialect

testFilePath = "../example/regex_test.csv"

importer = Importer()

dialect = Dialect(testFilePath)

importer.importCSVFile(testFilePath, dialect)
importer.importCSVFile(testFilePath, dialect)

exporter = Exporter(importer)

exporter.exportCSVFile("sample_export.csv", "utf-8", ",")
