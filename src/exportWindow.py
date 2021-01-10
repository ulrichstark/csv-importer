from tkinter.constants import X
from tkinter.filedialog import asksaveasfilename
from tkinter import Button, Entry, Frame, Label, StringVar, Tk, Toplevel, ttk
from tkinter.messagebox import showerror, showinfo

from exporter import Exporter
from util import formatExceptionMessage


class ExportWindow:
    """
    Secondary window used to export the imported rows to a CSV or XML file
    """
    def __init__(self, window: Tk, exporter: Exporter):
        self.window = window
        self.exporter = exporter

        self.toplevel = Toplevel(window)
        self.toplevel.title("Export as...")
        self.toplevel.minsize(300, 200)

        self.varEncoding = StringVar(value="utf-8")
        self.varSepChar = StringVar(value=",")
        self.varQuoteChar = StringVar(value="\"")

        self.tabs = ttk.Notebook(self.toplevel)

        self.frameCSV = Frame(self.tabs)
        self.tabs.add(self.frameCSV, text="CSV")

        self.labelEncodingCSV = Label(self.frameCSV, text="Encoding: ")
        self.labelEncodingCSV.grid(row=0, column=0, sticky="E")
        self.entryEncodingCSV = Entry(self.frameCSV, width=10, textvariable=self.varEncoding)
        self.entryEncodingCSV.grid(row=0, column=1, sticky="W")

        self.labelSepChar = Label(self.frameCSV, text="Seperator Character: ")
        self.labelSepChar.grid(row=1, column=0, sticky="E")
        self.entrySepChar = Entry(self.frameCSV, width=4, textvariable=self.varSepChar)
        self.entrySepChar.grid(row=1, column=1, sticky="W")

        self.labelQuoteChar = Label(self.frameCSV, text="Quote Character: ")
        self.labelQuoteChar.grid(row=2, column=0, sticky="E")
        self.entryQuoteChar = Entry(self.frameCSV, width=4, textvariable=self.varQuoteChar)
        self.entryQuoteChar.grid(row=2, column=1, sticky="W")

        self.buttonExportCSV = Button(self.frameCSV, text="Export", command=self.onExportCSV)
        self.buttonExportCSV.grid(row=3, column=0, padx=6, pady=6)
        
        self.frameXML = Frame(self.tabs)
        self.tabs.add(self.frameXML, text="XML")

        self.labelEncodingXML = Label(self.frameXML, text="Encoding: ")
        self.labelEncodingXML.grid(row=0, column=0, sticky="E")
        self.labelEncodingXML = Entry(self.frameXML, width=10, textvariable=self.varEncoding)
        self.labelEncodingXML.grid(row=0, column=1, sticky="W")

        self.buttonExportXML = Button(self.frameXML, text="Export", command=self.onExportXML)
        self.buttonExportXML.grid(row=1, column=0, padx=6, pady=6)

        self.tabs.pack(fill=X, pady=6)

    def onExportCSV(self):
        """
        Called when the "Export" button was clicked in the "CSV" tab
        """
        filePath = asksaveasfilename(
            parent=self.toplevel,
            defaultextension=".csv",
            filetypes=[
                ("Comma-Seperated Values", "*.csv"),
                ("All files", "*.*")
            ]
        )

        if filePath:
            # only continue if the user selected a filePath
            encoding = self.varEncoding.get()
            sepChar = self.varSepChar.get()
            quoteChar = self.varQuoteChar.get()

            try:
                self.exporter.exportCSVFile(filePath, encoding, sepChar, quoteChar)

                showinfo(title="Sucess", message=f"Your CSV-File '{filePath}' was sucessfully exported")
            except Exception as error:
                errorMessage = formatExceptionMessage(error)
                showerror(title="Error while exporting CSV file", message=errorMessage)


    def onExportXML(self):
        """
        Called when the "Export" button was clicked in the "XML" tab
        """
        filePath = asksaveasfilename(
            parent=self.toplevel,
            defaultextension=".xml",
            filetypes=[
                ("Extensible Markup Language", "*.xml"),
                ("All files", "*.*")
            ]
        )

        if filePath:
            # only continue if the user selected a filePath
            encoding = self.varEncoding.get()

            try:
                self.exporter.exportXMLFile(filePath, encoding)

                showinfo(title="Sucess", message=f"Your XML-File '{filePath}' was sucessfully exported")
            except Exception as error:
                errorMessage = formatExceptionMessage(error)
                showerror(title="Error while exporting XML file", message=errorMessage)