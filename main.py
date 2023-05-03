import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import shutil
import sys
import os
import time
from threading import Thread
from configparser import ConfigParser

# zaczytywanie pliku konfikuracyjnego
config = ConfigParser()
config.read('config.ini')
savedSource = config.get('paths', 'source')
savedtarget = config.get('paths', 'target')
savedtarget1 = config.get('paths', 'target1')
savedtarget2 = config.get('paths', 'target2')
savedtarget3 = config.get('paths', 'target3')
savedSchema = config.get('schemas', 'schema')
savedSchema1 = config.get('schemas', 'schema1')
savedSchema2 = config.get('schemas', 'schema2')
savedSchema3 = config.get('schemas', 'schema3')

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
        self.mainWin.geometry('750x400')
        
        self.upperMenu = tk.Menu(self.mainWin)
        self.menuSettings = tk.Menu(self.upperMenu, tearoff=0)
        self.menuSettings.add_command(label='Paths', command=self.setPaths)
        self.menuSettings.add_command(label='Schemas', command=self.setOther)
        
        self.upperMenu.add_cascade(menu=self.menuSettings, label='Settings')
        
        self.mainWin.config(menu=self.upperMenu)
        self.upperMenu.configure(bg='#ffffff')
        
        self.Title = tk.Label(self.mainWin, text='Simply Sort', font=('Caladea', 24)).pack()
        
        self.PathsReadOnly = tk.Entry(self.mainWin, state='normal', width=35)
        self.PathsReadOnly.pack(pady=5)
        self.PathsReadOnly.insert(tk.END, savedSource)
        self.PathsReadOnly.configure(state='readonly')
        
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
        
        # schema 1
        self.PathsReadOnly = tk.Entry(self.containerDesc, state='normal', width=35)
        self.PathsReadOnly.grid(row=1, column=0, pady=5)
        self.PathsReadOnly.insert(tk.END, savedSchema)
        self.PathsReadOnly.configure(state='readonly')
        
        # Path2
        self.PathsReadOnly1 = tk.Entry(self.containerDesc, state='normal', width=35)
        self.PathsReadOnly1.grid(row=2, column=0, pady=5)
        self.PathsReadOnly1.insert(tk.END, savedSchema1)
        self.PathsReadOnly1.configure(state='readonly')
        
        # Path3
        self.PathsReadOnly2 = tk.Entry(self.containerDesc, state='normal', width=35)
        self.PathsReadOnly2.grid(row=3, column=0, pady=5)
        self.PathsReadOnly2.insert(tk.END, savedSchema2)
        self.PathsReadOnly2.configure(state='readonly')
        
        # Path4
        self.PathsReadOnly3 = tk.Entry(self.containerDesc, state='normal', width=35)
        self.PathsReadOnly3.grid(row=4, column=0, pady=5)
        self.PathsReadOnly3.insert(tk.END, savedSchema3)
        self.PathsReadOnly3.configure(state='readonly')
        
        # kontener na przyciski
        self.containerButtons = tk.Frame(self.containerFunc)
        self.containerFunc.columnconfigure(0, weight=1)
        self.containerFunc.columnconfigure(1, weight=1)
        
        # przycisk "SORT!"
        self.sortButton = tk.Button(self.containerButtons, width=7, height=1, text='SORT!', font=('David Libre', 15), command=self.sortStart, disabledforeground="#363636")
        self.sortButton.grid(row=0, column=0, padx=2)
        
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
        self.PathsTitle = tk.Label(self.containerPaths, text="Your Paths:", font=('David Libre', 16))
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
    
    def sortStart(self):
        self.sortThread = Thread(target = self.sortItems)
        self.sortThread.start()
                
    def sortItems(self):
        if os.path.isdir(savedSource) is False:
            print('Path that you entered cannot be found! :(')
        else:
            dir = os.listdir(savedSource)
            if len(dir) == 0:
                print('Your sorting folder is empty!')
            else:
                print("--------------------------------------------------------------------------------\nStarting sorting...\n--------------------------------------------------------------------------------")
                for file in os.listdir(savedSource):
                    if file.endswith(savedSchema):
                        if os.path.exists(savedtarget) is True:
                            shutil.move(f'{savedSource}/{file}', savedtarget)
                            print(f'Sorting to {savedtarget.upper()} directory finished succesfuly')
                        elif os.path.exists(savedtarget) is False:
                            print(f'Path {savedtarget.upper()} does not exist!')
                    elif file.endswith(savedSchema1):
                        if os.path.exists(savedtarget1) is True:
                            shutil.move(f'{savedSource}/{file}', savedtarget1)
                            print(f'Sorting to {savedtarget1.upper()} directory finished succesfuly')
                        elif os.path.exists(savedtarget1) is False:
                            print(f'Path {savedtarget1.upper()} does not exist!')
                    elif file.endswith(savedSchema2):
                        if os.path.exists(savedtarget2) is True:
                            shutil.move(f'{savedSource}/{file}', savedtarget2)
                            print(f'Sorting to {savedtarget2.upper()} directory finished succesfuly')
                        elif os.path.exists(savedtarget2) is False:
                            print(f'Path {savedtarget2.upper()} does not exist!')
                    elif file.endswith(savedSchema3):
                        if os.path.exists(savedtarget3) is True:
                            shutil.move(f'{savedSource}/{file}', savedtarget3)
                            print(f'Sorting to {savedtarget3.upper()} directory finished succesfuly')
                        elif os.path.exists(savedtarget3) is False:
                            print(f'Path {savedtarget3.upper()} does not exist!')
            
                print('--------------------------------------------------------------------------------\nSorting finished succefully!\n--------------------------------------------------------------------------------')
        
    def autoSort(self):
        
        self.thread = Thread(target=self.checkingForFiles)
        
        self.sortingVar += 1
        if self.sortingVar % 2 != 0:
            self.autoSorting['text'] = "ON "
            self.autoSorting.configure(bg='#00ff00')
            self.sortButton['state'] = 'disabled'
            self.sortButton['text'] = ' ... '
            print('--------------------------------------------------------------------------------\nAutosorting ON\n--------------------------------------------------------------------------------')
            self.thread.start()
        elif self.sortingVar % 2 == 0:
            self.autoSorting['text'] = "OFF"
            self.autoSorting.configure(bg='#ff0000')
            self.sortButton['state'] = 'normal'
            self.sortButton['text'] = 'SORT!'
            self.temp += 2000000

    def setPaths(self):
        self.mainWin.destroy()
        os.system('python.exe paths.py')
    
    def setOther(self):
        self.mainWin.destroy()
        os.system('python.exe other.py')
        
    def checkingForFiles(self):
        self.temp = 0
        while self.temp<1000000:
            if len(os.listdir(savedSource)) == 0:
                time.sleep(2)
                print('Looking for some files...')
                self.temp += 1
            elif len(os.listdir(savedSource)) > 0:
                self.sortItems()
                time.sleep(2)
                self.temp += 1
        else:
            self.autoSorting['text'] = "OFF"
            self.autoSorting.configure(bg='#ff0000')
            self.sortButton['state'] = 'normal'
            self.sortButton['text'] = 'SORT!'
            print('--------------------------------------------------------------------------------\nAutosorting OFF\n--------------------------------------------------------------------------------')
        
Main()