import tkinter as tk
from tkinter import messagebox
from configparser import ConfigParser
import os

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

class Other:
    def __init__(self):
        self.schemasWin = tk.Tk(className =' Schemas Settings')
        self.schemasWin.geometry('480x410')
        
        self.title = tk.Label(self.schemasWin, font=('Consolas', 14), text='You can change your schemas here')
        self.title.pack()
        
        self.testLabel = tk.Label(self.schemasWin, font=('Consolas', 10), text='Schemas are the endings of names of your files.\nFor examlpe your files name is "file-test1",\nthe "test1" part is the schema. Every schema is assigned\nto the path you set up in the Paths settings.\nBased on the schemas program will know where to move your file.')
        self.testLabel.pack()
        
        self.schemasGrid = tk.Frame(self.schemasWin)
        
        self.schemasEntryVar = tk.StringVar()
        self.schemasEntryVar1 = tk.StringVar()
        self.schemasEntryVar2 = tk.StringVar()
        self.schemasEntryVar3 = tk.StringVar()
        
        # schema 1
        self.schemaPath = tk.Label(self.schemasGrid, text=f'Path: {savedtarget}')
        self.schemaPath.grid(row=0, column=1)
        self.schemaNumber = tk.Label(self.schemasGrid, text='1.')
        self.schemaNumber.grid(row=1, column=0)
        self.schemaEntry = tk.Entry(self.schemasGrid, width=40, textvariable=self.schemasEntryVar)
        self.schemaEntry.grid(row=1, column=1, pady=5)
        self.schemaEntry.insert(tk.END, savedSchema)
        
        #schema 2
        self.schemaPath = tk.Label(self.schemasGrid, text=f'Path: {savedtarget1}')
        self.schemaPath.grid(row=2, column=1)
        self.schemaNumber1 = tk.Label(self.schemasGrid, text='2.')
        self.schemaNumber1.grid(row=3, column=0)
        self.schemaEntry1 = tk.Entry(self.schemasGrid, width=40, textvariable=self.schemasEntryVar1)
        self.schemaEntry1.grid(row=3, column=1, pady=5)
        self.schemaEntry1.insert(tk.END, savedSchema1)
        
        #schema 3
        self.schemaPath = tk.Label(self.schemasGrid, text=f'Path: {savedtarget2}')
        self.schemaPath.grid(row=4, column=1)
        self.schemaNumber2 = tk.Label(self.schemasGrid, text='3.')
        self.schemaNumber2.grid(row=5, column=0)
        self.schemaEntry2 = tk.Entry(self.schemasGrid, width=40, textvariable=self.schemasEntryVar2)
        self.schemaEntry2.grid(row=5, column=1, pady=5)
        self.schemaEntry2.insert(tk.END, savedSchema2)
        
        #schema 4
        self.schemaPath = tk.Label(self.schemasGrid, text=f'Path: {savedtarget3}')
        self.schemaPath.grid(row=6, column=1)
        self.schemaNumber3 = tk.Label(self.schemasGrid, text='4.')
        self.schemaNumber3.grid(row=7, column=0)
        self.schemaEntry3 = tk.Entry(self.schemasGrid, width=40, textvariable=self.schemasEntryVar3)
        self.schemaEntry3.grid(row=7, column=1, pady=5)
        self.schemaEntry3.insert(tk.END, savedSchema3)
        
        self.schemasGrid.pack(pady=20)
        
        # self.exitButton = tk.Button(self.schemasWin, text='EXIT', font=('Consolas', 14), command=self.close)
        # self.exitButton.pack()
        
        self.buttonsFrame = tk.Frame(self.schemasWin)
        
        self.exitButton = tk.Button(self.buttonsFrame, text='EXIT', font=('Consolas', 14), command=self.close)
        self.exitButton.grid(row=0, column=1, pady=10, padx=100)
        
        self.saveButton = tk.Button(self.buttonsFrame, text='SAVE', font=('Consolas', 14), command=self.saveSchemas)
        self.saveButton.grid(row=0, column=0, pady=10, padx=90)
        
        self.buttonsFrame.pack()
        
        self.schemasWin.mainloop()
        
    def close(self):
        if messagebox.askyesno(title='Quit?', message='Are you sure you have set everything how you want it to be?'):
            self.schemasWin.destroy()
            os.system('python.exe main.py')
            
    def saveSchemas(self):
        config = ConfigParser()
        config.read('config.ini')
        config.set('schemas', 'schema', self.schemasEntryVar.get())
        config.set('schemas', 'schema1', self.schemasEntryVar1.get())
        config.set('schemas', 'schema2', self.schemasEntryVar2.get())
        config.set('schemas', 'schema3', self.schemasEntryVar3.get())
            
        with open('config.ini', 'w') as configFile:
            config.write(configFile)
        print(f"Schemas saved. {self.schemasEntryVar.get()}")
            
Other()