from importer import Importer
from dialect import Dialect

testFilePath = "../example/regex_test.csv"

importer = Importer()

dialect = Dialect(testFilePath)

importer.importCSVFile(testFilePath, dialect)
importer.importCSVFile(testFilePath, dialect)

importer.exportCSVFile("sample_export.csv", "utf-8", ",")
