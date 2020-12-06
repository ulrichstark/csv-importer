from importer import Importer

testFilePath = "../example/regex_test.csv"

importer = Importer()

importer.importCSVFile(testFilePath)
importer.importCSVFile(testFilePath)

importer.export("sample_export.csv", newline="")
