import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import os
import sys
import time
from paths import Paths
from other import Other

title = ' Simply Sort'
desc = 'Simply Sort will help you mantain a clean and\nwell organized enviroment in your data. It works by just\ntelling you the schema for naming your files,\nthen you can just drop them in to the predefined folder and wait for the\n Simply Sort to finish placing your files in to the right folders.'

class Logger(object):

    def __init__(self, textbox):
        self.textbox = textbox

    def write(self, text):
        self.textbox.configure(state="normal")
        self.textbox.insert("end", text)
        self.textbox.see("end")
        self.textbox.configure(state="disabled")

    def flush(self):
        pass

class Main:
    def __init__(self):
        
        self.mainWin = tk.Tk(className=title)
        self.mainWin.geometry('800x500')
        self.mainWin.configure(bg='#ffffff')
        
        self.upperMenu = tk.Menu(self.mainWin)
        self.menuSettings = tk.Menu(self.upperMenu, tearoff=0)
        self.menuSettings.add_command(label='Paths', command=self.setPaths)
        
        self.menuMiscellaneous = tk.Menu(self.upperMenu, tearoff=0)
        self.menuMiscellaneous.add_command(label='Other Settings', command=self.setOther)
        
        self.upperMenu.add_cascade(menu=self.menuSettings, label='Settings')
        self.upperMenu.add_cascade(menu=self.menuMiscellaneous, label='Miscellaneous')
        
        self.mainWin.config(menu=self.upperMenu)
        self.upperMenu.configure(bg='#ffffff')
        
        self.header = tk.Label(self.mainWin, text='Sorting', font=('Consolas', 18))
        self.header.pack(padx=10, pady=10)
        self.header.configure(bg='#ffffff')
        
        self.desciption = tk.Label(self.mainWin, text=desc, font=('Consolas', 12))
        self.desciption.pack(padx=10, pady=10)
        self.desciption.configure(bg='#ffffff')
        
        self.sortButton = tk.Button(self.mainWin, width=10, text='SORT!', font=('Segoe Print', 16), command=self.sortItems, disabledforeground="white")
        self.sortButton.pack(pady=20)
        
        self.autoSGrid = tk.Frame(self.mainWin)
        self.autoSGrid.columnconfigure(0, weight=1)
        self.autoSGrid.columnconfigure(1, weight=1)
        self.autoSGrid.configure(bg='#ffffff')
        
        self.autoSorting = tk.Label(self.autoSGrid, text='   ', font=('Consolas', 16))
        self.autoSorting.configure(bg='#ffffff')
        self.autoSorting.grid(row=0, column=1, sticky=tk.E+tk.W)
        
        self.sortingVar = 0
        self.autoSortingButton = tk.Button(self.autoSGrid, text='Auto Sorting', font=('Consolas', 15), command=self.autoSort)
        self.autoSortingButton.grid(row=0, column=0, sticky=tk.E+tk.W)
        
        self.autoSGrid.pack()
        
        self.consoleLog = ScrolledText(self.mainWin, height=50)
        self.consoleLog.pack(padx=10, pady=20)
        
        logger = Logger(self.consoleLog)
        sys.stdout = logger
        sys.stderr = logger
        
        self.mainWin.mainloop()
        
    def sortItems(self):
        messagebox.showinfo(title='In construction...', message='We are working on it :)')
        
    def autoSort(self):
        self.sortingVar += 1
        if self.sortingVar % 2 != 0:
            self.autoSorting['text'] = "ON "
            self.autoSorting.configure(bg='#00ff00')
            self.sortButton['state'] = 'disabled'
            self.sortButton['text'] = 'Autosorting ON'
            print('Autosorting ON')
            self.sortButton['width'] = '14'
        elif self.sortingVar % 2 == 0:
            self.autoSorting['text'] = "OFF"
            self.autoSorting.configure(bg='#ff0000')
            self.sortButton['state'] = 'normal'
            self.sortButton['text'] = 'SORT!'
            print('Autosorting OFF')
            self.sortButton['width'] = '10'
    
    def setPaths(self):
        Paths()
    
    def setOther(self):
        Other()
        
        
Main()