from importer import Importer
from importFrameCSV import ImportFrameCSV
from importFrameXML import ImportFrameXML
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from pandastable import Table, TableModel


class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Excel 2.0")
        self.window.minsize(400, 400)

        self.importButton = Button(
            self.window,
            text="Import file(s)",
            command=self.onImportButtonClick
        )
        self.importButton.pack(pady=20)

        self.importsFrame = Frame(self.window)
        self.importsFrame.pack(fill=X, padx=10, pady=5)

        self.previewFrame = Frame(self.window)
        self.previewFrame.pack(fill=X, padx=10, pady=5)

        self.table = Table(self.previewFrame)

        self.importFrameList = []
        self.isTableShown = False

        self.window.mainloop()

    def onImportButtonClick(self):
        filePathList = askopenfilenames(initialdir="../example")

        for filePath in filePathList:
            self.importFile(filePath)

        if len(self.importFrameList) > 0:
            self.updatePreview()

    def onRemoveImportFrame(self, importFrame):
        importFrame.frame.destroy()
        
        self.importFrameList.remove(importFrame)
        self.updatePreview()

    def importFile(self, filePath: str):
        if filePath.endswith(".csv"):
            importFrame = ImportFrameCSV(self, filePath)
            self.importFrameList.append(importFrame)
        elif filePath.endswith(".xml"):
            importFrame = ImportFrameXML(self, filePath)
            self.importFrameList.append(importFrame)
        else:
            showerror(message=f"Your selected file '{filePath}' is not a csv or xml file!")

    def updatePreview(self):
        importer = Importer()

        for importFrame in self.importFrameList:
            try:
                importFrame.importFile(importer)
                importFrame.clearError()
            except Exception as error:
                errorMessage = error.__class__.__name__ + ": " + str(error)
                importFrame.setError(errorMessage)

        dataFrame = importer.getDataFrame()

        if self.isTableShown is False:
            self.isTableShown = True
            self.table.show()

        if dataFrame is not None:
            tableModel = TableModel(dataFrame)
            self.table.updateModel(tableModel)
            self.table.redraw()

if __name__ == "__main__":
    GUI()
