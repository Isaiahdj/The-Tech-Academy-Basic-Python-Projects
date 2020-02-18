from tkinter import *
import tkinter as tk

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(725,275))
        self.master.title('Check Files')

        self.txtBox = Entry(self.master, width=40, font=("Helvetica", 16), fg='black', bg='white')
        self.txtBox.grid(row=0, column=1,columnspan=2, padx=(40,0), pady=(60,0))

        self.txtBox2 = Entry(self.master,width=40, font=("Helvetica", 16), fg='black', bg='white')
        self.txtBox2.grid(row=1, column=1,columnspan=2, padx=(40,0), pady=(15,0))
        
        self.btn_Browse = tk.Button(self.master,width=20,height=2,text='Browse...')
        self.btn_Browse.grid(row=0,column=0,padx=(25,0),pady=(65,0),sticky=W)

        self.btn_Browse2 = tk.Button(self.master,width=20,height=2,text='Browse...')
        self.btn_Browse2.grid(row=1,column=0,padx=(25,0),pady=(25,0),sticky=W)

        self.btn_Check = tk.Button(self.master,width=20,height=3,text='Check for files...')
        self.btn_Check.grid(row=2,column=0,padx=(25,0),pady=(20,10),sticky=W)

        self.btn_Close = Button(self.master, text='Close Program', width=20, height=3, command=self.Close)
        self.btn_Close.grid(row=2, column=2, padx=(0,0), pady=(20,10), sticky=E)

    def Close(self):
        self.master.destroy()


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
