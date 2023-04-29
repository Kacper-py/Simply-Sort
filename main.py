import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import shutil
import sys
import os
from other import Other

from configparser import ConfigParser

# zaczytywanie pliku konfikuracyjnego
config = ConfigParser()
config.read('config.ini')
savedSource = config.get('paths', 'source')
savedtarget = config.get('paths', 'target')
savedtarget1 = config.get('paths', 'target1')
savedtarget2 = config.get('paths', 'target2')
savedtarget3 = config.get('paths', 'target3')
print(savedSource)

title = ' Simply Sort'
desc = 'Simply Sort will help you mantain\na clean and well organized\nenviroment in your data.\nIt works by just telling\nyou the schema for naming\nyour files, then you can\njust drop them in to the\npredefined folder and wait\nfor the Simply Sort to finish\nplacing your files in to\nthe right folders.\n'

class LoggerConsole(object):

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
        
        self.upperMenu = tk.Menu(self.mainWin)
        self.menuSettings = tk.Menu(self.upperMenu, tearoff=0)
        self.menuSettings.add_command(label='Paths', command=self.setPaths)
        
        self.menuMiscellaneous = tk.Menu(self.upperMenu, tearoff=0)
        self.menuMiscellaneous.add_command(label='Other Settings', command=self.setOther)
        
        self.upperMenu.add_cascade(menu=self.menuSettings, label='Settings')
        self.upperMenu.add_cascade(menu=self.menuMiscellaneous, label='Miscellaneous')
        
        self.mainWin.config(menu=self.upperMenu)
        self.upperMenu.configure(bg='#ffffff')
        
        self.Title = tk.Label(self.mainWin, text='Simply Sort', font=('Caladea', 24)).pack()
        
        # główny kontener
        self.container = tk.Frame(self.mainWin)
        self.container.columnconfigure(0, weight=1)
        self.container.columnconfigure(1, weight=1)
        
        # kontener na opis i tytuł
        self.containerDesc = tk.Frame(self.container, width=20)
        self.containerDesc.columnconfigure(0, weight=1)
        self.containerDesc.columnconfigure(1, weight=1)
        
        # kontener na wszystko inne
        self.containerFunc = tk.Frame(self.container)
        self.containerFunc.columnconfigure(0, weight=1)
        self.containerFunc.columnconfigure(1, weight=1)
        
        # tytuł schemty
        self.description = tk.Label(self.containerDesc, text='Schemas:', justify='left', font=('David Libre', 16))
        self.description.grid(row=0, column=0, sticky=tk.E+tk.W)
        
        # schemty
        self.description = tk.Label(self.containerDesc, text='Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.\nCurabitur aliquet turpis a\ntincidunt consequat. Integer\nfinibus mauris in commodo\npellentesque. Pellentesque\nauctor neque id arcu hendrerit,\nid iaculis felis faucibus.\nNam vulputate dolor neque,\nnon iaculis tortor tempus vitae.', justify='left', font=('David Libre', 11))
        self.description.grid(row=1, column=0, sticky=tk.E+tk.W)
        
        # kontener na przyciski
        self.containerButtons = tk.Frame(self.containerFunc)
        self.containerFunc.columnconfigure(0, weight=1)
        self.containerFunc.columnconfigure(1, weight=1)
        
        # przycisk "SORT!"
        self.sortButton = tk.Button(self.containerButtons, width=7, height=1, text='SORT!', font=('David Libre', 15), command=self.sortItems, disabledforeground="#363636")
        self.sortButton.grid(row=0, column=0, padx=5)
        
        # ramka z przyciskiem do autosortowania
        self.autoSGrid = tk.Frame(self.containerButtons)
        self.autoSGrid.columnconfigure(0, weight=1)
        self.autoSGrid.columnconfigure(1, weight=1)
        
        # Etykieta "ON" lub "OFF" przy przycisku "Autosort"
        self.autoSorting = tk.Label(self.autoSGrid, text='   ', font=('Consolas', 16))
        self.autoSorting.grid(row=0, column=1, sticky=tk.E+tk.W)
        
        # Przycisk "Autosort"
        self.sortingVar = 0
        self.autoSortingButton = tk.Button(self.autoSGrid, text='Auto Sorting', font=('David Libre', 15), command=self.autoSort)
        self.autoSortingButton.grid(row=0, column=0, sticky=tk.E+tk.W)
        
        self.autoSGrid.grid(row=0, column=1, padx=5)
        
        # kontener na Paths
        self.containerPaths = tk.Frame(self.containerFunc)
        self.containerPaths.columnconfigure(0, weight=1)
        self.containerPaths.columnconfigure(1, weight=1)
        
        # tytuł "Your Paths"
        self.PathsTitle = tk.Label(self.containerPaths, text="Your Paths:", font=('David Libre', 11))
        self.PathsTitle.grid(row=0, column=0)
        
        # Path 1
        self.PathsReadOnly = tk.Entry(self.containerPaths, state='normal', width=35)
        self.PathsReadOnly.grid(row=1, column=0, pady=5)
        self.PathsReadOnly.insert(tk.END, savedtarget)
        self.PathsReadOnly.configure(state='readonly')
        
        # Path2
        self.PathsReadOnly1 = tk.Entry(self.containerPaths, state='normal', width=35)
        self.PathsReadOnly1.grid(row=2, column=0, pady=5)
        self.PathsReadOnly1.insert(tk.END, savedtarget1)
        self.PathsReadOnly1.configure(state='readonly')
        
        # Path3
        self.PathsReadOnly2 = tk.Entry(self.containerPaths, state='normal', width=35)
        self.PathsReadOnly2.grid(row=3, column=0, pady=5)
        self.PathsReadOnly2.insert(tk.END, savedtarget2)
        self.PathsReadOnly2.configure(state='readonly')
        
        # Path4
        self.PathsReadOnly3 = tk.Entry(self.containerPaths, state='normal', width=35)
        self.PathsReadOnly3.grid(row=4, column=0, pady=5)
        self.PathsReadOnly3.insert(tk.END, savedtarget3)
        self.PathsReadOnly3.configure(state='readonly')
        
        # wywołania kontenerów
        self.containerPaths.grid(row=0, column=1)
        self.containerButtons.grid(row=0, column=0, sticky=tk.W, pady=20)
        self.containerFunc.grid(row=0, column=1, sticky=tk.W)
        self.containerDesc.grid(row=0, column=0, sticky=tk.E, padx=20)
        self.container.pack()
    
        self.consoleLog = ScrolledText(self.mainWin, height=50)
        self.consoleLog.pack(padx=10, pady=20)
        
        logger = LoggerConsole(self.consoleLog)
        sys.stdout = logger
        sys.stderr = logger
        
        self.mainWin.mainloop()
                
    def sortItems(self):
        print("sorting")
        # shutil.move(self.source, self.target)
            
        
    def autoSort(self):
        self.sortingVar += 1
        if self.sortingVar % 2 != 0:
            self.autoSorting['text'] = "ON "
            self.autoSorting.configure(bg='#00ff00')
            self.sortButton['state'] = 'disabled'
            self.sortButton['text'] = ' ... '
            print('Autosorting ON')
        elif self.sortingVar % 2 == 0:
            self.autoSorting['text'] = "OFF"
            self.autoSorting.configure(bg='#ff0000')
            self.sortButton['state'] = 'normal'
            self.sortButton['text'] = 'SORT!'
            print('Autosorting OFF')
    
    def setPaths(self):
        os.system('python.exe paths.py')
    
    def setOther(self):
        Other()
        
        
Main()
