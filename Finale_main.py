#**********************************************************************************
# Python:   3.8.1
#
# Author:   Isaiah D. Johnson
#
# Date:     3/3/20
#
# Purpose:  The Tech Acadamy - Python course, Creating a program that
#           grabs moves and records text files in a directory
#*********************************************************************************

#My Imports
from tkinter import *           # Importing this module to provide gui functionality
import tkinter as tk            
from tkinter import filedialog  # This allows the user to get a file path

#Self made modules
import Finale_gui
import Finale_func

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(1200,400))
        self.master.title('Move text files')
        # Calling my gui to run
        Finale_gui.load_gui(self)

    #These are button functions that access a directory
    def Browse(self):
        root.direct= filedialog.askdirectory()
        direct=root.direct
        self.directory.set("{}".format(direct))

    def getDest(self):
        root.direct= filedialog.askdirectory()
        Dir=root.direct
        self.Destination.set("{}".format(Dir))




if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
