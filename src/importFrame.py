from tkinter import *
from dialect import Dialect


class ImportFrame:
    def __init__(self, gui, filePath: str):
        self.gui = gui
        self.filePath = filePath
        self.dialect = Dialect()

        self.frame = LabelFrame(gui.importsFrame, text=filePath)
        self.frame.pack(fill=X, padx=10, pady=5)

        self.varEncoding = StringVar()
        self.labelEncoding = Label(self.frame, text="Encoding: ")
        self.labelEncoding.grid(row=0, column=0, sticky="E")
        self.entryEncoding = Entry(self.frame, width=10, textvariable=self.varEncoding)
        self.entryEncoding.grid(row=0, column=1, sticky="W")

        self.varHasHeader = BooleanVar()
        self.labelHasHeader = Label(self.frame, text="Has Header: ")
        self.labelHasHeader.grid(row=1, column=0, sticky="E")
        self.checkbuttonHasHeader = Checkbutton(self.frame, variable=self.varHasHeader)
        self.checkbuttonHasHeader.grid(row=1, column=1, sticky="W")

        self.varSepChar = StringVar()
        self.labelSepChar = Label(self.frame, text="Seperator Character: ")
        self.labelSepChar.grid(row=2, column=0, sticky="E")
        self.entrySepChar = Entry(self.frame, width=4, textvariable=self.varSepChar)
        self.entrySepChar.grid(row=2, column=1, sticky="W")

        self.varQuoteChar = StringVar()
        self.labelQuoteChar = Label(self.frame, text="Quote Character: ")
        self.labelQuoteChar.grid(row=3, column=0, sticky="E")
        self.entryQuoteChar = Entry(self.frame, width=4, textvariable=self.varQuoteChar)
        self.entryQuoteChar.grid(row=3, column=1, sticky="W")

        self.buttonReset = Button(
            self.frame,
            text="Reset Dialect",
            command=self.resetDialect
        )
        self.buttonReset.grid(row=4, column=0)

        self.buttonRemove = Button(
            self.frame,
            text="Remove Import",
            command=lambda: gui.onRemoveImportFrame(self)
        )
        self.buttonRemove.grid(row=4, column=1)

        self.errorMessage = StringVar()
        self.labelError = Label(self.frame, textvariable=self.errorMessage, fg="red")
        self.labelError.grid(row=5, column=0, columnspan=2)

        self.resetDialect()
        self.setupVarTracer()

    def setupVarTracer(self):
        varTracer = lambda var, index, mode: self.onFieldChange()
        self.varEncoding.trace("w", varTracer)
        self.varHasHeader.trace("w", varTracer)
        self.varSepChar.trace("w", varTracer)
        self.varQuoteChar.trace("w", varTracer)

        self.isTraceActive = True
    
    def onFieldChange(self):
        if self.isTraceActive:
            self.updateDialect()
            self.gui.updatePreview()

    def resetDialect(self):
        self.isTraceActive = False

        self.dialect.guessFromFile(self.filePath)

        self.varEncoding.set(self.dialect.encoding)
        self.varHasHeader.set(self.dialect.hasHeader)
        self.varSepChar.set(self.dialect.sepChar)
        self.varQuoteChar.set(self.dialect.quoteChar)

        self.isTraceActive = True
        self.onFieldChange()


    def updateDialect(self):
        self.dialect.encoding = self.varEncoding.get()
        self.dialect.hasHeader = self.varHasHeader.get()
        self.dialect.sepChar = self.varSepChar.get()
        self.dialect.quoteChar = self.varQuoteChar.get()

    def clearError(self):
        self.errorMessage.set("")

    def setError(self, message: str):
        self.errorMessage.set(message)

