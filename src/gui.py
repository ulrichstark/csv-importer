from dialect import Dialect
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *


def onImportButtonClick():
    selectedFileName = askopenfilename(initialdir="../example")

    if selectedFileName is not None:
        if selectedFileName.endswith(".csv"):
            guessedDialect = Dialect(selectedFileName)
            applyDialect(guessedDialect)
        else:
            showerror(
                message=f"Your selected file '{selectedFileName}' is not a csv file!"
            )


def applyDialect(dialect: Dialect):
    varEncoding.set(dialect.encoding)
    varHasHeader.set(dialect.hasHeader)
    varSepChar.set(dialect.sepChar)
    varQuoteChar.set(dialect.quoteChar)


if __name__ == "__main__":
    window = Tk()
    window.title("Excel 2.0")
    window.minsize(400, 400)

    importButton = Button(
        window,
        text="Import file(s)",
        command=onImportButtonClick
    )
    importButton.grid(row=0, column=0)

    varEncoding = StringVar()
    labelEncoding = Label(window, text="Encoding: ")
    labelEncoding.grid(row=1, column=0, sticky="E")
    entryEncoding = Entry(window, width=10, textvariable=varEncoding)
    entryEncoding.grid(row=1, column=1, sticky="W")

    varHasHeader = IntVar()
    labelHasHeader = Label(window, text="Has Header: ")
    labelHasHeader.grid(row=2, column=0, sticky="E")
    checkbuttonHasHeader = Checkbutton(window, variable=varHasHeader)
    checkbuttonHasHeader.grid(row=2, column=1, sticky="W")

    varSepChar = StringVar()
    labelSepChar = Label(window, text="Seperator Character: ")
    labelSepChar.grid(row=3, column=0, sticky="E")
    entrySepChar = Entry(window, width=4, textvariable=varSepChar)
    entrySepChar.grid(row=3, column=1, sticky="W")

    varQuoteChar = StringVar()
    labelQuoteChar = Label(window, text="Quote Character: ")
    labelQuoteChar.grid(row=4, column=0, sticky="E")
    entryQuoteChar = Entry(window, width=4, textvariable=varQuoteChar)
    entryQuoteChar.grid(row=4, column=1, sticky="W")

    window.mainloop()
