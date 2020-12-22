from tkinter.constants import X
from tkinter.filedialog import asksaveasfilename
from tkinter import Button, Frame, Tk, Toplevel, ttk
from tkinter.messagebox import showerror, showinfo

from exporter import Exporter
from util import formatExceptionMessage


class ExportWindow:
    def __init__(self, window: Tk, exporter: Exporter):
        self.window = window
        self.exporter = exporter

        self.toplevel = Toplevel(window)
        self.toplevel.title("Export as...")
        self.toplevel.minsize(300, 200)

        self.tabs = ttk.Notebook(self.toplevel)

        self.frameCSV = Frame(self.tabs)
        self.tabs.add(self.frameCSV, text="CSV")

        self.buttonExportCSV = Button(self.frameCSV, text="Export", command=self.onExportCSV)
        self.buttonExportCSV.grid(row=0, column=0, padx=6, pady=6)
        
        self.frameXML = Frame(self.tabs)
        self.tabs.add(self.frameXML, text="XML")

        self.buttonExportXML = Button(self.frameXML, text="Export", command=self.onExportXML)
        self.buttonExportXML.grid(row=0, column=0, padx=6, pady=6)

        self.tabs.pack(fill=X, pady=6)

    def onExportCSV(self):
        filePath = asksaveasfilename(
            parent=self.toplevel,
            defaultextension=".csv",
            filetypes=[
                ("Comma-Seperated Values", "*.csv"),
                ("All files", "*.*")
            ]
        )

        if filePath:
            encoding = "utf-8"
            sepChar = ","
            quoteChar = "\""

            try:
                self.exporter.exportCSVFile(filePath, encoding, sepChar, quoteChar)

                showinfo(title="Sucess", message=f"Your CSV-File '{filePath}' was sucessfully exported")
            except Exception as error:
                errorMessage = formatExceptionMessage(error)
                showerror(title="Error while exporting CSV file", message=errorMessage)


    def onExportXML(self):
        filePath = asksaveasfilename(
            parent=self.toplevel,
            defaultextension=".xml",
            filetypes=[
                ("Extensible Markup Language", "*.xml"),
                ("All files", "*.*")
            ]
        )

        if filePath:
            encoding = "utf-8"

            try:
                self.exporter.exportXMLFile(filePath, encoding)

                showinfo(title="Sucess", message=f"Your XML-File '{filePath}' was sucessfully exported")
            except Exception as error:
                errorMessage = formatExceptionMessage(error)
                showerror(title="Error while exporting XML file", message=errorMessage)