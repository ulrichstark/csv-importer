from dialect import Dialect
from importer import Importer
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from pandastable import Table


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
        self.importButton.grid(row=0, column=0)

        self.varEncoding = StringVar()
        self.labelEncoding = Label(self.window, text="Encoding: ")
        self.labelEncoding.grid(row=1, column=0, sticky="E")
        self.entryEncoding = Entry(
            self.window, width=10, textvariable=self.varEncoding)
        self.entryEncoding.grid(row=1, column=1, sticky="W")

        self.varHasHeader = IntVar()
        self.labelHasHeader = Label(self.window, text="Has Header: ")
        self.labelHasHeader.grid(row=2, column=0, sticky="E")
        self.checkbuttonHasHeader = Checkbutton(
            self.window, variable=self.varHasHeader)
        self.checkbuttonHasHeader.grid(row=2, column=1, sticky="W")

        self.varSepChar = StringVar()
        self.labelSepChar = Label(self.window, text="Seperator Character: ")
        self.labelSepChar.grid(row=3, column=0, sticky="E")
        self.entrySepChar = Entry(
            self.window, width=4, textvariable=self.varSepChar)
        self.entrySepChar.grid(row=3, column=1, sticky="W")

        self.varQuoteChar = StringVar()
        self.labelQuoteChar = Label(self.window, text="Quote Character: ")
        self.labelQuoteChar.grid(row=4, column=0, sticky="E")
        self.entryQuoteChar = Entry(
            self.window, width=4, textvariable=self.varQuoteChar)
        self.entryQuoteChar.grid(row=4, column=1, sticky="W")

        self.window.mainloop()

    def onImportButtonClick(self):
        selectedFileName = askopenfilename(initialdir="../example")

        if selectedFileName is not None:
            if selectedFileName.endswith(".csv"):
                guessedDialect = Dialect(selectedFileName)
                self.applyDialect(guessedDialect)

                importer = Importer()
                importer.importCSVFile(selectedFileName, guessedDialect)

                dataFrame = importer.getDataFrame()
                print(dataFrame)
                Table(self.window, dataframe=dataFrame)
            else:
                showerror(
                    message=f"Your selected file '{selectedFileName}' is not a csv file!"
                )

    def applyDialect(self, dialect: Dialect):
        self.varEncoding.set(dialect.encoding)
        self.varHasHeader.set(dialect.hasHeader)
        self.varSepChar.set(dialect.sepChar)
        self.varQuoteChar.set(dialect.quoteChar)


if __name__ == "__main__":
    GUI()
