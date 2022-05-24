from tkinter import *
from PIL import Image
from PIL import ImageTk
import webbrowser
#the canvas of the project

root = Tk()
root.title("Student Kit")
root.geometry("1280x720")
root.iconbitmap("logo.ico")
canvas = Canvas(root, height=1280, width=720)
bg = PhotoImage(file="backgroud.png")
canvas.pack(fill="both",expand=False)
canvas.create_image(0,0,image=bg,anchor="nw")
root.attributes('-alpha',0.9)

#Collage Websites
def Collage_Websites():
    def bttn(x,y,text,bcolor,fcolor,link):
        def website():
            webbrowser.open(link)

        def on_entr(e):
            myButton['background']=bcolor
            myButton['foreground']=fcolor

        def on_leave(e):
            myButton['background']=fcolor
            myButton['foreground']=bcolor

        
    

        myButton = Button(root,width=42,height=2,text=text,
                            fg=bcolor,
                            bg=fcolor,
                            border=0,
                            activeforeground=fcolor,
                            activebackground=bcolor,
                            command=website,font=("Raleway",10))

        myButton.bind("<Enter>",on_entr)
        myButton.bind("<Leave>",on_leave)

        myButton.place(x=x,y=y)

    bttn(860,360,"EDU SERVE","#ffcc66","#1b1b1b","https://eduserve.karunya.edu/Login.aspx?ReturnUrl=%2f")
    bttn(860,400,"Student Portal","#ccff66","#1b1b1b","https://online.karunya.edu/oauth/login?access=student")
    bttn(860,440,"Payment","#66ff66","#1b1b1b","https://karunya.edu/payments") 

def download_python():
    webbrowser.open("https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe")
def download_pycharm():
    webbrowser.open("https://download-cdn.jetbrains.com/python/pycharm-community-2022.1.exe")
def video_arulsir():
    webbrowser.open("https://www.youtube.com/watch?v=OZHhsIQ1-MQ")

def python_command():
    def bttn(x,y,text,bcolor,fcolor,download):

        def on_entr(e):
            myButton['background']=bcolor
            myButton['foreground']=fcolor

        def on_leave(e):
            myButton['background']=fcolor
            myButton['foreground']=bcolor

        
    

        myButton = Button(root,width=42,height=2,text=text,
                            fg=bcolor,
                            bg=fcolor,  
                            border=0,
                            activeforeground=fcolor,
                            activebackground=bcolor,
                            command=download,font=("Raleway",10))

        myButton.bind("<Enter>",on_entr)
        myButton.bind("<Leave>",on_leave)

        myButton.place(x=x,y=y)
    bttn(110,360,"P Y T H O N","#ffcc66","#1b1b1b",download_python)
    bttn(110,400,"P Y C H A R M","#ccdd66","#1b1b1b",download_pycharm)
    bttn(110,440,"Installation Video","#dd66bb","#1b1b1b",video_arulsir)
def download_codeblocks():
    webbrowser.open("https://download.fosshub.com/Protected/expiretime=1651717991;badurl=aHR0cHM6Ly93d3cuZm9zc2h1Yi5jb20vQ29kZS1CbG9ja3MuaHRtbA==/71603f369136edf1086efdf3037837a85726bb253ba6608f89ba291daecf1d58/5b85805cf9ee5a5c3e979f1b/5e80624f7d74bb810359a46c/codeblocks-20.03mingw-setup.exe")
def download_web():
    webbrowser.open("http://www.codeblocks.org/downloads/binaries/")
def video_youtube():
    webbrowser.open("https://www.youtube.com/watch?v=OZHhsIQ1-MQ")
def C_command():
    def bttn(x,y,text,bcolor,fcolor,download):

        def on_entr(e):
            myButton['background']=bcolor
            myButton['foreground']=fcolor

        def on_leave(e):
            myButton['background']=fcolor
            myButton['foreground']=bcolor

        
    

        myButton = Button(root,width=42,height=2,text=text,
                            fg=bcolor,
                            bg=fcolor,
                            border=0,
                            activeforeground=fcolor,
                            activebackground=bcolor,
                            command=download,font=("Raleway",10))

        myButton.bind("<Enter>",on_entr)
        myButton.bind("<Leave>",on_leave)

        myButton.place(x=x,y=y)
    bttn(110,360,"Code Blocks(20.3)","#ffcc66","#1b1b1b",download_codeblocks)
    bttn(110,400,"Code Blocks(website)","#ccdd66","#1b1b1b",download_web)
    bttn(110,440,"Installation Video","#dd66bb","#1b1b1b",video_youtube)
def open_IEEE():
    webbrowser.open("https://www.ieee.org/")
def open_science_direct():
    webbrowser.open("https://www.sciencedirect.com/")
def open_instructables():
    webbrowser.open("https://www.instructables.com/")

def evs_command():
    def bttn(x,y,text,bcolor,fcolor,download):

        def on_entr(e):
            myButton['background']=bcolor
            myButton['foreground']=fcolor

        def on_leave(e):
            myButton['background']=fcolor
            myButton['foreground']=bcolor

        
    

        myButton = Button(root,width=42,height=2,text=text,
                            fg=bcolor,
                            bg=fcolor,
                            border=0,
                            activeforeground=fcolor,
                            activebackground=bcolor,
                            command=download,font=("Raleway",10))

        myButton.bind("<Enter>",on_entr)
        myButton.bind("<Leave>",on_leave)

        myButton.place(x=x,y=y)
    bttn(110,360,"I E E E","#ffcc66","#1b1b1b",open_IEEE)
    bttn(110,400,"Science Direct","#ccdd66","#1b1b1b",open_science_direct)
    bttn(110,440,"Instructables","#dd66bb","#1b1b1b",open_instructables)

def Subject_Related():
    def bttn(x,y,text,bcolor,fcolor,command):

        def on_entr(e):
            myButton['background']=bcolor
            myButton['foreground']=fcolor

        def on_leave(e):
            myButton['background']=fcolor
            myButton['foreground']=bcolor

        
    

        myButton = Button(root,width=42,height=2,text=text,
                            fg=bcolor,
                            bg=fcolor,
                            border=0,
                            activeforeground=fcolor,
                            activebackground=bcolor,
                            command=command,font=("Raleway",10))

        myButton.bind("<Enter>",on_entr)
        myButton.bind("<Leave>",on_leave)

        myButton.place(x=x,y=y)
    bttn(110,360,"P Y T H O N","#ffcc66","#1b1b1b",python_command)
    bttn(110,400,"C Programing","#ccdd66","#1b1b1b",C_command)
    bttn(110,440,"E V S","#dd66bb","#1b1b1b",evs_command)





btn_inactive_1 = Image.open("collage_websites_1.png")
btn_active_1 = Image.open("collage_websites_2.png")
root.btn_inactive_1 = ImageTk.PhotoImage(btn_inactive_1)
root.btn_active_1 = ImageTk.PhotoImage(btn_active_1)
def on_enter(event):
    button_1.config(image=root.btn_active_1)
def on_leave(event):
    button_1.config(image=root.btn_inactive_1)
button_1 = Button(root,activebackground="#1b1b1b",bd=0, image=root.btn_inactive_1, bg="#1b1b1b",command=Collage_Websites)
canvas.create_window(750,420, window=button_1)

button_1.bind("<Enter>",on_enter)
button_1.bind("<Leave>",on_leave)

btn_inactive_4 = Image.open("subject_releted_1.png")
btn_active_4 = Image.open("subject_releted_2.png")
root.btn_inactive_4 = ImageTk.PhotoImage(btn_inactive_4)
root.btn_active_4 = ImageTk.PhotoImage(btn_active_4)
def on_enter(event):
    button_4.config(image=root.btn_active_4)
def on_leave(event):
    button_4.config(image=root.btn_inactive_4)
button_4 = Button(root,activebackground="#1b1b1b",bd=0, image=root.btn_inactive_4, bg="#1b1b1b",command=Subject_Related)
canvas.create_window(550,420, window=button_4)

button_4.bind("<Enter>",on_enter)
button_4.bind("<Leave>",on_leave)






mainloop()