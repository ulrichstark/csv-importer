import os
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from importer import Importer


class ImportFrameXML:
    def __init__(self, gui, filePath: str):
        self.gui = gui
        self.xmlFilePath = filePath
        self.xslFilePath = None

        self.frame = LabelFrame(gui.importsFrame, text=filePath)
        self.frame.pack(fill=X, padx=10, pady=5)

        self.varXSLFilePath = StringVar(value="-")
        self.labelXSLFilePath = Label(self.frame, text="XSL File: ")
        self.labelXSLFilePath.grid(row=0, column=0, sticky="E")
        self.outputXSLFilePath = Label(self.frame, textvariable=self.varXSLFilePath)
        self.outputXSLFilePath.grid(row=0, column=1, sticky="W")

        self.buttonXSLFile = Button(
            self.frame,
            text="Select XSL File",
            command=self.onSelectXSLFile
        )
        self.buttonXSLFile.grid(row=1, column=0, padx=8, pady=4)

        self.buttonRemove = Button(
            self.frame,
            text="Remove Import",
            command=lambda: gui.onRemoveImportFrame(self)
        )
        self.buttonRemove.grid(row=1, column=1, padx=8, pady=4)

        self.errorMessage = StringVar()
        self.labelError = Label(self.frame, textvariable=self.errorMessage, fg="red")
        self.labelError.grid(row=3, column=0, columnspan=2)

        self.setupVarTracer()

    def onSelectXSLFile(self):
        filePath = askopenfilename(initialdir="../example")

        if filePath is not None and len(filePath) > 0:
            if filePath.endswith(".xsl"):
                self.xslFilePath = filePath
                selectedFileName = os.path.basename(filePath)
                self.varXSLFilePath.set(selectedFileName)
            else:
                showerror(message=f"Your selected file '{filePath}' is not a xsl file!")

    def importFile(self, importer: Importer):
        if self.xslFilePath is None:
            raise ValueError("No XSL File specified!")
        else:
            importer.importXMLFile(self.xmlFilePath, self.xslFilePath)

    def setupVarTracer(self):
        varTracer = lambda var, index, mode: self.onFieldChange()

        self.varXSLFilePath.trace("w", varTracer)
    
    def onFieldChange(self):
        self.gui.updatePreview()

    def clearError(self):
        self.errorMessage.set("")

    def setError(self, message: str):
        self.errorMessage.set(message)

