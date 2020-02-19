from tkinter import *
import tkinter as tk
from tkinter import filedialog

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.directory= StringVar()
        
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(975,200))
        self.master.title('Get File Path')

        self.txtBox = Entry(self.master, width=60, textvariable=self.directory, font=("Helvetica", 16), fg='black')
        self.txtBox.grid(row=0, column=1,columnspan=2, padx=(40,0), pady=(60,0))

        self.btn_Browse = tk.Button(self.master,width=20,height=2,text='Browse...', command=self.Browse)
        self.btn_Browse.grid(row=0,column=0,padx=(25,0),pady=(65,0),sticky=W)


    def Browse(self):
        root.direct= filedialog.askdirectory()
        direct=root.direct
        self.directory.set("{}".format(direct))
  
        
        



if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
