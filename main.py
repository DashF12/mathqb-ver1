# Import all the necessary packages and modules

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
from addqn import activateADDQN
import shutil
from tkinter import filedialog
# Declare the tkinter window and Define it.

window = ctk.CTk()
window.geometry("1280x720")
window.title("MathQBGEN")
window.iconbitmap('assets/appicon.ico')


def Catalogue(username):
    
    listofDir = listdir(f"Accounts/{username}")
    listofDir.remove(f'{username}')
    listofDir.remove('Catalogue')
    with open(f"Accounts/{username}/Catalogue","wb") as Cataloguefilew:
        CataDict = {}
        for i in listofDir:
            CataDict[i] = "Chapter" + i

        pickle.dump(CataDict,Cataloguefilew)

    with open(f"Accounts/{username}/Catalogue","rb") as Cataloguefiler:
        data = pickle.load(Cataloguefiler)
    
    return data


def AccountPage():
    global dataINT



    def HomePage():
        global ACCOUNTSTAB,SOFTWAREINFOTAB,QUESTIONSTAB,WEBSCRAPTAB
    

        frame.destroy()
        suframe.destroy()
        try:
            sucess_frame.destroy()
        except NameError as e:
            print(e)

        
        def change_appearance_mode_event( new_appearance_mode: str):
            ctk.set_appearance_mode(new_appearance_mode)

        #TAB FRAME AS ALL THE 4 TABS, ITS A CHILD FRAME
        Tab_frame = ctk.CTkFrame(master=window,corner_radius=0)
        Tab_frame.pack(side=tk.LEFT,anchor="w", expand = False, fill = "y", ipadx=34)
        Tab_frame.columnconfigure(0,weight=1)
        Tab_frame.rowconfigure((0,1,2,3,4,5,6),weight=1)

        QtabIMG = Image.open("assets/safe.png").resize((32,32))
        QtabIMG_tk = ImageTk.PhotoImage(QtabIMG)

        WebScrapTabIMG = Image.open("assets/web.png").resize((32,32))
        WebScrapTabIMG_tk = ImageTk.PhotoImage(WebScrapTabIMG)

        SoftwareTabIMG = Image.open("assets/software.png").resize((32,32))
        SoftwareTabIMG_tk = ImageTk.PhotoImage(SoftwareTabIMG)

        AccountTabIMG = Image.open("assets/user.png").resize((32,32))
        AccountTabIMG_tk = ImageTk.PhotoImage(AccountTabIMG)


        logo = ctk.CTkLabel(master=Tab_frame, text="MathsQBGEN", font=ctk.CTkFont(size=20, weight="bold"))
        logo.grid(row=0, column=0)

        QUESTIONSTAB = ctk.CTkButton(master=Tab_frame, text="Question Bank", font=ctk.CTkFont(family="Clash Grotesk",size=18, weight="bold"), image=QtabIMG_tk, compound="left")
        QUESTIONSTAB.grid(row=1,column=0)

        WEBSCRAPTAB = ctk.CTkButton(master=Tab_frame, text="Web Scrapping", font=ctk.CTkFont(family="Clash Grotesk",size=18, weight="bold"), image=WebScrapTabIMG_tk, compound="left")
        WEBSCRAPTAB.grid(row=2,column=0)

        SOFTWAREINFOTAB = ctk.CTkButton(master=Tab_frame, text="Software Info", font=ctk.CTkFont(family="Clash Grotesk",size=18, weight="bold"), image=SoftwareTabIMG_tk, compound="left")
        SOFTWAREINFOTAB.grid(row=3,column=0)

        ACCOUNTSTAB = ctk.CTkButton(master=Tab_frame, text="Accounts Tab", font=ctk.CTkFont(family="Clash Grotesk",size=18, weight="bold"), image=AccountTabIMG_tk, compound="left")
        ACCOUNTSTAB.grid(row=4,column=0)


        ThemeMenuFrame = ctk.CTkFrame(Tab_frame, fg_color="transparent")
        ThemeMenuFrame.grid(row=5,column=0, ipady=5,ipadx=5)
        ThemeMenuLabel = ctk.CTkLabel(ThemeMenuFrame, text="Appearance Mode:", anchor="w",font=ctk.CTkFont(family="Clash Grotesk",size=14,weight="bold"))
        ThemeMenuLabel.pack(padx=5,pady=5)
        ThemeMenu = ctk.CTkOptionMenu(ThemeMenuFrame, values=["Dark", "Light", "System"], command=change_appearance_mode_event,font=ctk.CTkFont(family="Clash Grotesk",size=14))
        ThemeMenu.pack(padx=5,pady=5)

        def AccountsTabPAGE():
            global NonTab_FrameA, WebScrapTabPAGE, SoftwareInfoTabPAGE, QuestionsTabPAGE
            

            NonTab_FrameA = ctk.CTkFrame(master=window,corner_radius=0, fg_color="transparent")
            NonTab_FrameA.pack(side=tk.RIGHT,expand = True, fill="both", anchor="e")


            AccountsTab_Frame = ctk.CTkFrame(master=NonTab_FrameA, fg_color="transparent")
            AccountsTab_Frame.place(relx=0.5,rely=0.45,anchor="center")
            AccountsTab_Frame.rowconfigure((0,1,2),weight=1)
            AccountsTab_Frame.rowconfigure(3,weight=1)
            AccountsTab_Frame.columnconfigure(0,weight=1)


            ProfileIMG = Image.open("assets/accounttabuser.png").resize((256,256))
            ProfileIMG_tk = ImageTk.PhotoImage(ProfileIMG)
            LabelFORprofileIMG = ctk.CTkLabel(master=AccountsTab_Frame,image=ProfileIMG_tk,text="")
            LabelFORprofileIMG.grid(row=0,column=0, rowspan=1, sticky="nsew", pady=5)

            Labelforusername = ctk.CTkLabel(master=AccountsTab_Frame, text="Username: {}".format(username.capitalize()),font=ctk.CTkFont(family="Clash Grotesk",size=20, weight="bold"),text_color="lightgreen")
            Labelforusername.grid(row=1,column=0, sticky="nsew",pady=0)

            

            StatinAccTab_Frame = ctk.CTkFrame(master=AccountsTab_Frame, fg_color="transparent")
            StatinAccTab_Frame.grid(row=2,column=0, ipadx=25,ipady=25)
            StatinAccTab_Frame.rowconfigure((0,1,2,3),weight=1)
            StatinAccTab_Frame.columnconfigure((0,1,2),weight=1)

            NoOfQuestions = listdir(f"Accounts/{username}")
            NoOfQuestions = len(NoOfQuestions) - 2
        
            LabelforQuestions = ctk.CTkLabel(master=StatinAccTab_Frame, text="No. of Questions: {}".format(NoOfQuestions),font=ctk.CTkFont(family="Clash Grotesk",size=20, weight="bold"))
            LabelforQuestions.grid(row=0,column=0, sticky="nsew")

            LabelforWebScraps = ctk.CTkLabel(master=StatinAccTab_Frame, text="No. of WebScraps: None",font=ctk.CTkFont(family="Clash Grotesk",size=20, weight="bold"))
            LabelforWebScraps.grid(row=1,column=0, sticky="nsew")

            LabelforDOB = ctk.CTkLabel(master=StatinAccTab_Frame, text="Date of Birth: None",font=ctk.CTkFont(family="Clash Grotesk",size=20, weight="bold"))
            LabelforDOB.grid(row=2,column=0, sticky="nsew")

            LabelforEmail = ctk.CTkLabel(master=StatinAccTab_Frame, text="Email: None",font=ctk.CTkFont(family="Clash Grotesk",size=20, weight="bold"))
            LabelforEmail.grid(row=0,column=1, sticky="nsew")

            LabelforEmail = ctk.CTkLabel(master=StatinAccTab_Frame, text="Phone Number: None",font=ctk.CTkFont(family="Clash Grotesk",size=20, weight="bold"))
            LabelforEmail.grid(row=1,column=1, sticky="nsew")

            LabelforEmail = ctk.CTkLabel(master=StatinAccTab_Frame, text="BackUp: None",font=ctk.CTkFont(family="Clash Grotesk",size=20, weight="bold"))
            LabelforEmail.grid(row=2,column=1, sticky="nsew")

            logoutBTN = ctk.CTkButton(master=AccountsTab_Frame, text="Sign out", fg_color="#e62e2e", hover_color="OrangeRed4" ,font=ctk.CTkFont(family="Clash Grotesk",size=16,weight="bold"))
            logoutBTN.grid(row=3,column=0,sticky="se")




            ACCOUNTSTAB.configure(state= tk.DISABLED,fg_color="gray90")
            WEBSCRAPTAB.configure(state= tk.NORMAL,fg_color=["#3a7ebf", "#1f538d"])
            SOFTWAREINFOTAB.configure(state= tk.NORMAL,fg_color=["#3a7ebf", "#1f538d"])
            QUESTIONSTAB.configure(state= tk.NORMAL,fg_color=["#3a7ebf", "#1f538d"])

            def signout():
                Tab_frame.destroy()
                NonTab_FrameA.destroy()
                AccountPage()

            logoutBTN.configure(command=signout)
        
            def WebScrapTabPAGE():
                global NonTab_FrameW
                try:
                    NonTab_FrameA.destroy()
                except:
                    pass

                try:
                    NonTab_FrameS.destroy()
                except:
                    pass

                try:
                    NonTab_FrameQ.destroy()
                except:
                    pass

                NonTab_FrameW = ctk.CTkFrame(master=window,corner_radius=0, fg_color="transparent")
                NonTab_FrameW.pack(side=tk.RIGHT,expand = True, fill="both", anchor="e")

                sucess_label = ctk.CTkLabel(master=NonTab_FrameW, text="[ ! ] This Feature is in the works, set to be released in the version 1.1 of MathQBGEN.", font=ctk.CTkFont(family="Clash Grotesk",size=23,weight="normal"))
                sucess_label.place(relx=0.5,rely=0.5,anchor="center")

                ACCOUNTSTAB.configure(state= tk.NORMAL,fg_color=["#3a7ebf", "#1f538d"])
                WEBSCRAPTAB.configure(state= tk.DISABLED,fg_color="gray90")
                SOFTWAREINFOTAB.configure(state= tk.NORMAL,fg_color=["#3a7ebf", "#1f538d"])
                QUESTIONSTAB.configure(state= tk.NORMAL,fg_color=["#3a7ebf", "#1f538d"])

                return
            
            try:
                NonTab_FrameW.destroy()
            except:
                pass

            try:
                NonTab_FrameS.destroy()
            except:
                pass

            try:
                NonTab_FrameQ.destroy()
            except:
                pass
            
            

            def SoftwareInfoTabPAGE():
                try:
                    NonTab_FrameW.destroy()
                except:
                    pass

                try:
                    NonTab_FrameA.destroy()
                except:
                    pass

                try:
                    NonTab_FrameQ.destroy()
                except:
                    pass

                ACCOUNTSTAB.configure(state= tk.NORMAL,fg_color=["#3a7ebf", "#1f538d"])
                WEBSCRAPTAB.configure(state= tk.NORMAL,fg_color=["#3a7ebf", "#1f538d"])
                SOFTWAREINFOTAB.configure(state= tk.DISABLED,fg_color="gray90")
                QUESTIONSTAB.configure(state= tk.NORMAL,fg_color=["#3a7ebf", "#1f538d"])
                

                global NonTab_FrameS
                NonTab_FrameS = ctk.CTkFrame(master=window,corner_radius=0, fg_color="transparent")
                NonTab_FrameS.pack(side=tk.RIGHT,expand = True, fill="both", anchor="e")


                softwareTABIMGINDEED = Image.open('assets/softwareinfo.png')
                softwareTABIMGINDEED_tk = ImageTk.PhotoImage(softwareTABIMGINDEED)

                l1 = ctk.CTkLabel(master=NonTab_FrameS, image=softwareTABIMGINDEED_tk,text="")
                l1.place(relx=0.5,rely=0.5,anchor="center")



                return
            
            def QuestionsTabPAGE():

                try:
                    NonTab_FrameW.destroy()
                except:
                    pass

                try:
                    NonTab_FrameS.destroy()
                except:
                    pass

                try:
                    NonTab_FrameA.destroy()
                except:
                    pass


                ACCOUNTSTAB.configure(state= tk.NORMAL,fg_color=["#3a7ebf", "#1f538d"])
                WEBSCRAPTAB.configure(state= tk.NORMAL,fg_color=["#3a7ebf", "#1f538d"])
                SOFTWAREINFOTAB.configure(state= tk.NORMAL,fg_color=["#3a7ebf", "#1f538d"])
                QUESTIONSTAB.configure(state= tk.DISABLED,fg_color="gray90")

                global NonTab_FrameQ, dataINT
                NonTab_FrameQ = ctk.CTkFrame(master=window,corner_radius=0, fg_color="transparent")
                NonTab_FrameQ.pack(side=tk.RIGHT,expand = True, fill="both", anchor="e")

                NonTab_FrameQ.rowconfigure(0, weight=1)
                NonTab_FrameQ.rowconfigure(1, weight=3)
                NonTab_FrameQ.columnconfigure(0, weight=1)


                TOPQuestionTab_Frame = ctk.CTkFrame(master=NonTab_FrameQ, fg_color="transparent" )
                TOPQuestionTab_Frame.grid(row=0,column=0,sticky="nsew")

                TOPQuestionTab_Frame.rowconfigure(0,weight=1)
                TOPQuestionTab_Frame.columnconfigure(0,weight=3)
                TOPQuestionTab_Frame.columnconfigure(1,weight=1)

                TOPQuestionTab_Frame_RIGHT = ctk.CTkFrame(master=TOPQuestionTab_Frame, fg_color="transparent" )
                TOPQuestionTab_Frame_RIGHT.grid(row=0,column=1, sticky="nsew")

                TOPQuestionTab_Frame_RIGHT.rowconfigure((0,1,2,3,4),weight=1)
                TOPQuestionTab_Frame_RIGHT.columnconfigure(0,weight=1)

                TOPQuestionTab_Frame_LEFT = ctk.CTkFrame(master=TOPQuestionTab_Frame, fg_color="transparent")
                TOPQuestionTab_Frame_LEFT.grid(row=0,column=0, sticky="nsew")
                
                addqnIMG = Image.open("assets/addqnicon.png").resize((30,30))
                addqnIMG_tk = ImageTk.PhotoImage(addqnIMG)

                removeqnIMG = Image.open("assets/removeqnicon.png").resize((30,30))
                removeqnIMG_tk = ImageTk.PhotoImage(removeqnIMG)

                editqnicon = Image.open("assets/editqnicon.png").resize((30,30))
                editqnicon_tk = ImageTk.PhotoImage(editqnicon)

                genrandomqnicon = Image.open("assets/genrandomqnicon.png").resize((30,30))
                genrandomqnicon_tk = ImageTk.PhotoImage(genrandomqnicon)

                exportqnicon = Image.open("assets/exportqnicon.png").resize((30,30))
                exportqnicon_tk = ImageTk.PhotoImage(exportqnicon)

                def addQNTAB():
                    global dataINT
                    dataINT = activateADDQN()

                    shutil.move(dataINT["File"],f"Accounts/{username}")

                    return

                AddQuestionBTN = ctk.CTkButton(master=TOPQuestionTab_Frame_RIGHT, text="Add Question", fg_color="#2ea808", hover_color="chartreuse4", font=ctk.CTkFont(family="Clash Grotesk",size=16, weight="bold"), image=addqnIMG_tk, compound="left", command=addQNTAB)
                AddQuestionBTN.grid(row=0,column=0)

                EditQuestionBTN = ctk.CTkButton(master=TOPQuestionTab_Frame_RIGHT, text="Edit Question", font=ctk.CTkFont(family="Clash Grotesk",size=16, weight="bold"), image=editqnicon_tk, compound="left")
                EditQuestionBTN.grid(row=1,column=0)

                def viewqn():
                    filedialog.askopenfile(initialdir=f"Accounts/{username}",mode ='r', filetypes =[('Text Files', '*.txt')])
                    return

                ViewQuestionBTN = ctk.CTkButton(master=TOPQuestionTab_Frame_RIGHT, text="View Questions", font=ctk.CTkFont(family="Clash Grotesk",size=16, weight="bold"), image=exportqnicon_tk,command=viewqn, compound="left")
                ViewQuestionBTN.grid(row=2,column=0)

                GenRandomQuestionBTN = ctk.CTkButton(master=TOPQuestionTab_Frame_RIGHT, text="Pick Random Question", font=ctk.CTkFont(family="Clash Grotesk",size=16, weight="bold"), image=genrandomqnicon_tk, compound="left")
                GenRandomQuestionBTN.grid(row=3,column=0)

                RemoveQuestionBTN = ctk.CTkButton(master=TOPQuestionTab_Frame_RIGHT, text="Remove Question", font=ctk.CTkFont(family="Clash Grotesk",size=16, weight="bold"), image=removeqnIMG_tk, compound="left", fg_color="#e62e2e", hover_color="OrangeRed4")
                RemoveQuestionBTN.grid(row=4,column=0)


                BottomHalf_Frame = ctk.CTkFrame(master=NonTab_FrameQ, fg_color="transparent")
                BottomHalf_Frame.grid(row=1,column=0,sticky="nsew")

                QuestionCatalogue = Catalogue(username)

                QuestionCatalogue_Frame = ctk.CTkScrollableFrame(master=BottomHalf_Frame, fg_color="transparent", label_text="Questions Catalogue", label_font=ctk.CTkFont(family="Clash Grotesk",size=19, weight="bold"))
                QuestionCatalogue_Frame.pack(side=tk.TOP, fill="both", expand=True)

                
                for i in range(1,len(QuestionCatalogue.keys())+1):
                    

                    EACHQuestion_Frame = ctk.CTkFrame(master=QuestionCatalogue_Frame, height=150)
                    EACHQuestion_Frame.pack(expand=False,fill="x", padx=20,pady=10)
                    EACHQuestion_Frame.rowconfigure(0,weight=1)
                    EACHQuestion_Frame.columnconfigure(0,weight=1)
                    EACHQuestion_Frame.columnconfigure(1,weight=4)


                    global img_tk,img,QuestionCatalogue_LEFT_Canvas

                    QuestionCatalogue_LEFT_Canvas = tk.Canvas(master=EACHQuestion_Frame,height=150)
                    QuestionCatalogue_LEFT_Canvas.grid(row=0,column=0,sticky="nsew")
                    
                    QuestionCatalogue_RIGHT_Frame = ctk.CTkFrame(master=EACHQuestion_Frame,height=150)
                    QuestionCatalogue_RIGHT_Frame.grid(row=0,column=1,sticky="nsew")

                    qnNO = ctk.CTkLabel(master=QuestionCatalogue_RIGHT_Frame,text=f"Question number {i}", font=('Calibri', 15)) 
                    qnNO.pack(pady=9,padx=12)

                    ChapterQN = ctk.CTkLabel(master=QuestionCatalogue_RIGHT_Frame,text="Chapter Number : dataINT[Chapter]", font=('Calibri', 15)) 
                    ChapterQN.pack(pady=9,padx=12)

                    typeQN = ctk.CTkLabel(master=QuestionCatalogue_RIGHT_Frame,text="Question Type : dataINT[Type]", font=('Calibri', 15)) 
                    typeQN.pack(pady=9,padx=12)

                    diffQN = ctk.CTkLabel(master=QuestionCatalogue_RIGHT_Frame,text="Quesiton Difficulty : dataINT[Difficulty]", font=('Calibri', 15)) 
                    diffQN.pack(pady=9,padx=12)

                    



                
                return
            
            return 
            

        AccountsTabPAGE()
        ACCOUNTSTAB.configure(command=AccountsTabPAGE)
        WEBSCRAPTAB.configure(command=WebScrapTabPAGE)
        SOFTWAREINFOTAB.configure(command=SoftwareInfoTabPAGE)
        QUESTIONSTAB.configure(command=QuestionsTabPAGE)

        return
    
    def SignUpPage():
        global pass1,pass2,suuframe,back_btn
        frame.destroy()

        suuframe = ctk.CTkFrame(master=window)
        suuframe.place(anchor="c", relx=0.5, rely=0.5) 
  
        suulabel = ctk.CTkLabel(master=suuframe,text='Sign Up', font=("Calibri",24)) 
        suulabel.pack(pady=12,padx=10)

        suuuser_entry= ctk.CTkEntry(master=suuframe,placeholder_text="Username") 
        suuuser_entry.pack(pady=12,padx=10) 
  
        suuuser_pass= ctk.CTkEntry(master=suuframe,placeholder_text="Password",show="*") 
        suuuser_pass.pack(pady=12,padx=10)
        pass1 = suuuser_pass.get()

        suuuser_conpass= ctk.CTkEntry(master=suuframe,placeholder_text="Confirm Password",show="*") 
        suuuser_conpass.pack(pady=12,padx=10)
        pass2 = suuuser_conpass.get()

        def AccountCreation():
            global sucess_frame
            username = suuuser_entry.get()
            username = username.lower()
            password = suuuser_pass.get()
            mkdir(f'Accounts/{username}')
            with open(f"Accounts/{username}/{username}", "wb") as account:
                pickle.dump({password:username}, account)
            with open(f"Accounts/{username}/Catalogue",'wb') as Catalogue:
                pass
            
            suuframe.destroy()
            suubutton.destroy()
            back_btn.destroy()
            
            sucess_frame = ctk.CTkFrame(master=window)
            sucess_frame.pack(side=tk.BOTTOM, anchor="s", padx=20,pady=20)

            sucess_label = ctk.CTkLabel(master=sucess_frame, text="[ ! ] Account has been created, You shall Login.", font=('Calibri', 20))
            sucess_label.pack()
            AccountPage()




            return

        
        suubutton = ctk.CTkButton(master=suuframe,text='Sign Up',font=('Calibri', 15), command=AccountCreation) 
        suubutton.pack(pady=12,padx=10) 


        def backbtn():
            suuframe.destroy()
            back_btn.destroy()
            AccountPage()

        back_btn = ctk.CTkButton(master=window, text="<- Back" ,font=("Calibri", 18), command=backbtn)
        back_btn.pack(side=tk.TOP, anchor="nw")

  
    
    frame = ctk.CTkFrame(master=window)
    frame.place(anchor="c", relx=0.5, rely=0.5) 
  
    label = ctk.CTkLabel(master=frame,text='Login', font=("Calibri",24)) 
    label.pack(pady=12,padx=10)

    user_entry= ctk.CTkEntry(master=frame,placeholder_text="Username") 
    user_entry.pack(pady=12,padx=10) 
  
    user_pass= ctk.CTkEntry(master=frame,placeholder_text="Password",show="*") 
    user_pass.pack(pady=12,padx=10)

    def AccountCheck():
        global username

        username = user_entry.get()
        username = username.lower()
        password = user_pass.get()
        if username == "" and password == "":
            messagebox.showerror("Error", "Account does not exist")
        file_exists = exists(f"Accounts/{username}")
        if file_exists:
            with open(f"Accounts/{username}/{username}", "rb") as account:
                details = pickle.load(account)
                print("Account exists...")
                if password in details:
                    print("Password matches the username!")
                    
                    HomePage()

                else:
                    messagebox.showwarning("Error", "Passowrd does not match!")
        else:
            messagebox.showwarning("Error", "Account Does not exist, Please create an account by signing up!")
        
        return


    button = ctk.CTkButton(master=frame,text='Login',font=('Calibri', 15), command=AccountCheck) 
    button.pack(pady=12,padx=10) 
  
    suframe = ctk.CTkFrame(master=frame)
    suframe.pack(padx=12,pady=12)
    signup = ctk.CTkLabel(master=suframe,text='Don\'t have an account yet?', font=('Calibri', 15)) 
    signup.pack(side="left",padx=12)
    signupbtn = ctk.CTkButton(master=suframe, text="Signup",command=SignUpPage, font=('Calibri', 15))
    signupbtn.pack(side="left")


AccountPage()

window.mainloop()