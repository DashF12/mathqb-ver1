import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pickle
from os.path import exists
from os import mkdir,listdir
import time
from PIL import Image,ImageTk
import random
from tkinter import filedialog

def activateADDQN():
    global diffINT, ch, type
    window = ctk.CTk()
    window.geometry("1280x720")
    window.title("MathQBGEN")
    window.iconbitmap('assets/appicon.ico')


    diffINT = ''
    ch = ''
    type = ''
    def inputfile():
        global file_path
        file_path = filedialog.askopenfilename()
        print(file_path)

        return
    Importframe = ctk.CTkFrame(master=window)
    Importframe.pack(padx=12,pady=135)
    importstn = ctk.CTkLabel(master=Importframe,text='Import the Question -> ', font=('Calibri', 15)) 
    importstn.pack(side="left",padx=12)
    importbn = ctk.CTkButton(master=Importframe,command=inputfile, text="Import", font=('Calibri', 15))
    importbn.pack(pady=5)
    


    mainframe = ctk.CTkFrame(master=window)
    mainframe.pack(padx=12)

    typeframe = ctk.CTkFrame(master=mainframe)
    typeframe.pack(side="left",pady=12,padx=12)

    typeStn = ctk.CTkLabel(master=typeframe,text='Type of the Question', font=('Calibri', 15)) 
    typeStn.pack(pady=12,padx=12)


    radio_varTYPE = ctk.StringVar(value="other")

    def radiobutton_eventtype():
        global type
        type = radio_varTYPE.get()

    Type2M = ctk.CTkRadioButton(master=typeframe, text="2 Marks",
                                             command=radiobutton_eventtype, variable= radio_varTYPE, value=2)
    Type3M = ctk.CTkRadioButton(master=typeframe, text="3 Marks",
                                             command=radiobutton_eventtype, variable= radio_varTYPE, value=3)
    Type5M = ctk.CTkRadioButton(master=typeframe, text="5 Marks",
                                             command=radiobutton_eventtype, variable= radio_varTYPE, value=5)
    
    Type2M.pack(padx=20, pady=10)
    Type3M.pack(padx=20, pady=10)
    Type5M.pack(padx=20, pady=10)

    diffframe = ctk.CTkFrame(master=mainframe)
    diffframe.pack(side="left",padx=12,pady=30)

    diffStn = ctk.CTkLabel(master=diffframe,text='Difficulty of the Question', font=('Calibri', 15)) 
    diffStn.pack(pady=12,padx=12)

    radio_vardiff = ctk.StringVar(value="other")

    def radiobutton_eventdiff():
        global diffINT
        diffINT = radio_vardiff.get()

    easy = ctk.CTkRadioButton(master=diffframe, text="Easy",
                                             command=radiobutton_eventdiff, variable= radio_vardiff, value="Easy")
    moderate = ctk.CTkRadioButton(master=diffframe, text="Moderate",
                                             command=radiobutton_eventdiff, variable= radio_vardiff, value="Moderate")
    hard = ctk.CTkRadioButton(master=diffframe, text="Hard",
                                             command=radiobutton_eventdiff, variable= radio_vardiff, value="Hard")

    easy.pack(padx=20, pady=10)
    moderate.pack(padx=20, pady=10)
    hard.pack(padx=20, pady=10)

    chptframe = ctk.CTkFrame(master=mainframe)
    chptframe.pack(padx=12,pady=30)

    chStn = ctk.CTkLabel(master=chptframe,text='Select the Chapter', font=('Calibri', 15)) 
    chStn.pack(pady=12,padx=12)

    def optionmenu_callback(choice):
        global ch,dataINT,contentdata
        ch = choice
        dataINT = {'File':file_path}
        contentdata = {'Type': type,'Difficulty': diffINT, 'Chapter': ch}
        print(dataINT)

    combobox = ctk.CTkOptionMenu(master=chptframe,
                                       values=["Choose","Chapter 1", "Chapter 2","Chapter 3", "Chapter 4","Chapter 5", "Chapter 6","Chapter 7", "Chapter 8","Chapter 9", "Chapter 10","Chapter 11", "Chapter 12","Chapter 13", "Chapter 14",],
                                       command=optionmenu_callback)
    combobox.pack(padx=20, pady=10)
    combobox.set("Choose") 


    window.mainloop()

    return dataINT
