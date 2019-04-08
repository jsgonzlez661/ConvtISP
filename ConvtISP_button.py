#!/usr/bin/python3
# -*- coding: utf-8 -*-
from tkinter import filedialog
from PIL import Image, ImageOps
from tkinter import messagebox
from platform import system
from webbrowser import open
from os.path import dirname, abspath

img = "" 
word = {
            "defaultextension": ".jpeg",
            "title": "Save Image",
            "filetypes": [("Jpeg file", "*.jpeg"), 
                        ("Jpg file", "*.jpg"),
                        ("Png file", "*.png"), 
                        ("Tiff file", "*.tiff")]
        }

direct = ""

def save_file():
    global word 
    global direct
    direct = filedialog.asksaveasfilename(**word)
    return direct

def open_img(et):
    global img
    img = filedialog.askopenfilename(title="Select Image", filetypes=(("Jpeg file", "*.jpeg"),("Jpg file", "*.jpg"),("Png file", "*.png"),("Tiff file", "*.tiff")))
    if(img!=None and img!=""):
        if(system()=="Windows"):
            img = img.replace("/","\\")
        et.insert(0, img)
    else: 
        messagebox.showwarning("Select Image","Image was not selected\nPlease select an image")




def convert_img(tipe):
    global img 
    if(img!=None and img!=""):
        try:
            image = Image.open(img)
            sfile=""             
            if(tipe.get()==0):
                image_change = ImageOps.grayscale(image)          
            else:
                image_change = image.convert('1', dither=Image.NONE)
            sfile=save_file()
            if(sfile!=None and sfile!=""):
                image_change.save(sfile, dpi=(300,300))
                messagebox.showinfo("Saved Image", "Converted Image\nThank you for using the program")
            else:
                messagebox.showwarning("Save Image","Image was not save\nPlease save image")
        except AttributeError:
            pass   

def about_info():
    messagebox.showinfo("About ConvtISP", "License: Free Software\nVersion: 0.0.1\nDate: 30/03/2019\nPython: 3.6.5\nTkinter: 8.6.6\nPillow: 5.2.0")


def open_doc():
    if(system()=="Windows"):
        open("documentation.html", new=0 , autoraise=True)
    else: 
        open(dirname(abspath(__file__))+'/documentation.html', new=0 , autoraise=True)