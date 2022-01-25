#importing modules
from tkinter import *
from tkinter.filedialog import *
from PIL import ImageTk,Image
from stegano import exifHeader as stg
from tkinter import messagebox
     
def return_back(): 
    global dopened 
    DecScreen.withdraw()
    dopened = True
    #print(opened)
    Screen.deiconify()

#decoding the file
def Decode():
    global dopened, DecScreen
    Screen.withdraw()
    if dopened == True:
        DecScreen.deiconify()
    else:    
        DecScreen = Toplevel(Screen) 
        DecScreen.title("Decode-")
        DecScreen.geometry("500x500+300+300")
        DecScreen.config(bg="grey")
        def OpenFile():
            global FileOpen
            FileOpen=StringVar()
            FileOpen = askopenfilename(initialdir ="/Desktop",title="Select the File",filetypes=(("only jpeg files","*jpg"),("all type of files","*.*")))
            
        def Decoder():
            Message=stg.reveal(FileOpen)
            label3 = Label(DecScreen,text=Message)
            label3.place(relx=0.3,rely=0.3)
            
        SelectButton = Button(DecScreen,text="Select the file",command=OpenFile)
        SelectButton.place(relx=0.1,rely=0.4)
        DecodeButton=Button(DecScreen,text="Decode",command=Decoder)
        DecodeButton.place(relx=0.4,rely=0.5)
        button_exit = Button(DecScreen, text = "back",  command = return_back)
        button_exit.place(relx=0.6,rely=0.5)
 
def return_main(): 
    global eopened 
    EncScreen.withdraw()
    eopened = True
    Screen.deiconify()

#encoding the file
def Encode():
    global eopened, EncScreen
    Screen.withdraw()
    if eopened == True:
        EncScreen.deiconify()
    else:    
    
        EncScreen = Toplevel(Screen) 
        EncScreen.title("Encode-")
        EncScreen.geometry("500x500+300+300")
        EncScreen.config(bg="grey")
        label = Label(EncScreen,text=" Message")
        label.place(relx=0.1,rely=0.2)
        entry=Entry(EncScreen)
        entry.place(relx=0.5,rely=0.2)
        label1 = Label(EncScreen,text="Name of the File")
        label1.place(relx=0.1,rely=0.3)
        SaveEntry = Entry(EncScreen)
        SaveEntry.place(relx=0.5,rely=0.3)
        
        def OpenFile():
            global FileOpen
            FileOpen=StringVar()
            FileOpen = askopenfilename(initialdir ="/Desktop",title="SelectFile",filetypes=(("only jpeg files","*jpg"),("all type of files","*.*")))

            label2 = Label(EncScreen,text=FileOpen)
            label2.place(relx=0.3,rely=0.3)

        def Encoder():
            Response= messagebox.askyesno("PopUp","Do you want to encode the image?")
            if Response == 1:
                stg.hide(FileOpen,SaveEntry.get()+".jpg",entry.get())
                messagebox.showinfo("Pop Up","Successfully Encoded")
            else:
                messagebox.showwarning("Pop Up","Unsuccessful, please try again")
        
        
        SelectButton = Button(EncScreen,text="Select the file",command=OpenFile)
        SelectButton.place(relx=0.1,rely=0.4)
        EncodeButton=Button(EncScreen,text="Encode",command=Encoder)
        EncodeButton.place(relx=0.4,rely=0.5)
        button_exit = Button(EncScreen, text = "back",command = return_main)
        button_exit.place(relx=0.6,rely=0.5)
   
#Initializing the screen

Screen = Tk()
Screen.title("Image Steganography  ")
Screen.geometry("500x500+300+300")
file=PhotoImage(file="download.png")
label=Label(Screen,image=file)
label.place(x=0,y=0,relwidth=1,relheight=1)
Screen.config(bg= "grey")
y=Label(Screen, text="STEGNOGRAPHY",bg="black",fg="white",)
y.place(x=200,y=60)
x=Label(Screen, text="Hello Everyone Welcome To My GUI , Please Select What You Want",bg="black",fg="white")
x.place(x=80,y=100)

#creating buttons

EncodeButton = Button(text="Encode",command=Encode)
EncodeButton.place(relx=0.3,rely=0.4)


DecodeButton = Button(text="Decode",command=Decode)
DecodeButton.place(relx=0.6,rely=0.4)

eopened = False 
dopened = False

Screen.mainloop()
    

