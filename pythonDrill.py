#**********************************************************************************
# Python:   3.8.1
#
# Author:   Isaiah D. Johnson
#
# Date:     2/10/20
#
# Purpose:  The Tech Acadamy - Python course, Creating first Drill program.
#           Demonstrating how use the OS module to get and use
#           data from a specific directory
#**********************************************************************************

import os   # Getting the OS module
import time # Getting the time module for later formating


# This function gets the required info from the
# getTxt and getTime functions to print out what
# text files are in my directory and when they were
# last modified
def start():
    i = 0
    txt_list = getTxt()
    time_list = getTime()
    a = len(txt_list)
    print("\nThere are {} text files in this directory".format(a))
    while i < a:
        b = i + 1
        txt = txt_list[i]
        tm = time_list[i]
        print("\nFile #{} is: \n{} last modified at {}".format(b, txt, tm))
        i += 1


# This function itterates through the files in
# the directory and puts all .txt files in a list
def getTxt():
    dir_List = os.listdir('C:\\Users\\Student\\Desktop\\GitHub\\The-Tech-Academy-Basic-Python-Projects\\Random_files')
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
def getPath():
    i = 0
    abPath = []
    fPath = 'C:\\Users\\Student\\Desktop\\GitHub\\The-Tech-Academy-Basic-Python-Projects\\Random_files\\'
    txt_list = getTxt()
    while i < len(txt_list):
        a = txt_list[i]
        b = os.path.join(fPath, a)
        abPath.append(b)
        i += 1
    return abPath


# This function gets the last time the text file
# was modified and converts it into a format the
# user can understand
def getTime():
    i = 0
    abPath = getPath()
    time_list = []
    while i < len(abPath):
        a = abPath[i]
        b = os.path.getmtime(a)
        c = time.ctime(b)
        time_list.append(c)
        i += 1
    return time_list
    




# When this program runs it will launch the start function
if __name__== "__main__":
    start()
