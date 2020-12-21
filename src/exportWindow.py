from tkinter.constants import X
import pandas
from tkinter import Frame, Tk, Toplevel
from tkinter import ttk


class ExportWindow:
    def __init__(self, window: Tk, dataFrame: pandas.DataFrame):
        self.window = window
        self.dataFrame = dataFrame

        self.toplevel = Toplevel(window)
        self.toplevel.title("Export as...")

        self.tabs = ttk.Notebook(self.toplevel)

        self.frameCSV = Frame(self.tabs)
        self.tabs.add(self.frameCSV, text="CSV")
        
        self.frameXML = Frame(self.tabs)
        self.tabs.add(self.frameXML, text="XML")

        self.tabs.pack(fill=X, pady=6)