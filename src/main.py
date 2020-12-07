from importer import Importer

testFilePath = "../example/regex_test.csv"

importer = Importer()

importer.importCSVFile(testFilePath, headerPresent=False)
importer.importCSVFile(testFilePath, headerPresent=False)

importer.exportCSVFile("sample_export.csv", "utf-8", ",")
