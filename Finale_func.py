#**********************************************************************************
# Python:   3.8.1
#
# Author:   Isaiah D. Johnson
#
# Date:     3/3/20
#
# Purpose:  The Tech Acadamy - Python course, creating a module that holds all
#           my functions for a program that gets text files from one directory
#           and moves it to another and records some things along the way
#*********************************************************************************

#My Imports
import os       # Getting the OS module
import time     # Getting the time module for later formating
import shutil   # Needed to move files from one directory to another
import sqlite3  # Records to a database

#Self made modules
import Finale_gui   #This module provides the GUI for the user
import Finale_main  #Starting module
Gui = Finale_gui    #Renaming for later convienence


# This function gets the required info from the
# getTxt and getTime functions to print out what
# text files are in my directory and when they were
# last modified, also launches the DataBase functions
def start(self):
    i = 0
    txt_list = getTxt(self)
    time_list = getTime(self)
    a = len(txt_list)
    print("\nThere are {} text files in this directory".format(a))
    while i < a:
        b = i + 1
        txt = txt_list[i]
        tm = time_list[i]
        print("\nFile #{} is: \n{} last modified at {}".format(b, txt, tm))
        i += 1
    DataBase(self)
    dbCreate(self)
    dbTbl(self,txt_list,time_list)

    
# creating a new database if it has not already been created.
# And drops the table out of it if it already exist
def DataBase(self):
    conn = sqlite3.connect('Moved_files.db')
    with conn:
        cur = conn.cursor()
        cur.execute('DROP TABLE IF EXISTS tbl_txtFiles')
        conn.commit()
    conn.close()
    
# Creates a table in the database if none already exist
def dbCreate(self):
    conn = sqlite3.connect('Moved_files.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtFiles( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            txt_File TEXT, last_modified TEXT\
            )")
        print("Creating new table...")
        conn.commit()
    conn.close()

# Provides the values to be stored in the table
def dbTbl(self,txt_list,time_list):
    conn = sqlite3.connect('Moved_files.db')
    for i in range(len(txt_list)):
        txt = txt_list[i]
        time = time_list[i]
        cur = conn.cursor()
        cur.execute("INSERT INTO tbl_txtFiles (txt_File, last_modified) VALUES (?,?)",(txt, time))
        conn.commit()
    conn.close()
        

# This function itterates through the files in
# the directory and puts all .txt files in a list
def getTxt(self):
    dir_List = os.listdir('{}'.format(self.directory.get()))
    i = 0
    txt_list = []
    while i < len(dir_List):
        if '.txt' in dir_List[i]:
            a = dir_List[i]
            txt_list.append(a)
            i += 1
        else:
            i += 1
    return txt_list


# This function is here to get the absolute file
# path of all text files in the directory
def getPath(self):
    i = 0
    abPath = []
    fPath = self.directory.get()
    txt_list = getTxt(self)
    while i < len(txt_list):
        a = txt_list[i]
        b = os.path.join(fPath, a)
        abPath.append(b)
        i += 1
    return abPath

# This function moves all text files from source directory
# to the destination directory
def move(self):
    i = 0
    txt_list = getTxt(self)
    getDest = self.Destination.get()
    Finale_path = []
    abPath = getPath(self)
    while i < len(abPath):
        a = abPath[i]
        b = shutil.move(a,getDest)
        c = txt_list[i]
        d = os.path.join(getDest,c)
        Finale_path.append(d)
        i += 1
    return Finale_path
    


# This function gets the last time the text file
# was modified and converts it into a format the
# user can understand
def getTime(self):
    i = 0
    fPath = move(self)
    time_list = []
    while i < len(fPath):
        a = fPath[i]
        b = os.path.getmtime(a)
        c = time.ctime(b)
        time_list.append(c)
        i += 1
    return time_list


# This function will kill the program when called upon       
def Kill(self):
    self.master.destroy()



# this makes it so the program does not start here
if __name__== "__main__":
    pass
