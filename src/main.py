from importer import Importer

testFilePath = "../example/regex_test.csv"

importer = Importer()

importer.importCSVFile(testFilePath, encoding="utf-8", headerPresent=True)
importer.importCSVFile(testFilePath, encoding="utf-8", headerPresent=False)

importer.exportCSVFile("sample_export.csv", "utf-8", ",")
