#**********************************************************************************
# Python:   3.8.1
#
# Author:   Isaiah D. Johnson
#
# Date:     2/13/20
#
# Purpose:  The Tech Acadamy - Python course, creating a database.
#           Demonstrating how how to create a database and how to
#           retreive data stored within it and print it out to the screen
#*******************************************************************************

import sqlite3  #importing this module to be able to write to databases


def Start():
    conn = sqlite3.connect('txt.db')
    with conn:
        cur = conn.cursor()
        cur.execute('DROP TABLE tbl_txtFiles')
        print("\nDropping Table...")
        conn.commit()
    conn.close()
    dbCreate()
    

def dbCreate():
    conn = sqlite3.connect('txt.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtFiles( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            txt_File TEXT \
            )")
        conn.commit()
    conn.close()
    dbTbl()


def createList():
    fileList = ('information.docx','Hello.txt','myImage.png', \
                'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
    i = 0
    txtList = []
    while i < len(fileList):
        if ".txt" in fileList[i]:
            a = fileList[i]
            txtList.append(a)
            i += 1
        else:
            i += 1
    return txtList



def dbTbl():
    conn = sqlite3.connect('txt.db')
    txtList = createList()
    i = 0
    with conn:
        for item in txtList:
            quary = """INSERT INTO tbl_txtFiles(txt_File) VALUES(?)"""
            cur = conn.cursor()
            cur.execute(quary, [item])
            conn.commit()
            i += 1
    conn.close()
    dbSelect()

def dbSelect():
    conn = sqlite3.connect('txt.db')
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT txt_File FROM tbl_txtFiles")
        varTbl = cur.fetchall()
        a = len(varTbl)
        i = 0
    conn.close()
    print(a)
    print("\n\nThere are {} text files in this DataBase".format(a))
    while i < a:
        for item in varTbl:
            b = i + 1
            tbl = varTbl[i]
            print("\nFile #{} is: \n{}".format(b, item))
            i += 1
            for item in varTbl:
                b = i + 1
                tbl = varTbl[i]
                print("\nFile #{} is: \n{}".format(b, item))


    




if __name__== "__main__":
    Start()
