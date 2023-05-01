import tkinter as tk
from tkinter import messagebox
import os
import time
from configparser import ConfigParser

# zaczytywanie pliku konfikuracyjnego
config = ConfigParser()
config.read('config.ini')
savedSource = config.get('paths', 'source')
savedtarget = config.get('paths', 'target')
savedtarget1 = config.get('paths', 'target1')
savedtarget2 = config.get('paths', 'target2')
savedtarget3 = config.get('paths', 'target3')

class Paths:
    def __init__(self):
        
        self.pathsWin = tk.Tk(className =' Paths Settings')
        self.pathsWin.geometry('470x390')
        
        self.testLabel = tk.Label(self.pathsWin, font=('Consolas', 12), text='Change or add your paths here')
        self.testLabel.pack(pady=10)
        
        self.pathsDirectoryFrame = tk.Frame(self.pathsWin, highlightbackground="#a1a1a1", highlightthickness=2)
        self.pathsDirectoryFrame.columnconfigure(0, weight=1)
        self.pathsDirectoryFrame.columnconfigure(1, weight=1)
        
        self.sortingEntryVar = tk.StringVar()
        self.sortingDirectoryLabel = tk.Label(self.pathsDirectoryFrame, text='From there your files will be sorted')
        self.sortingDirectoryLabel.grid(row=0, column=0, pady=10)
        self.sortingDirectory = tk.Entry(self.pathsDirectoryFrame, width=25, textvariable=self.sortingEntryVar)
        self.sortingDirectory.insert(tk.END, savedSource)
        self.sortingDirectory.grid(row=0, column=1, pady=10)
        self.sortingDirectoryButton = tk.Button(self.pathsDirectoryFrame, text='Save', width=10, activebackground = "cyan", command=self.saveDirectory)
        self.sortingDirectoryButton.grid(row=0, column=2, pady=10, padx=3)
        
        self.pathsDirectoryFrame.pack()
        
        self.addPathsInfo = tk.Label(self.pathsWin, text='Below you can find fields where you can enter\nthe paths for your files to be saved to')
        self.addPathsInfo.pack(pady=10)

        self.pathsFrame = tk.Frame(self.pathsWin, highlightbackground="#a1a1a1", highlightthickness=2)
        self.pathsFrame.columnconfigure(0, weight=1)
        self.pathsFrame.columnconfigure(1, weight=1)
        
        self.addEntryVar = tk.StringVar()
        self.addEntryVar1 = tk.StringVar()
        self.addEntryVar2 = tk.StringVar()
        self.addEntryVar3 = tk.StringVar()
        
        self.addPathsVar = 5

        # Path 1
        self.pathNumber = tk.Label(self.pathsFrame, text='1.')
        self.pathNumber.grid(row=0, column=0, pady=10)
        self.pathsEntry = tk.Entry(self.pathsFrame, width=60, text=self.addEntryVar)
        self.pathsEntry.insert(tk.END, savedtarget)
        self.pathsEntry.grid(row=0, column=1, pady=10, padx=20)
        
        # Path 2
        self.pathNumber1 = tk.Label(self.pathsFrame, text='2.')
        self.pathNumber1.grid(row=1, column=0, pady=10)
        self.pathsEntry1 = tk.Entry(self.pathsFrame, width=60, text=self.addEntryVar1)
        self.pathsEntry1.insert(tk.END, savedtarget1)
        self.pathsEntry1.grid(row=1, column=1, pady=10, padx=20)
        
        # Path 3
        self.pathNumber2 = tk.Label(self.pathsFrame, text='3.')
        self.pathNumber2.grid(row=2, column=0, pady=10)
        self.pathsEntry2 = tk.Entry(self.pathsFrame, width=60, text=self.addEntryVar2)
        self.pathsEntry2.insert(tk.END, savedtarget2)
        self.pathsEntry2.grid(row=2, column=1, pady=10, padx=20)
        
        # Path 4
        self.pathNumber3 = tk.Label(self.pathsFrame, text='4.')
        self.pathNumber3.grid(row=3, column=0, pady=10)
        self.pathsEntry3 = tk.Entry(self.pathsFrame, width=60, text=self.addEntryVar3)
        self.pathsEntry3.insert(tk.END, savedtarget3)
        self.pathsEntry3.grid(row=3, column=1, pady=10, padx=20)
        
        self.pathsFrame.pack()
        
        self.buttonsFrame = tk.Frame(self.pathsWin)
        
        self.exitButton = tk.Button(self.buttonsFrame, text='EXIT', font=('Consolas', 14), command=self.close)
        self.exitButton.grid(row=0, column=1, pady=10, padx=100)
        
        self.saveButton = tk.Button(self.buttonsFrame, text='SAVE', font=('Consolas', 14), command=self.savePaths)
        self.saveButton.grid(row=0, column=0, pady=10, padx=90)
        
        self.buttonsFrame.pack()
        
        self.pathsWin.mainloop()
        
    def close(self):
        if messagebox.askyesno(title='Quit?', message='Are you sure you want to quit?'):
            self.pathsWin.destroy()
            os.system('python.exe main.py')
            
    def addPath(self):
        self.addPathsVar += 1
        print(self.addPathsVar)
        self.pathsWin.mainloop()
    
    def savePaths(self):
        config = ConfigParser()
        config.read('config.ini')
        config.set('paths', 'target', self.addEntryVar.get())
        config.set('paths', 'target1', self.addEntryVar1.get())
        config.set('paths', 'target2', self.addEntryVar2.get())
        config.set('paths', 'target3', self.addEntryVar3.get())
            
        with open('config.ini', 'w') as configFile:
            config.write(configFile)
        print(f"Paths saved. {self.addEntryVar.get()}")     
        
    def saveDirectory(self):
        config = ConfigParser()
        config.read('config.ini')
        config.set('paths', 'source', self.sortingEntryVar.get())
            
        with open('config.ini', 'w') as configFile:
            config.write(configFile)
        print(f"Target saved. {self.sortingEntryVar.get()}")
        
Paths()