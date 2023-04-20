import tkinter as tk
from tkinter import messagebox
import os
import time

class Paths:
    def __init__(self):
        self.pathsWin = tk.Tk(className =' Paths Settings')
        self.pathsWin.geometry('470x450')
        
        self.testLabel = tk.Label(self.pathsWin, font=('Consolas', 12), text='Change or add your paths here')
        self.testLabel.pack()
        
        self.pathsDirectoryFrame = tk.Frame(self.pathsWin, highlightbackground="#a1a1a1", highlightthickness=2)
        self.pathsDirectoryFrame.columnconfigure(0, weight=1)
        self.pathsDirectoryFrame.columnconfigure(1, weight=1)
        
        self.sortingEntryVar = tk.StringVar()
        self.sortingDirectoryLabel = tk.Label(self.pathsDirectoryFrame, text='From there your files will be sorted')
        self.sortingDirectoryLabel.grid(row=0, column=0, pady=10)
        self.sortingDirectory = tk.Entry(self.pathsDirectoryFrame, text='elo', width=25, textvariable=self.sortingEntryVar)
        self.sortingDirectory.insert(tk.END, r'C:\Users\Kacper\Desktop')
        self.sortingDirectory.grid(row=0, column=1, pady=10)
        self.sortingDirectoryButton = tk.Button(self.pathsDirectoryFrame, text='Save', width=10, activebackground = "cyan", command=self.saveDirectory)
        self.sortingDirectoryButton.grid(row=0, column=2, pady=10, padx=3)
        
        self.pathsDirectoryFrame.pack()
        
        self.addPathsInfo = tk.Label(self.pathsWin, text='Below you can find fields where you can enter\nthe paths for your files to be seved to')
        self.addPathsInfo.pack()
                
        self.addButton = tk.Button(self.pathsWin, text='Add more paths', command=self.addPath)
        self.addButton.pack(pady=10)
        
        self.pathsFrame = tk.Frame(self.pathsWin, highlightbackground="#a1a1a1", highlightthickness=2)
        self.pathsFrame.columnconfigure(0, weight=1)
        self.pathsFrame.columnconfigure(1, weight=1)
        
        self.addEntryVar = tk.StringVar()
        self.addPathsVar = 5
        for i in range(0, self.addPathsVar):
            self.pathNumber = tk.Label(self.pathsFrame, text=str(i+1)+".")
            self.pathNumber.grid(row=i, column=0, pady=10)
            self.pathsEntry = tk.Entry(self.pathsFrame, width=50, text=self.addEntryVar)
            self.pathsEntry.grid(row=i, column=1, pady=10, padx=20)
            self.pathsEntryButton = tk.Button(self.pathsFrame, width=10, text='Save', activebackground = "cyan", command=self.savePaths)
            self.pathsEntryButton.grid(row=i, column=2, pady=10, padx=5)
        
        self.pathsFrame.pack()
        
        self.exitButton = tk.Button(self.pathsWin, text='EXIT', font=('Consolas', 14), command=self.close)
        self.exitButton.pack(pady=10)
        
        self.pathsWin.mainloop()
        
    def close(self):
        if messagebox.askyesno(title='Quit?', message='Are you sure you want to quit?'):
            self.pathsWin.destroy()
            
    def addPath(self):
        self.addPathsVar += 1
        print(self.addPathsVar)
        self.pathsWin.mainloop()
    
    def savePaths(self):
        print(self.addEntryVar.get())
        
    def saveDirectory(self):
        print(self.sortingEntryVar.get())
        path = str(self.sortingEntryVar.get())
        os.mkdir(f'{path}/elo.txt')