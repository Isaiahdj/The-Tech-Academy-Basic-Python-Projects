#**********************************************************************************
# Python:   3.8.1
#
# Author:   Isaiah D. Johnson
#
# Date:     3/3/20
#
# Purpose:  The Tech Acadamy - Python course, creating a graphic user interface
#           that allows the user to pick a directory and get text files from that
#           directory and move them to another chosen directory all with the push
#           of a couple of buttons
#*********************************************************************************

#My Imports
from tkinter import *           #imported to ad gui functionality
import tkinter as tk
from tkinter import filedialog  #allows user to access there directories

#Self made modules
import Finale_func #This module has all my functions in it
import Finale_main #This module is used to run the program hin the name main
Func = Finale_func #Renaming to make it easier to call later on

#This function gets called by Finale_main at the start of the program
#to add a gui for the user to well use
def load_gui(self):
    
    #making string variables with tkinter
    self.directory= StringVar()
    self.Destination= StringVar()
    
    #Size and alignment of first textbox also passing in the string variable here
    self.txtBox = Entry(self.master, width=80, textvariable=self.directory, font=("Helvetica", 16), fg='black')
    self.txtBox.grid(row=0, column=1,columnspan=2, padx=(40,0), pady=(60,0))
    
    #Size and alignment of first button. This button will allow the user to access
    #their directories and let them pick a source directory
    self.btn_Browse = tk.Button(self.master,width=20,height=2,text='Source File', command=self.Browse)
    self.btn_Browse.grid(row=0,column=0,padx=(25,0),pady=(65,0),sticky=W)
    
    #Size and alignment of second textbox also passing in another string variable
    self.txtBox = Entry(self.master, width=80, textvariable=self.Destination, font=("Helvetica", 16), fg='black')
    self.txtBox.grid(row=1, column=1,columnspan=2, padx=(40,0), pady=(60,0))
    
    #Size and alignment of second button which will provide the user an opertunity to
    #to pick a destination folder where some files will be moved to
    self.btn_Browse = tk.Button(self.master,width=20,height=2,text='Destination...', command=self.getDest)
    self.btn_Browse.grid(row=1,column=0,padx=(25,0),pady=(65,0),sticky=W)
    
    #Size and alignment of third button which will iterate through source directory and
    #get text files and move them to the destination directory
    self.btn_Browse = tk.Button(self.master,width=20,height=2,text='Get txt files...', command= lambda: Func.start(self))
    self.btn_Browse.grid(row=2,column=0,padx=(25,0),pady=(65,0),sticky=W)
    
    #Size and alignment of the fourth and finale button which kills the program and
    #closses the GUI
    self.btn_Browse = tk.Button(self.master,width=20,height=2,text='Close!!!', command= lambda: Func.Kill(self))
    self.btn_Browse.grid(row=2,column=2,padx=(25,0),pady=(65,0),sticky=E)
        



#This makes it so the program does not start here
if __name__== "__main__":
    pass
