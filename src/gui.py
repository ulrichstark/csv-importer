from tkinter.constants import X
from exporter import Exporter
from importer import Importer
from importFrameCSV import ImportFrameCSV
from importFrameXML import ImportFrameXML
from util import formatExceptionMessage
from exportWindow import ExportWindow
from tkinter import Tk, Button, Frame
from tkinter.filedialog import askopenfilenames
from tkinter.messagebox import showerror
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

    def onExportClick(self):
        if self.importer:
            exporter = Exporter(self.importer)
            ExportWindow(self.window, exporter)

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
        self.importer = Importer()

        for importFrame in self.importFrameList:
            try:
                importFrame.importFile(self.importer)
                importFrame.clearError()
            except Exception as error:
                errorMessage = formatExceptionMessage(error)
                importFrame.setError(errorMessage)

        dataFrame = self.importer.getDataFrame()

        if self.isTableShown is False:
            self.isTableShown = True
            self.table.show()

            self.exportButton = Button(self.window, text="Export", command=self.onExportClick)
            self.exportButton.pack(pady=10)

        if dataFrame is not None:
            tableModel = TableModel(dataFrame)
            self.table.updateModel(tableModel)
            self.table.redraw()

if __name__ == "__main__":
    GUI()
