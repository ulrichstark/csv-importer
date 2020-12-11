from importer import Importer
from exporter import Exporter
from dialect import Dialect

testFilePath = "../example/regex_test.csv"

importer = Importer()

importer.importCSVFile("../example/regex_test.csv",
                       Dialect("../example/regex_test.csv"))

importer.importCSVFile("../example/regex_test_mit_header.csv",
                       Dialect("../example/regex_test_mit_header.csv"))

print(importer.getDataFrame())

exporter = Exporter(importer)

exporter.exportCSVFile("sample_export.csv", "utf-8", ",")
