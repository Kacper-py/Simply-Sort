import tkinter as tk
from tkinter import messagebox
import os
import time

class Other:
    def __init__(self):
        self.pathsWin = tk.Tk(className =' Other Settings')
        self.pathsWin.geometry('800x500')
        
        self.testLabel = tk.Label(self.pathsWin, font=('Consolas', 12), text='In the future you will be able to change other aspects of this program')
        self.testLabel.pack()
        
        self.exitButton = tk.Button(self.pathsWin, text='EXIT', font=('Consolas', 14), command=self.close)
        self.exitButton.place(x=700, y=425)
        
        self.pathsWin.mainloop()
        
    def close(self):
        if messagebox.askyesno(title='Quit?', message='Are you sure you have set everything how you want it to be?'):
            self.pathsWin.destroy()