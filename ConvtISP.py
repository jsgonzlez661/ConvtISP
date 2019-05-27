#!/usr/bin/python3
# -*- coding: utf-8 -*-
from tkinter import Tk, Frame, Button, Label, Menu, LabelFrame, Entry, PhotoImage, IntVar
from tkinter import ttk
from platform import system
from ConvtISP_button import open_img, convert_img, about_info, open_doc
from os.path import dirname, abspath

class myFrame(Frame):

    def __init__(self, root):
        self.myFra = Frame.__init__(self, root)
        #--------------- System Option ---------------
        if(system()=="Windows"):
            root.geometry("232x240")
            root.iconbitmap("icons/ConvtISP.ico")
            #--------------- Elements img ---------------
            self.Img = PhotoImage(file="icons/select.png")
            self.Img_cont = PhotoImage(file="icons/convert.png")
            self.Img_exit = PhotoImage(file="icons/exit.png")
            self.Img_doc = PhotoImage(file="icons/doc.png")
            self.Img_about = PhotoImage(file="icons/about.png")
            #--------------- Elements img END ---------------
        else: # For Linux
            root.geometry("290x220")
            #--------------- Elements img ---------------
            self.Img = PhotoImage(file=dirname(abspath(__file__))+'/icons/select.png')
            self.Img_cont = PhotoImage(file=dirname(abspath(__file__))+'/icons/convert.png')
            self.Img_exit = PhotoImage(file=dirname(abspath(__file__))+'/icons/exit.png')
            self.Img_doc = PhotoImage(file=dirname(abspath(__file__))+'/icons/doc.png')
            self.Img_about = PhotoImage(file=dirname(abspath(__file__))+'/icons/about.png')
            #--------------- Elements img END ---------------
        #--------------- System Option END  ---------------    

        #--------------- Variable ---------------
        self.tipe = IntVar()

        #--------------- Style ttk ---------------
        self.style = ttk.Style()
        self.style.configure('TRadiobutton', font=("Arial",10))
        self.style.configure('TButton', font=("Arial",12, "bold"))

        #--------------- Elements Menu ---------------
        self.menu = Menu(root)
        root.config(menu=self.menu)
        self.Archive  = Menu(self.menu, tearoff=0)
        self.Archive.add_command(label="Open Image", image=self.Img, compound="left", command=lambda:open_img(self.Et))
        self.Archive.add_command(label="Convert", image=self.Img_cont, compound="left", command=lambda:convert_img(self.tipe))
        self.Archive.add_separator()
        self.Archive.add_command(label="Exit", image=self.Img_exit, compound="left", command=lambda:root.destroy())
        self.menu.add_cascade(label="Archive", menu=self.Archive)       
        self.Help = Menu(self.menu, tearoff=0)
        self.Help.add_command(label="Documentation", image=self.Img_doc, compound="left", command=lambda:open_doc())
        self.Help.add_separator()
        self.Help.add_command(label="About", image=self.Img_about, compound="left", command=lambda:about_info())
        self.menu.add_cascade(label="Help", menu=self.Help)
        #--------------- Elements Menu END ---------------

        #--------------- Elements Option Archive  ---------------

        #----- Elements 1 ----- 
        self.LFrame = LabelFrame(self.myFra, text="File Options", font=("Arial",10))
        self.LFrame.grid(row=0, column=0, padx=10)
        self.Et = ttk.Entry(self.LFrame, width=30)
        self.Et.grid(row=0, column=0, padx=10, pady=5)
        self.Et.configure(state='readonly')   
        self.bt1 = ttk.Button(self.LFrame, image=self.Img, text="Select Image", compound="left", command=lambda:open_img(self.Et))
        self.bt1.grid(row=1, column=0)     
        self.bt2 = ttk.Button(self.LFrame, text="Convert", image=self.Img_cont, compound="left", command=lambda:convert_img(self.tipe))
        self.bt2.grid(row=2, column=0, pady=4)
        #----- Elements 1 END ----- 

        #----- Elements 2  ----- 
        self.LFrame2 = LabelFrame(self.myFra, text="Conversion Options", font=("Arial",10))
        self.LFrame2.grid(row=1, column=0, padx=10, pady=5)
        self.Rb1 = ttk.Radiobutton(self.LFrame2, text="Grayscale / 300dpi", value=0, variable=self.tipe)
        self.Rb1.grid(row=0, column=0, sticky="w", padx=20, pady=5)
        self.Rb2 = ttk.Radiobutton(self.LFrame2, text="Black and White / 300dpi", value=1, variable=self.tipe)
        self.Rb2.grid(row=1, column=0, sticky="w", padx=20, pady=4)     
        #----- Elements 2 END ----- 

        #--------------- Elements Option Archive END  ---------------

if __name__ == "__main__":     
	root = Tk()
	root.title("ConvtISP")
	root.resizable(0,0)
	frame = myFrame(root)
	frame.grid(row=0, column=0)
	root.mainloop()